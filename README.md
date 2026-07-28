# Esterke (אסתּרקע) — Aaron Zeitlin

A corrected digital edition of Aaron Zeitlin's four-act verse drama **Esterke**,
with an English reader's guide.

Zeitlin (1898–1973) takes up one of the founding legends of Polish Jewry — the
Jewish woman *Esterke*, said to have been the beloved of King Casimir the Great —
and turns it into a "Polish-Jewish mystery play" that runs from the
fourteenth-century royal court to a mystical epilogue on the ruins of a Jewish
inn, where the Wandering Jew and the shades of Y. L. Peretz and Adam Mickiewicz
meet at daybreak. It was for the 1940–41 Yiddish Art Theatre production of this
play that Zeitlin and Sholom Secunda wrote the song **"Dona Dona."** First
published in Warsaw in 1932 and reworked in 1967 — before and after the
destruction of Polish Jewry, which took Zeitlin's own family — it is at once a
national-historical pageant and an elegy for *Po-lin*, the legend of "here shall
you dwell."

> **On the text.** *Esterke* is in copyright. The scan and its OCR are already
> public through the Internet Archive / Yiddish Book Center; the corrected
> transcription and the guide here are offered for study, with thanks to those
> institutions. An official or print edition — or a published translation —
> should be arranged with the Yiddish Book Center and/or the Zeitlin estate.

---

## What to read

### The play, in Yiddish — the text itself
- **[`esterke_transcription.pdf`](esterke_transcription.pdf)** — a clean
  right-to-left reading edition (90 pp.): title, cast list, folio numbers in the
  margins for cross-reference, bold speaker-cues, set-off stage directions.
  **Start here.**
- **[`esterke_transcription.txt`](esterke_transcription.txt)** — the same text,
  plain and fully searchable.

  This is the whole play (Acts I–III and the Epilogue), corrected line by line
  against the scan. It corresponds to book folios **81–150**.

### The original scan — to check the transcription against
- **[`source/nybc200294.pdf`](source/nybc200294.pdf)** — *Gezamlte drames*,
  vol. 2 (Tel Aviv, 1980), also on the
  [Internet Archive](https://archive.org/details/nybc200294) courtesy the
  [Yiddish Book Center](https://www.yiddishbookcenter.org). *Esterke* runs from
  book folio 81 (PDF p. 85) to folio 150 (PDF p. 154). The raw OCR text layer,
  before correction, is in [`source/`](source/).

### An English guide — for orientation, or if you don't read Yiddish
- **[`digest/esterke_dialogue_summary.pdf`](digest/esterke_dialogue_summary.pdf)**
  — a scene-by-scene digest, laid out as a two-column "playbill," each speaker
  rendered in their own voice, with a closing glossary of the names, places, and
  terms (Łokietek, the Piast dynasty, Wiślica, the Frankists, Mickiewicz's
  "forty-four," and so on). A **paraphrase, not a translation.**
- **[`digest/esterke_dialogue_summary.md`](digest/esterke_dialogue_summary.md)**
  — the same guide in Markdown.

---

## About this edition

- **Method.** The Internet Archive added an OCR text layer to the scan in 2025;
  a correction script normalized its systematic artifacts, and then every page
  was compared by eye against the scan and its residual errors recorded. Those
  corrections — several hundred, wrong → right — are logged folio by folio in
  [`errata/esterke_errata.md`](errata/esterke_errata.md), which doubles as an
  account of the OCR's failure modes.
- **Orthography.** Digraphs are written as separate letters (וו · וי · יי) while
  the pasekh-tsvey-yudn ligature (ײַ) is kept — chosen for searchability and
  keyboard compatibility. To be recorded in the edition's note.
- **Two caveats worth knowing.** (1) The four inline footnotes come from the
  printed volume, but whether they are Zeitlin's or the 1980 editor's is
  **unverified** — the digest labels them "Footnote in the source." (2) The cast
  list carries a few of the scan's rougher OCR spellings that the correction pass,
  focused on the dialogue, did not fully reach.

## Regenerating the files

The [`scripts/`](scripts/) folder holds the tools (Python 3; the PDFs render
through headless Google Chrome):

```bash
python3 scripts/apply_errata.py apply       # → esterke_transcription.txt
python3 scripts/make_transcription_pdf.py   # → esterke_transcription.pdf
python3 scripts/make_summary_pdf.py         # → digest/esterke_dialogue_summary.pdf
```
