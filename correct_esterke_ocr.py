#!/usr/bin/env python3
"""
correct_esterke_ocr.py
Systematic cleanup of the Internet Archive OCR layer for Aaron Zeitlin's
"Esterke" (Gezamlte drames, vol. 2, Tel Aviv 1980, pp. 81-152;
scan: archive.org/details/nybc200294, PDF pages 83-154).

Fixes the error patterns documented by scan-vs-OCR comparison of
book pp. 81-88. Run on the raw extracted text, then proofread the
result against the scans — this script handles the systematic ~80-90%,
not the residual word-level misreadings.

Usage:
    pdftotext -f 83 -l 154 nybc200294.pdf esterke_raw.txt
    python3 correct_esterke_ocr.py esterke_raw.txt esterke_clean.txt
"""

import re
import sys

def clean(text: str) -> str:
    # ------------------------------------------------------------------
    # 1. Strip RTL/LTR embedding control characters inserted by pdftotext
    # ------------------------------------------------------------------
    text = re.sub("[\u202a\u202b\u202c\u200e\u200f]", "", text)

    # ------------------------------------------------------------------
    # 2. Page breaks -> visible markers
    # ------------------------------------------------------------------
    text = text.replace("\f", "\n\n═══ [page break] ═══\n\n")

    # ------------------------------------------------------------------
    # 3. Remove running headers (author name on even pages, play title
    #    on odd pages). They appear as isolated lines near page breaks.
    # ------------------------------------------------------------------
    header_patterns = [
        r"^\s*א\s*ה?\s*[רד]\s*[ןז]\s*$",          # אהרן (also misread אהרז/אחרן)
        r"^\s*אהרן\s+צייטלין\s*$",
        r"^\s*אחרן\s*$",
        r"^\s*צייטלין\s*$",
        r"^\s*א\s+ס\s+ת[ּ]?\s+ר\s+ק\s+ע\s*$",     # א ס ת ר ק ע (spaced title)
    ]
    lines = text.split("\n")
    lines = [ln for ln in lines
             if not any(re.match(p, ln) for p in header_patterns)]
    text = "\n".join(lines)

    # ------------------------------------------------------------------
    # 4. Re-join the split character cue ספּיטעק:
    #    OCR renders it as "סּיטעק:\nפ" or "פּיטעק:\nס"
    # ------------------------------------------------------------------
    text = re.sub(r"ס[ּ]?יטעק\s*:\s*\nפ[ּ]?\s*\n?", "ספּיטעק:\n", text)
    text = re.sub(r"פ[ּ]?יטעק\s*:\s*\nס\s*\n?", "ספּיטעק:\n", text)
    # split speaker names across lines generally: "באַריטש קאַ:" -> "באַריטשקאַ:"
    text = re.sub(r"באַריטש\s+קאַ\s*:", "באַריטשקאַ:", text)

    # ------------------------------------------------------------------
    # 5. RTL punctuation displacement.
    #    pdftotext puts sentence punctuation on the wrong side of the
    #    following word: "שלאָס .בישאָף" -> "שלאָס. בישאָף"
    #    Applies to . , ! ? ; :
    # ------------------------------------------------------------------
    text = re.sub(r"(\S)\s+([.,;])([\u0590-\u05FF])", r"\1\2 \3", text)
    # space before ? ! at clause end: "פּויפּסט ?" -> "פּויפּסט?"
    text = re.sub(r"\s+([?!])", r"\1", text)
    # "?!" misread as "? 1"
    text = re.sub(r"\?\s*1", "?!", text)
    # "!" misread as standalone "1" between Hebrew words
    text = re.sub(r"([\u0590-\u05FF])\s+1\s+([\u0590-\u05FF])", r"\1? \2", text)

    # ------------------------------------------------------------------
    # 6. Doubled-vav artifacts: װו / וו combinations misassembled.
    #    Normalize װ (U+05F0) followed by ו to plain double-vav 'וו',
    #    and collapse triple vavs.
    # ------------------------------------------------------------------
    text = text.replace("\u05f0\u05d5", "\u05d5\u05d5")   # װו -> וו
    text = text.replace("\u05f0", "\u05d5\u05d5")          # װ ligature -> וו
    text = re.sub("\u05d5{3,}", "\u05d5\u05d5", text)      # ווו+ -> וו
    # NOTE: this also collapses legitimate triple-vav in words like
    # "וווינען"; the errata pass restores those. Comment out if unwanted.

    # ------------------------------------------------------------------
    # 6b. Ligature normalization (applies corpus-wide).
    #     The 1980 typesetting/OCR yields Hebrew presentation ligatures;
    #     normalize to standard letter pairs per YIVO orthography.
    # ------------------------------------------------------------------
    text = text.replace("\u05f1", "\u05d5\u05d9")  # ױ -> וי  (פּױלן -> פּוילן)
    # ײ -> יי ONLY when not carrying a pasekh (ײַ stays as the standard
    # pasekh-tsvey-yudn ligature)
    text = re.sub("\u05f2(?!\u05b7)", "\u05d9\u05d9", text)
    # OCR typo forms that surface after normalization:
    text = text.replace("פּויילן", "פּוילן")
    text = text.replace("איייביק", "אייביק")

    # ------------------------------------------------------------------
    # 7. Known recurring misreadings (verified against scans, pp. 81-88)
    # ------------------------------------------------------------------
    replacements = {
        "שלאַכטפעלך": "שלאַכטפעלד",
        "קראַפּט": "קראַפט",
        "פּולנס": "פּוילנס",
        "פּולן.": "פּוילן.",
        "אײיביק": "אייביק",
        "באַלײידיק": "באַליידיק",
        "געקרײיציקט": "געקרייציקט",
        "אַדעלאַיראַ": "אַדעלאַידאַ",
        "א ויך": "אויך",
        "אָ  --": "אָ —",
        # verified via diff vs. hand-corrected pp. 81-88 (safe as whole
        # words / substrings anywhere in the play):
        "פּײַנט": "פײַנט",          # enemy; OCR adds spurious dagesh
        "פּייַנט": "פייַנט",         # same, decomposed-pasekh encoding
        "באַפּעלקערן": "באַפעלקערן",
        "ייַד": "ייִד",              # wrong vowel point under yud
        "ייָד": "ייִד",
    }
    for wrong, right in replacements.items():
        text = text.replace(wrong, right)

    # standalone וי is a misread of ווי ("how/as"); apply as whole word
    # only — never inside words (e.g. legitimate ...וי... sequences).
    text = re.sub(r"(^|\s)וי(\s)", r"\1ווי\2", text)

    # NOTE deliberately NOT automated: זי -> זיי (both are real words,
    # "she" vs "they" — context-dependent, errata pass only), and
    # letterspaced headings (ע ר ש ט ע ר  אַ ק ט), which are layout
    # features better handled editorially.

    # ------------------------------------------------------------------
    # 8. Em-dash spacing: OCR gives "  --" glued to next word
    # ------------------------------------------------------------------
    text = re.sub(r"\s*--\s*", " — ", text)

    # ------------------------------------------------------------------
    # 8b. Final mechanical rules (validated on pp. 81-88 diff)
    # ------------------------------------------------------------------
    # post-normalization triple-yud form of 'insult':
    text = text.replace("באַלייידיק", "באַליידיק")
    # stage-direction parens: "קעפּ)." -> "קעפּ.)" (RTL displacement)
    text = re.sub(r"\)([.,])", r"\1)", text)
    # colon displaced to next word: "זאַך :איך" -> "זאַך: איך"
    text = re.sub(r"(\S)\s+:([\u0590-\u05FF])", r"\1: \2", text)
    # standalone folio numbers (book page numbers) on their own line
    text = re.sub(r"^\s*\d{2,3}\s*$", "", text, flags=re.M)

    # ------------------------------------------------------------------
    # 9. Collapse excessive blank lines
    # ------------------------------------------------------------------
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    return text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    raw = open(sys.argv[1], encoding="utf-8").read()
    out = clean(raw)
    open(sys.argv[2], "w", encoding="utf-8").write(out)
    print(f"Wrote {len(out)} chars to {sys.argv[2]}")
    print("Next step: proofread against the page scans; "
          "apply the errata list for residual word-level errors.")
