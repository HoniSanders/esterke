#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render esterke_transcription.txt (the corrected Yiddish text) as a clean,
single-column, right-to-left reading PDF via headless Chrome.

    python3 scripts/make_transcription_pdf.py    → esterke_transcription.pdf
"""
import io, re, os, subprocess, tempfile, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TXT  = os.path.join(ROOT, "esterke_transcription.txt")
PDF  = os.path.join(ROOT, "esterke_transcription.pdf")

CSS = r"""
@page { size: 8.5in 11in; margin: 0.9in 0.95in 0.85in;
  @bottom-center { content: counter(page); font-family: Georgia, serif;
    font-size: 9pt; color: #9a9a9a; } }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { direction: rtl; text-align: right; margin: 0; color: #1a1a1a;
  font-family: "Taamey Frank CLM","Frank Ruehl CLM","New Peninim MT","SBL Hebrew",
               "Times New Roman","David CLM","Ezra SIL",serif;
  font-size: 13.5pt; line-height: 1.72; }
.title { text-align: center; margin: 6pt 0 0; }
.title .name { font-size: 30pt; font-weight: 700; letter-spacing: 2pt; color: #111; }
.title .auth { font-size: 13pt; color: #555; margin-top: 5pt; }
.title .ver  { font-size: 10pt; color: #8a8a8a; margin-top: 3pt; }
hr.rule { border: none; border-top: 1.2pt solid #7a1616; width: 34%;
  margin: 13pt auto 20pt; }
.folio { text-align: center; color: #b0a396; font-size: 9.5pt; letter-spacing: 1pt;
  margin: 15pt 0 7pt; }
.head { text-align: center; font-weight: 700; font-size: 16pt; letter-spacing: 4pt;
  color: #7a1616; margin: 14pt 0 10pt; }
.cue { font-weight: 700; color: #111; margin-top: 7pt; }
.dir { color: #6c6c6c; }
.gap { margin-top: 8pt; }
p { margin: 0; }
"""

HEB = lambda c: 'א' <= c <= 'ת'
def baseletters(tok): return sum(1 for c in tok if HEB(c))

def esc(s): return html.escape(s)

def build(lines):
    # lookups for blank neighbours (for heading detection)
    def blank(i): return i < 0 or i >= len(lines) or lines[i].strip() == ""
    out = ['<div class="title"><div class="name">אסתּרקע</div>'
           '<div class="auth">אהרן צייטלין</div>'
           '<div class="ver">איבערגעאַרבעטע ווערסיע · 1967</div></div>'
           '<hr class="rule">']
    marker = 0        # count of page-break markers seen
    depth = 0         # open-paren depth (stage directions)
    pending_gap = False
    def cls(*c):
        c = [x for x in c if x]
        return (' class="%s"' % " ".join(c)) if c else ""
    for i, raw in enumerate(lines):
        s = raw.rstrip("\n")
        if s.strip() == "":
            pending_gap = True
            continue
        # page-break marker → folio number
        if s.strip().startswith("═══") and "page break" in s:
            marker += 1
            depth = 0
            folio = 79 + marker           # marker 2 → folio 81 … marker 71 → folio 150
            if 81 <= folio <= 150:
                out.append(f'<div class="folio">· {folio} ·</div>')
            pending_gap = False
            continue
        gap = "gap" if pending_gap else ""
        pending_gap = False
        starts_paren = s.lstrip().startswith("(")
        in_dir = depth > 0 or starts_paren
        toks = s.split()
        is_cue = (depth == 0 and s.rstrip().endswith(":")
                  and s.count(":") == 1 and len(toks) <= 4)
        is_head = (marker >= 2 and depth == 0 and not is_cue and not starts_paren
                   and 1 <= len(toks) <= 3 and all(baseletters(t) <= 6 for t in toks)
                   and blank(i-1) and blank(i+1))
        if in_dir:
            out.append(f'<p{cls("dir", gap)}>{esc(s)}</p>')
        elif is_head:
            out.append(f'<div{cls("head", gap)}>{esc(s)}</div>')
        elif is_cue:
            out.append(f'<p{cls("cue", gap)}>{esc(s)}</p>')
        else:
            out.append(f'<p{cls(None, gap)}>{esc(s)}</p>')
        depth += s.count("(") - s.count(")")
        if depth < 0: depth = 0
    return "\n".join(out)

def main():
    lines = io.open(TXT, encoding="utf-8").read().split("\n")
    body = build(lines)
    doc = ("<!doctype html><html lang='yi' dir='rtl'><head><meta charset='utf-8'>"
           f"<title>אסתּרקע — אהרן צייטלין</title><style>{CSS}</style>"
           f"</head><body>{body}</body></html>")
    scratch = os.environ.get("SCRATCH", tempfile.gettempdir())
    htmlpath = os.path.join(scratch, "esterke_transcription.html")
    io.open(htmlpath, "w", encoding="utf-8").write(doc)
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    with tempfile.TemporaryDirectory() as ud:
        subprocess.run([chrome, "--headless=new", "--disable-gpu",
                        "--no-pdf-header-footer", f"--user-data-dir={ud}",
                        f"--print-to-pdf={PDF}", "file://" + htmlpath],
                       capture_output=True, text=True)
    print("html:", htmlpath)
    print("pdf :", PDF, "written" if os.path.exists(PDF) else "FAILED")

if __name__ == "__main__":
    main()
