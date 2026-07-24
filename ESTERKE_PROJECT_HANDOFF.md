# Esterke Digital Edition — Project Handoff Note

## Goal
Produce a verified, searchable digital Yiddish text of Aaron Zeitlin's play
**Esterke** (four-act "Polish-Jewish mystery," first publ. Globus 1932;
staged by Maurice Schwartz's Yiddish Art Theatre 1940–41; source of
"Dona Dona"). Eventual aim: offer the corrected text to the Yiddish Book
Center and/or the Zeitlin estate; ideally an English translation in collaboration with above.


## Source
- Scan: *Gezamlte drames*, vol. 2 (Tel Aviv, 1980), Internet Archive item
  [**nybc200294**](https://archive.org/details/nybc200294) (Yiddish Book Center / Spielberg Digital Yiddish Library).
- The May 2025 IA reprocessing added a Yiddish OCR text layer (GlyphLessFont).
  Quality: good, with systematic artifact families (documented below).
- **Esterke = PDF pages 83–154** (book folio pages 81–152). 318-page PDF.
- Vol. 2 also contains Yidnshtot (PDF 11–), Yankev Frank (PDF 155–),
  Vaytsman der tsveyter (PDF 251–).

## Page mapping
book folio = PDF page − 4. Cleaned-text page markers (`═══ [page break] ═══`)
count from the extraction start (PDF 83 = segment 0 = title page;
segment 1 = cast list = PDF 84 = folio 80[unnumbered]; segment 2 = PDF 85
= folio 81; thereafter segment n = PDF 83+n).

## Pipeline (reproducible)
1. `pdftotext -f 83 -l 154 nybc200294.pdf esterke_raw.txt`
2. `python3 correct_esterke_ocr.py esterke_raw.txt esterke_clean.txt`
   — **script FROZEN as of 2026-07-16** at ~96.7% word-level agreement
   with the hand-verified sample. All future fixes go through errata,
   not script changes, so errata stay stable.
3. Errata passes: compare page scans (rasterize at 150 dpi:
   `pdftoppm -jpeg -r 150 -f N -l N nybc200294.pdf pg`) against the
   corresponding cleaned-text segment. Record residual errors only, as:
   `folio p. / line or speech cue: wrong → right (note)`.
4. Apply errata to produce the final text; keep errata files as the audit
   trail.

## Status
- [x] Extraction (esterke_yiddish_ocr.txt, 65k chars)
- [x] Correction script (correct_esterke_ocr.py) — frozen
- [x] Script-cleaned full text (esterke_clean_scripted.txt)
- [x] Hand-verified reference sample: folios 81–88 (PDF 85–92)
      (esterke_corrected_act1_pp81-88.txt) — used to derive script rules
- [ ] Errata: folios 89–152 (PDF 93–154), ~64 pages, batches of 8–10
- [ ] Apply errata → final text
- [ ] Editorial note (orthography decisions, see below)
- [x] Contact Yiddish Book Center (drafts written; general-inquiries
      email is on yiddishbookcenter.org/contact-us; tel 413-256-4900)
- [ ] Identify/contact Zeitlin estate (ask YBC for guidance)

## Documented OCR artifact families (handled by script)
- RTL/LTR control chars from pdftotext
- Running headers (אהרן צייטלין / א ס ת ר ק ע) bleeding into text
- Split speaker cue ספּיטעק → "סּיטעק:\nפ"
- RTL punctuation displacement: "שלאָס .בישאָף" → "שלאָס. בישאָף";
  paren order "קעפּ)." → "קעפּ.)"
- "?!" misread as "? 1"; standalone "1" for ?/!
- Ligatures normalized: װ→וו, ױ→וי, bare ײ→יי (ײַ pasekh form KEPT)
- Em-dash spacing; folio numbers stripped; known word fixes
  (שלאַכטפעלד, פײַנט, ייִד, באַליידיק, אַדעלאַידאַ …)

## Known residual error types (errata-only, need eyes on scan)
- זי vs זיי (she/they — both real words)
- Line-end comma vs period; ? vs !
- Letterspaced headings (ע ר ש ט ע ר  אַ ק ט → ערשטער אַקט)
- Footnote placement (Zeitlin glosses Polish terms; OCR dumps them
  mid-page — reattach to their * anchors)
- Hyphenation/compounds, e.g. כלאָפּעס-קעניג (folio 85, flagged {?})
- Cast-list names vs dialogue: dialogue form wins (e.g. באַריטשקאַ,
  not cast-list OCR באַריטשלא; queen is אַדעלאַידאַ)

## Editorial decisions made
- Normalize to separate letters (וו/וי/יי), keep ײַ ligature — chosen for
  searchability/keyboard compatibility; record in the edition's note.
- Zeitlin's own footnotes restored inline under each page with their *.
- Page markers retain both folio and PDF numbers.

## Prompt for resuming errata work (new session)
"Continue the
errata pass for Zeitlin's Esterke: rasterize PDF pages N–M at 150 dpi,
compare each against the matching cleaned-text segment, and output only
errata entries (folio page / cue / wrong → right). Do not transcribe
full pages; the play is in copyright. Previous verified batch covered
folios 81–88 (esterke_errata.md); resume at folio 89 = PDF page 93."
