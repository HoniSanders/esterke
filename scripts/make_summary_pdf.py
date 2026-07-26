#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render esterke_dialogue_summary.md as a two-column, landscape (US-letter)
"playbill" PDF via headless Chrome.

    python3 make_summary_pdf.py

Outputs esterke_dialogue_summary.pdf (and a temp .html in the scratch dir).
"""
import io, re, os, sys, html, subprocess, tempfile, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD  = os.path.join(ROOT, "digest", "esterke_dialogue_summary.md")
PDF = os.path.join(ROOT, "digest", "esterke_dialogue_summary.pdf")

CSS = r"""
@page { size: 11in 8.5in; margin: 0.5in 0.62in 0.68in;
  @bottom-center { content: counter(page);
    font-family: "Palatino Linotype","Palatino",Georgia,serif; font-size: 8.5pt; color: #9a8f83; } }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Iowan Old Style","Palatino Linotype","Palatino","Hoefler Text","Georgia",serif;
  font-size: 9.2pt; line-height: 1.33; color: #1c1c1c; margin: 0;
  column-count: 2; column-gap: 0.5in; column-rule: 0.5pt solid #d9cfc4;
  text-align: justify; hyphens: auto; -webkit-hyphens: auto;
  orphans: 2; widows: 2;
}
/* ---- masthead (full width) ---- */
.masthead { column-span: all; margin: 0 0 13pt; padding-bottom: 9pt;
  border-bottom: 1.5pt solid #7a1616; text-align: left; }
.masthead h1 { margin: 0 0 5pt; font-size: 21pt; font-weight: 600;
  letter-spacing: .3pt; color: #7a1616; line-height: 1.1; }
.masthead p { margin: 3pt 0; font-size: 8.3pt; color: #34302c; line-height: 1.32;
  text-align: left; }
.masthead .who { columns: 3; column-gap: 0.34in; font-size: 8.1pt; margin-top: 5pt;
  list-style: none; padding: 0; }
.masthead .who li { margin: 0 0 2pt; padding-left: 0.85em; text-indent: -0.85em;
  break-inside: avoid; text-align: left; }
/* ---- act dividers (full width) ---- */
h1.act { column-span: all; text-align: center; margin: 13pt 0 9pt;
  padding-top: 7pt; border-top: 0.75pt solid #cbb9a8; }
h1.act .no  { display:block; font-size: 12.5pt; letter-spacing: 3.5pt; font-weight: 700;
  text-transform: uppercase; color: #7a1616; }
h1.act .sub { display:block; font-size: 9pt; font-style: italic; color: #6b6157;
  letter-spacing: .3pt; margin-top: 1pt; }
h1.act:first-of-type { border-top: none; padding-top: 0; margin-top: 2pt; }
/* ---- scenes ---- */
h2.scene { font-size: 9.6pt; font-weight: 700; color: #24160f; margin: 8pt 0 3pt;
  break-after: avoid; -webkit-column-break-after: avoid; text-align: left; }
h2.scene .ref { font-weight: 400; font-style: italic; color: #9a8f83; font-size: 8pt;
  white-space: nowrap; }
/* ---- dialogue ---- */
main ul { list-style: none; margin: 0 0 1pt; padding: 0; }
main li { margin: 0 0 2.6pt; padding-left: 1.15em; text-indent: -1.15em;
  break-inside: avoid; }
main li strong { font-weight: 700; color: #111; }
em { font-style: italic; color: #5a4f45; }
/* ---- footnotes (Zeitlin's glosses) ---- */
.fn-mark { color: #7a1616; font-weight: 700; font-size: 0.66em; vertical-align: super;
  line-height: 0; }
main p.fn { font-size: 7.7pt; color: #6b6157; line-height: 1.28; text-align: left;
  margin: 1.5pt 0 3pt; padding-left: 1.4em; text-indent: -1.4em; break-inside: avoid; }
main p.fn .fn-mark { vertical-align: baseline; font-size: 0.82em; margin-right: 0.35em; }
main p.fn em { color: #6b6157; }
main p.closing { column-span: all; text-align: center; font-style: italic;
  color: #6b6157; font-size: 8.4pt; margin: 12pt 0 0; padding-top: 8pt;
  border-top: 0.75pt solid #cbb9a8; }
"""

def inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*",     r"<em>\1</em>", s)
    s = re.sub(r"\^(\d+)", r'<sup class="fn-mark">\1</sup>', s)   # footnote anchors
    return s

def parse_blocks(lines):
    blocks, para, bullets = [], [], []
    def flush_p():
        if para: blocks.append(("p", " ".join(para))); para.clear()
    def flush_b():
        if bullets: blocks.append(("ul", list(bullets))); bullets.clear()
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.strip() == "":
            flush_p(); flush_b(); i += 1; continue
        if l.startswith("# "):
            flush_p(); flush_b(); blocks.append(("h1", l[2:].strip())); i += 1; continue
        if l.startswith("## "):
            flush_p(); flush_b(); blocks.append(("h2", l[3:].strip())); i += 1; continue
        if l.strip() == "---":
            flush_p(); flush_b(); i += 1; continue          # drop rules
        if l.startswith("- "):
            flush_p()
            b = l[2:]
            j = i + 1
            while j < len(lines) and lines[j].startswith("  "):
                b += " " + lines[j].strip(); j += 1
            bullets.append(b); i = j; continue
        flush_b(); para.append(l.strip()); i += 1
    flush_p(); flush_b()
    return blocks

def h2_html(text):
    text = re.sub(r"\s*(\(folios?[^)]*\))\s*$", r' <span class="ref">\1</span>', text)
    # the ref span was escaped-safe already since no special chars; inline the rest
    m = re.match(r"(.*?) <span", text)
    if m:
        head = inline(m.group(1)); rest = text[m.end(1):]
        return head + rest
    return inline(text)

def act_html(text):
    if " — " in text:
        no, sub = text.split(" — ", 1)
        return f'<span class="no">{html.escape(no)}</span><span class="sub">{html.escape(sub)}</span>'
    return f'<span class="no">{html.escape(text)}</span>'

def render(blocks):
    # masthead = everything before the first ACT/EPILOGUE h1
    k = next(i for i, b in enumerate(blocks)
             if b[0] == "h1" and re.match(r"(ACT|EPILOGUE)\b", b[1]))
    head, body = blocks[:k], blocks[k:]
    out = ['<header class="masthead">']
    for t, c in head:
        if t == "h1":  out.append(f"<h1>{inline(c)}</h1>")
        elif t == "p": out.append(f"<p>{inline(c)}</p>")
        elif t == "ul":
            cls = ' class="who"' if any(c[0].startswith("**") and "—" in c[0] for _ in [0]) else ""
            lis = "".join(f"<li>{inline(x)}</li>" for x in c)
            out.append(f"<ul{cls}>{lis}</ul>")
    out.append("</header>\n<main>")
    for idx, (t, c) in enumerate(body):
        if t == "h1":  out.append(f'<h1 class="act">{act_html(c)}</h1>')
        elif t == "h2": out.append(f'<h2 class="scene">{h2_html(c)}</h2>')
        elif t == "ul":
            lis = "".join(f"<li>{inline(x)}</li>" for x in c)
            out.append(f"<ul>{lis}</ul>")
        elif t == "p":
            mfn = re.match(r"\[FN(\d+)\]\s*(.*)", c)
            if mfn:
                out.append(f'<p class="fn"><span class="fn-mark">{mfn.group(1)}</span> '
                           f'{inline(mfn.group(2))}</p>')
            else:
                cls = ' class="closing"' if idx == len(body) - 1 else ""
                out.append(f"<p{cls}>{inline(c)}</p>")
    out.append("</main>")
    return "\n".join(out)

def main():
    lines = io.open(MD, encoding="utf-8").read().split("\n")
    body = render(parse_blocks(lines))
    doc = ("<!doctype html><html><head><meta charset='utf-8'>"
           f"<title>Esterke — dialogue digest</title><style>{CSS}</style>"
           f"</head><body>{body}</body></html>")
    scratch = os.environ.get("SCRATCH", tempfile.gettempdir())
    htmlpath = os.path.join(scratch, "esterke_summary.html")
    io.open(htmlpath, "w", encoding="utf-8").write(doc)

    chrome = ("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
    outpdf = os.path.abspath(PDF)
    with tempfile.TemporaryDirectory() as ud:
        cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
               f"--user-data-dir={ud}", f"--print-to-pdf={outpdf}",
               "file://" + htmlpath]
        r = subprocess.run(cmd, capture_output=True, text=True)
    ok = os.path.exists(outpdf)
    print("html:", htmlpath)
    print("pdf :", outpdf, "written" if ok else "FAILED")
    if not ok:
        print(r.stdout[-800:]); print(r.stderr[-800:])

if __name__ == "__main__":
    main()
