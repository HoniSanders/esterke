# Esterke — a digital edition

A corrected, searchable digital text of Aaron Zeitlin's Yiddish play **Esterke**
(a four-act "Polish-Jewish mystery"; first published Globus, 1932; reworked
version, 1967), together with an English reader's digest. Source: the scan of
*Gezamlte drames*, vol. 2 (Tel Aviv, 1980), from the [Yiddish Book
Center](https://www.yiddishbookcenter.org)'s Spielberg Digital Yiddish Library —
Internet Archive item [**nybc200294**](https://archive.org/details/nybc200294).
The play occupies book folios 81–150 (PDF pages 85–154).

> **Copyright.** *Esterke* is in copyright (Aaron Zeitlin, d. 1973). The source
> scan and its OCR layer are already public through the Internet Archive /
> [Yiddish Book Center](https://www.yiddishbookcenter.org); the corrected text and
> digest here are shared for study and scholarship, with thanks to those
> institutions. An official or print edition — or a published translation —
> should be arranged with the Yiddish Book Center and/or the Zeitlin estate.

## Layout

```
esterke_transcription.txt                   ← the corrected transcription (main product), folios 81–150
esterke_transcription.pdf                   ← the transcription typeset as a clean right-to-left reading PDF
source/
  nybc200294.pdf                    ← the Internet Archive scan (input)
  esterke_yiddish_ocr.txt           ← raw OCR text layer, as extracted
  esterke_clean_scripted.txt        ← OCR after the frozen correction script (baseline for errata)
errata/
  esterke_errata.md                 ← scan-vs-clean errata for the whole play (audit trail)
digest/
  esterke_dialogue_summary.md       ← English scene-by-scene digest (paraphrase, I/you voice)
  esterke_dialogue_summary.pdf      ← the digest as a 2-column landscape "playbill"
scripts/
  correct_esterke_ocr.py            ← the frozen OCR-correction script
  apply_errata.py                   ← applies errata/ → esterke_transcription.txt
  make_summary_pdf.py               ← renders digest .md → .pdf (headless Chrome)
  make_transcription_pdf.py         ← renders esterke_transcription.txt → RTL reading .pdf
```

## Pipeline

1. **Extract** the OCR layer from the scan (folios are PDF page − 4):
   `pdftotext -f 83 -l 154 source/nybc200294.pdf source/esterke_yiddish_ocr.txt`
   *(pdftotext/pdftoppm aren't installed on this machine — rasterize with
   Ghostscript instead: `gs -q -dNOPAUSE -dBATCH -sDEVICE=jpeg -r150 -dFirstPage=N
   -dLastPage=N -sOutputFile=pg-N.jpg source/nybc200294.pdf`.)*
2. **Clean** with the frozen script (tuned to ≈96.7% word agreement against a
   corrected sample of folios 81–88; all further fixes go through errata, not the
   script):
   `python3 scripts/correct_esterke_ocr.py <raw> source/esterke_clean_scripted.txt`
3. **Errata pass** — every cleaned page was compared against the scan (150 dpi;
   400 dpi for the few `{verify}` spots) and residual errors recorded in
   `errata/esterke_errata.md`.
4. **Apply** the errata to produce the final text:
   `python3 scripts/apply_errata.py` (dry-run coverage report) → `… apply`
   (writes `esterke_transcription.txt`).

## Reproduce

```bash
python3 scripts/apply_errata.py apply       # → esterke_transcription.txt
python3 scripts/make_transcription_pdf.py   # → esterke_transcription.pdf   (RTL reading edition)
python3 scripts/make_summary_pdf.py         # → digest/esterke_dialogue_summary.pdf
```
Both scripts resolve their own paths, so they can be run from anywhere.
`make_summary_pdf.py` drives **headless Google Chrome** to render the two-column
landscape PDF; edit the `CSS` block near its top to restyle.

## Notes on the digest

- Organized **by scene**, each speaker in the first/second person (**I** speaking,
  **you** addressed); stage directions in third person.
- Four numbered footnotes are carried over from the printed source and labeled
  *"Footnote in the source"* — their authorship (Zeitlin vs. the 1980 volume's
  editor) is **unverified**. A short editorial glossary ("Notes — names, places &
  terms") at the end is the digest editor's own.

## Status

Errata pass and final text: **complete** (folios 81–150). Digest + PDF: complete.
Outstanding: an editorial note on orthography; identifying/contacting the Zeitlin
estate (ask the YBC for guidance). A LaTeX rebuild of the PDF (for true
bottom-of-page footnotes) is possible but not done.
