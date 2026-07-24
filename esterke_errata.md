# Esterke — Errata List (Folios 81–88)

Baseline compared: `esterke_clean_scripted.txt` (script-cleaned OCR, frozen version)
Reference: hand-verified transcription against page scans (PDF pp. 85–92 = book
folios 81–88).

Format: `folio page — SCRIPT OUTPUT → CORRECTED`
Line-wrap differences (script joining/splitting lines differently) are noted
but are formatting, not textual, errors.

---

### Folio 81
- Heading: `ערשט ער / אַק ט` → `ערשטער אַקט` (letterspaced heading joined)
- `זי האָבן ווידער` → `זיי האָבן ווידער` (she→they; meaning-bearing)
- `זיי!וועט` → `זיי! וועט` (missing space after !)
- Line break: "אָרעם געווען די היים —" belongs on its own line before
  "פון האָלץ אַ כאַטע..."

### Folio 82
- Line break: "כיטרע זענען פּוילנס שׂונאים —" own line
- Line break: "וווילזײַן דאַרף מען — שטעט באַפעלקערן —" own line, "דוקאַטן —
  האַנדל." follows

### Folio 83
- `האָט יעדער ריטער,` → `האָט יעדער ריטער.` (comma→period, end of speech)
- `ספּיטעק, דאָס איז שלעכט` → `ספּיטעק, דאָס איז שלעכט —` (missing dash)
- Line break: "און אַז נישט —" ends a line before "האָבן מיר נישט פּוילן..."
- Line break: "אַז די ריטערס קלײַבן זיך אַהער —" own line
- `אַלע אויף להכעיס` → `אַלץ אויף להכעיס` ("everything," not "everyone" —
  meaning-bearing)

### Folio 84
- `פּוילנס קרול *,` → `פּוילנס קרול*.` (footnote marker spacing + punctuation)
- `דער אומגערעכטער,` → `דער אומגערעכטער.`
- Line break: "...קירך —" ends a line before "שטעל איך זיך..."
- Footnote: `* קרול / = / קעניג: / מלך.` → `* קרול = קעניג: מלך.` (OCR
  broke the footnote across lines)

### Folio 85
- Line break: "עס האָט דײַן וואָרט אָט ערשט אַזוי געלויכטן —" own line
- Line break: "וויל מען גליק פאַר פּוילן —" own line
- `כלאָפּעסיקעניג` → `כלאָפּעס-קעניג {?}` — OCR merged the hyphen into the
  word; **reading still uncertain, flagged for a closer look at this word
  specifically** (contraction of "peasants' king" as an insult — plausible
  but not fully confirmed against the scan resolution used)
- `מײַן שוועל!` → `מײַן שוועל?` (exclamation→question mark)
- Footnote: `(יעזוס.)` → `(יעזוס).` (period inside vs. outside parenthesis)

### Folio 86
- `אויפן קרייץ,` → `אויפן קרייץ.`
- `נישט אַליין!` → `נישט אַליין?`
- `געקריייציקטער?!דײַן` → `געקרייציקטער?! דײַן` (triple-yud OCR artifact;
  missing space after ?!)
- `נאָר ווינט דען יעזוס... דאָרט ווינען` → `נאָר וווינט דען יעזוס... דאָרט
  וווינען` (וווינט/וווינען = "dwells/dwell," lost a vav — meaning-bearing:
  not the same as ווינט "wind/cries")
- Same fix repeated: `ס'ווינט` → `ס'וווינט`, `ווינען` → `וווינען` two lines
  down

### Folio 87
- `געקריייציקטער באַגערט` → `געקרייציקטער באַגערט` (triple-yud artifact)
- `פון דײַנס גלײַכן` → `פון דײַנס גלײַכן.` (missing final period)
- `ריטערס זאָגן אויך :` → `ריטערס זאָגן אויך:` (displaced colon)
- `דו הער, קאַזימיר :` → `דו הער, קאַזימיר:` (displaced colon)

### Folio 88
- Line break: "פינצטערער" and "בעל-דבב?" were split across lines, should
  read together: "אַז נישט דער פינצטערער בעל-דבב?"
- `געקומען דאָ מיט מיר,` → `געקומען דאָ מיט מיר.`
- `פוֹן דעם באָרקאָוויטש.` → `פון דעם באָרקאָוויטש.` (stray vowel point)
- `ווער  1דער מאַטשקאָ?` → `ווער? דער מאַטשקאָ?` ("? 1" artifact not fully
  caught by the script's general rule in this instance — question mark
  placement differs from the pattern)
- `געקריייציקטן?` → `געקרייציקטן?` (triple-yud artifact)
- `קיין קריסט נישט!` → `קיין קריסט נישט?` (exclamation→question)
- `וועט קריייציקן` → `וועט קרייציקן` (triple-yud artifact)

---

## Summary of error types in this batch (36 entries, 8 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| Line-wrap/lineation differences | 10 | No — editorial layout choice |
| End punctuation (.  , ? !) | 12 | Partially — some patterns too varied |
| זי/זיי (she/they) | 1 | No — context-dependent |
| וווינט/וווינען vav-drop | 3 | Possibly — recurring word, could add |
| Triple-yud (קריייציקט forms) | 4 | Yes — should add to script |
| Footnote formatting | 2 | No — needs structural handling |
| Uncertain reading (flagged) | 1 | N/A — needs visual re-check |
| Stray vowel point (פוֹן) | 1 | Possibly — rare artifact |

**Recommended script addition:** the קריייציקט (triple-yud) pattern recurs
4 times in 8 pages and is fully mechanical — `text.replace("קריייציקט",
"קרייציקט")` would catch it corpus-wide. Not yet added, per the decision
to keep the script frozen; flagging here for a deliberate version-2 pass
if you want one.
