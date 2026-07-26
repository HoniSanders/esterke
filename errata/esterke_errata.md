# Esterke — Errata (folios 81–150, complete)

Scan-vs-cleaned-text errata for the whole play, compiled batch by batch during
the correction pass. Baseline: `source/esterke_clean_scripted.txt`; reference:
the IA scan `source/nybc200294.pdf` rasterized at 150 dpi (400 dpi for the few
`{verify}` spots). These corrections are applied by `scripts/apply_errata.py`
to produce `esterke_transcription.txt`; kept here as the audit trail.

---

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

---

# Esterke — Errata List (Folios 89–96)

Baseline compared: `esterke_clean_scripted.txt` (script-cleaned OCR, frozen version).
Reference: page scans rasterized from `nybc200294.pdf` at 150 dpi via Ghostscript
(`gs -r150 -sDEVICE=jpeg -dFirstPage=N -dLastPage=N`), PDF pp. 93–100 =
book folios 89–96 = cleaned-text segments 10–17.

Format: `folio cue — SCRIPT OUTPUT → CORRECTED (note)`
Line-wrap differences (script joining/splitting lines differently) are noted
as formatting, not textual, errors. Punctuation-order inside stage-direction
parentheses follows the edition's rule (period OUTSIDE the closing paren, per
the folio-85 `(יעזוס).` precedent).

---

### Folio 89 (PDF 93)
- `וואַרף! מיט מיר איז גאָט,` → `... גאָט.` (Baritshka; comma→period, end of speech)
- `... טיילט מיט דיר די קרוין!` → `... די קרוין?` (Spitek; rhetorical question, !→?)
- `... נישט דאָס געלעגער. גאָרנישט,` → `... גאָרנישט.` (Kazimir; comma→period)
- `... דאָס געטומל.)` → `... דאָס געטומל).` (stage dir.; period outside paren)
- Line-wrap: "זי ווייס אפשר אַליין נישט —" belongs on its own line before
  "שטייען לאַנדגראַפן און ריטערס טײַטשישע..." (script joined them)

### Folio 90 (PDF 94)
- `פאַר דײַן מאַן און קעניג בויג די קבי.` → `... בויג די קני.` (**קבי → קני**,
  "knee"; meaning-bearing OCR error)
- `... דער קלויסטער נישט געהייליקט!?` → `... געהייליקט?` (scan shows single ?)
- `(... ווי אַרײַנגעשטופּט פון דעם ריטער-המון.)` → `... ריטער-המון).` (period
  outside paren)
- `קאַזימיר ...פּײַניק מיך נישט מער..` → `קאַזימיר... פּײַניק מיך נישט מער...`
  (ellipsis spacing; two-dot → three-dot at line end)
- `... יאָרן לאַנג געבענקט,` → `... געבענקט.` (Kazimir; comma→period)
- Line-wrap + speaker merge: script ran "די זעלבע אויגן נאָך — די ליפּן האָבן
  קיינעם נישט געקושט —" together and pulled the following speaker cue
  `אַדעלאַידאַ:` onto the same line. Scan has three lines: "די זעלבע אויגן
  נאָך —" / "די ליפּן האָבן קיינעם נישט געקושט —" / then cue אַדעלאַידאַ:.

### Folio 91 (PDF 95)
- `... אַ קינד מיר שולדיק,` → `... שולדיק.` (Adelaida; comma→period)
- `כ'וואָלט זיך אַלייין צו ליבשאַפט` → `... אַליין ...` (triple-yud artifact
  אַלייין → אַליין)
- `... די שׂונאים דאַרפן. דיך אַלייין` → `... דיך אַליין` (triple-yud, 2nd occ.)
- `זאָל בעסער ס'טיייטשע לאַנדגראַפל` → `... ס'טײַטשע ...` (triple-yud + pasekh
  form: ס'טיייטשע → ס'טײַטשע, "the German [landgrave]")
- `... וועל איך האָרכן :` → `... האָרכן:` (displaced colon; space before → after)
- `קערט זיך אַלץ נישט אום מײַן האַר צו מיר?!` → `... צו מיר?` (scan shows single ?)
- Line-wrap: script joined "אײַנצאָלן ... דאָס צוגעזאָגטע געלט — צוויי טויזנט
  קאָפּעס גראָשנס פּוילישע. אַזוי פיל יאָרן —" onto one line; scan breaks after
  "געלט —" and after "יאָרן —".

### Folio 92 (PDF 96)
- `אייביק וועט עס פרעגן ס'האַרץ אין מיר,` → `... אין מיר.` (comma→period)
- `איך גיי,` → `איך גיי.` (comma→period)
- `(גלײַכט זיך אויס ... גייט פּאַמעלעך אַרויס.)` → `... אַרויס).` (period outside paren)
- `איז עס נישט די קעניגין  1כ'פאַרשטיי נישט.` → `... די קעניגין? כ'פאַרשטיי נישט.`
  (**"? 1" artifact**: the "1" is a dropped question mark; also restores the
  space before כ')
- `דײַן קעניגין,` → `דײַן קעניגין.` (comma→period)
- `דאָס געליאַרעם דרוייסן ווערט דראָעוודיק` → `... דרויסן ...` (extra-yud: דרוייסן
  → דרויסן)
- `העכער פון זיי אַלעמען שרײַט איינער,` → `... שרײַט איינער.` (comma→period)
- Speaker-cue scramble: script produced `יענעם` / `מאַטשקאָ` / (blank) /
  `לאָז אַרײַן(. קאָכאַן — אָפּ.)` / `באָרקאָוויטש:`. Scan reads —
  Kazimir: **"יענעם ... לאָז אַרײַן. (קאָכאַן — אָפּ)."** then the speaker cue
  **"מאַטשקאָ באָרקאָוויטש:"**. Two fixes: (a) the detached `מאַטשקאָ` belongs to
  the *next* speaker cue (character = Matshko Barkovitsh), not to Kazimir's
  line; (b) `לאָז אַרײַן(. קאָכאַן — אָפּ.)` → `לאָז אַרײַן. (קאָכאַן — אָפּ).`
  (paren/period displacement).
- `(קומט אַרײַן, נייגט זיך.)` → `... נייגט זיך).` (period outside paren)
- `האָב איך דען, קרול מײַנער, אַזוי געליאַרעמט!` → `... געליאַרעמט?` (!→?)

### Folio 93 (PDF 97)
This page is a run of Barkovitsh's rhetorical questions; the script rendered
several sentence-final `?` as `!`.
- `וואָס האָסטו דען געזאָגט!` → `... געזאָגט?` (!→?)
- `... זײַן דער לעצטער פּיאַסט!` → `... פּיאַסט?` (!→?)
- `ווּ איז זײַן טראָןדיורש?` → `ווּ איז זײַן טראָן-יורש?` (**טראָןדיורש → טראָן-יורש**;
  OCR merged the compound and inserted a stray ד — "throne-heir")
- `... פאַריאָגט ... דאָס ווײַב זײַנס!` → `... זײַנס?` (!→?)
- `ביסטו נישט איינער פון קאַזימירס ראָטלײַט!` → `... ראָטלײַט?` (!→?)
- `ווער רייצט דאָס קעגן מיר דאָס ריטערפאָלק!` → `... ריטערפאָלק?` (!→?)
- `דאָס טוען אַנ דע רע. איך — נישט. איך בין געטרל.` → `דאָס טוען אַנדערע. איך —
  נישט. איך בין געטרײַ.` (letterspaced אַנ דע רע → אַנדערע "others"; **געטרל →
  געטרײַ** "loyal", OCR mangled word)
- `דײַן פאַלשקייט איז מיר וויל באַקאַנט, באָרקאָוויטש,` → `... וווֹיל באַקאַנט,
  באָרקאָוויטש.` (vav-drop: וויל → ווויל "well[-known]"; comma→period at end)
- `איך בין געטרל.` → `איך בין געטרײַ.` (געטרל → געטרײַ, 2nd occ.)
- Speaker cue `באַרקאָוויטש:` → `באָרקאָוויטש:` (name spelling: pasekh→komets
  aleph, consistency)
- `(לאָזט אַראָפּ דעם קאָפּ.)` → `... דעם קאָפּ).` (period outside paren)
- `(רופט,)` → `(רופט).` (comma inside → period outside paren)
- `(קאָכאַן און גאָוואָרעק ... קומען אַרײַן.)` → `... קומען אַרײַן).` (period
  outside paren)
- `געעפנט טיר און טוייער!` → `... און טויער!` (extra-yud: טוייער → טויער)

### Folio 94 (PDF 98)
- `(די וועכטערס ... דער זאַל ווערט פול מיט ריטער-לײַט.)` → `... ריטער-לײַט).`
  (period outside paren)
- `אַרײַנפירן די פירשטין, וואָס בײַ מיר אין שלאָס,` → `... אין שלאָס.` (comma→period)
- `(קאָכאַן און גאָוואָרעק — אָב.)` → `... — אָפּ).` (**אָב → אָפּ** "exit", OCR read
  פּ as ב; also period outside paren)
- `אײַך אַלעמען דערווידער ועט אַרײַן דאָ` → `... וועט אַרײַן דאָ` (vav-drop: ועט → וועט)
- `דײַן האַר ...דו קנעכטיש ווײַב!` → `דײַן האַר... דו ...` (ellipsis spacing)
- Line-wrap: script split the stage cue `(צו באַריטשקאַן, / באָרקאָוויטשן / און
  די ריטערס)` across three lines; scan has it on one line.

### Folio 95 (PDF 99)
- `... אויגן וויפל סוויל דער קעניג.` → `... וויפל ס'וויל דער קעניג.` (missing
  apostrophe: סוויל → ס'וויל)
- `אַלע זענען זיי אַזוי ...דער האַר ...דער קעניג...` → `... אַזוי... דער האַר...
  דער קעניג...` (ellipsis spacing)
- `ווי אַ העלער העלדך -פּאַנצער.` → `ווי אַ העלער העלדן-פּאַנצער.` (**העלדך → העלדן**,
  OCR read ן as ך; hyphen re-seated: "hero's-armor")
- `אָ. וען איך בין קעניג —` → `אָ, ווען איך בין קעניג —` (period→comma; vav-drop
  וען → ווען). Script also merged the following cue `קאַזימיר:` onto this line;
  it belongs on its own line (Barkovitsh's line ends at the dash).
- `אים אוייסטאַנצן.` → `אים אויסטאַנצן.` (extra-yud: אוייסטאַנצן → אויסטאַנצן)
- `זי זענען דאָ פאַראַן?` → `זיי זענען דאָ פאַראַן?` (**זי → זיי**, "they" not
  "she"; meaning-bearing)
- `קאָן דער גאָרנישט זײַן פּאַראַן!` → `... זײַן פאַראַן?` (dagesh dropped פּ→פ for
  consistency with זענען דאָ פאַראַן above; !→?)
- `(מיט צוגעמאַכטע אויגן, איסגעצויגענע הענט,` → `... אויסגעצויגענע הענט,`
  (vav-drop: איסגעצויגענע → אויסגעצויגענע, "outstretched")
- Line-wrap: script joined "ווי דער קעניג וויל. באַפעלט דער קעניג — קוק איך..."
  onto one line; scan breaks after "באַפעלט דער קעניג —".

### Folio 96 (PDF 100)
- `(נאָכן טאַנץ ... דעם קעניג צו די פיס.)` → `... צו די פיס).` (period outside paren)
- Speaker-cue scramble: script produced `ָרוקויט ש:` / `אאָ` / `ב` (RTL
  fragmentation). Scan reads the single speaker cue **`באָרקאָוויטש:`**.
- `(ענטפערט נישט.)` → `(ענטפערט נישט).` (period outside paren)
- `קאָנסט גיין צוריק, יאַדווויגאַ.` → `... יאַדוויגאַ.` (extra-vav: יאַדווויגאַ →
  יאַדוויגאַ)
- `(אָפּ, נישט קוקנדיק אויף קיינעם.)` → `... אויף קיינעם).` (period outside paren)
- `געוואָלט  1וואָס שווײַגסטו, מאַטשקאָ?` → `געוואָלט... וואָס שווײַגסטו, מאַטשקאָ?`
  (**"1" artifact**: here the "1" is a dropped ellipsis, not a "?"; scan shows
  three dots)
- Stray footer bleed: line `צייטליו` (running author footer "צייטלין") leaked
  into the text near the page foot — delete.

---

## Summary of error types in this batch (folios 89–96, 8 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| Period outside stage-dir paren (`.)` → `).`) | 12 | Possibly — mechanical rule |
| End punctuation comma→period | 9 | Partially |
| `!` → `?` (rhetorical questions) | 10 | No — context-dependent |
| Extra-yud / triple-yud (דרוייסן, טוייער, אַלייין, אוייסטאַנצן, ס'טיייטשע) | 6 | Yes — mechanical |
| Extra-vav (יאַדווויגאַ) | 1 | Yes |
| Vav-drop (ועט→וועט, וען→ווען, וויל→ווויל, איסגעצויגענע) | 4 | Partially |
| `"1"` artifact (dropped ? or …) | 2 | Partially |
| Word/OCR mangling (קבי→קני, טראָןדיורש→טראָן-יורש, אַנ דע רע→אַנדערע, געטרל→געטרײַ ×2, העלדך→העלדן) | 6 | No — per-word |
| זי → זיי (she/they) | 1 | No — context-dependent |
| Speaker-cue scramble / detach (folios 92, 93, 96) | 3 | No — structural |
| Displaced colon (`האָרכן :`) | 1 | Partially |
| Ellipsis spacing / 2-dot→3-dot | 3 | Partially |
| `אָב → אָפּ` (stage exit misread) | 1 | Yes — recurring |
| Footer bleed (צייטליו) | 1 | Yes — header/footer rule |
| Line-wrap / lineation differences | 6 | No — editorial layout |

**Recurring, mechanical candidates for a deliberate v2 script pass** (still
frozen per project policy — flagged only):
- Extra-yud collapse in the triple-yud family already noted in the 81–88 batch
  now also covers דרוייסן/טוייער/אַלייין/אוייסטאַנצן/ס'טיייטשע — a general
  "collapse 3 identical adjacent yudn / spurious extra yud" rule would catch
  most.
- `.)` → `).` for stage directions is the single most frequent item (12×) and
  is fully mechanical.
- `אָב` as a standalone stage-exit token → `אָפּ` (also seen implicitly in the
  92/93 `— אָפּ` cues).

**Next batch:** resume at folio 97 = PDF page 101 (segment 18).

---

# Esterke — Errata List (Folios 97–104)

Baseline: `esterke_clean_scripted.txt`. Reference: scans of `nybc200294.pdf`
PDF pp. 101–108 (= folios 97–104 = segments 18–25), rasterized at 150 dpi with
Ghostscript. Format: `folio cue — SCRIPT OUTPUT → CORRECTED (note)`. Period
outside stage-direction parens per the edition's rule. Line-wrap-only
differences are noted as formatting, not textual, errors.

*Vowel-point micro-variants (אָ↔אַ in vocatives, stray dagesh) below the
resolution of these scans are not flagged.*

---

### Folio 97 (PDF 101)
- `כ'וואָלט געוו ( — כאַפּט זיך צוריק)` → `כ'וואָלט געוו — (כאַפּט זיך צוריק)`
  (Barkovitsh's word breaks off — dash belongs to the word, paren opens the cue)
- `ניין,..` → `ניין...` (comma+2-dot → ellipsis)
- `(געלעכטער.)` → `(געלעכטער).` (period outside paren)
- `... וויל נישט —  — באָרקאָוויטש:` — speaker cue `באָרקאָוויטש:` was pulled onto
  Kazimir's line; it belongs on its own line (Kazimir's line ends with the dash).
- `... נישט אָפּטרעטן ...נאָר` → `... אָפּטרעטן... נאָר` (ellipsis spacing)
- `אָט ערשט ...איך ווייס` → `אָט ערשט... איך ווייס` (ellipsis spacing)
- `... אין אויג אַרײַן געגלאָצט :` → `... געגלאָצט:` (displaced colon)

### Folio 98 (PDF 102)
- `פון אַ נזירדיקן קלוייסטערמאַן` → `... קלויסטערמאַן` (extra-yud)
- `נישט ווײַבעריייעגער` → `נישט ווײַבער-יעגער` (triple-yud merge → hyphenated
  compound "woman-hunter")
- `און בעטן זײַן פאַרגעבונג,` → `... פאַרגעבונג.` (comma→period)
- Line-wrap: script joined "איך ווייס אַליין נישט. אָדער זי מוז שטאַרק זײַן"
  differently across lines 690–695; scan lineation differs (formatting only).

### Folio 99 (PDF 103)
- `(קאָכאַן אָפּ.)` → `(קאָכאַן אָפּ).` (period outside paren)
- `פון שוואַבןדלענדער` → `פון שוואַבן-לענדער` (**ד-for-hyphen artifact**:
  שוואַבןדלענדער → שוואַבן-לענדער "Swabian-lands")
- `אין ברונעם-וואַסער — באָרקאָוויטש:` — speaker cue `באָרקאָוויטש:` pulled onto
  Spitek's line; belongs on its own line (Spitek's line ends with the dash).
- `און ס'ייאָגט פּוילן נישט אַרויס` → `און ס'יאָגט ...` (extra-yud: ס'ייאָגט → ס'יאָגט)

### Folio 100 (PDF 104)
- `און זיי באַשטעטיקן,` → `... באַשטעטיקן.` (comma→period)
- `(יַדן, מיט לעווקאָן בראָש, קומען אַרײַן.)` → `(ייִדן, ... אַרײַן).` (**יַדן → ייִדן**,
  dropped yud in "Jews"; also period outside paren)
- `(חזרן איבער די ברכה.)` → `(חזרן איבער די ברכה).` (period outside paren)
- Line-wrap: "אויך ייִדן ... דאָס מאָל — זיי ווילן רעדן ..." breaks after the dash
  in the scan (formatting only).

### Folio 101 (PDF 105)
- `פהילין! דאָ נעכטיק` → `פּה-לין! דאָ נעכטיק` (**garbled → פּה-לין**; the *Po-lin*
  "here shalt thou lodge" pun that is the heart of the passage — meaning-bearing.
  Cf. correct `פּה-לין!` at lines 817, 842.)
- `... אויף דײַנע פעלדער,.` → `... פעלדער.` (doubled comma+period → period)
- `(שטילקייט.)` → `(שטילקייט).` (period outside paren)
- `וונדערלעך איז דײַן געשיכטע` → `וווּנדערלעך ...` (vav-drop: וונדערלעך →
  וווּנדערלעך "wondrous")
- `... אַ נעכטן אַ פאַרגיייִקער,` → `... פאַרגייִקער,` (triple-yud: פאַרגיייִקער →
  פאַרגייִקער "bygone")
- `אַן אַשמוֹרה אין דער נאַכט` → `אַן אַשמורה ...` (stray holam point: אַשמוֹרה →
  אַשמורה "a watch of the night")
- Line-wraps (formatting only): scan breaks after "און פון דער מיט", after
  "טויזנט יאָר —", and after "דײַנע ערדן —".

### Folio 102 (PDF 106)
- Speaker `פסּיטעק:` → `ספּיטעק:` (**split-cue artifact**, ס/פ transposed)
- `די ייִדן ... זיי קענען אויסטראַכטן,` → `... אויסטראַכטן.` (comma→period)
- `די קרוין דעם קרייץ זיך קעגנשטעלן,` → `... קעגנשטעלן.` (comma→period)
- `סטאַטוטן אונדז געגעבן, שוץ צו אונדזער האָב,` → `... אונדזער האָב.` (comma→period)
- `באָלעסלאַווס אַלט געשריפטס,` → `... געשריפטס.` (comma→period)
- Line-wrap: stage cue `(דערלאַנגט / קאַזימירן די פּאַרמעטן)` is one line in the
  scan (formatting only).

### Folio 103 (PDF 107)
- `די נײַיגעקומענע צו דיר אין לאַנד — ... דײַנע,` → `די נײַ-געקומענע ...` +
  `... זיי אַלע זענען דײַנע.` (**yud-for-hyphen**: נײַיגעקומענע → נײַ-געקומענע
  "newly-come"; and comma→period, with the scan breaking the line after the dash)
- `ווײַל מען פאַרשטיייט אונדז נישט` → `... פאַרשטייט ...` (triple-yud)
- `איינזאַם איז ישׂראל,` → `... ישׂראל.` (comma→period)
- `געהערן זיי צום קעניג ...גייט מיט גאָט` → `... צום קעניג... גייט` (ellipsis spacing)
- `און זײַט געטרייסט. איך על אײַך געבן שוץ` → `... איך וועל אײַך ...` (vav-drop:
  על → וועל "I will")
- `דעם קעניגס האַרץ ווערט אײַנגעויגט.` → `... אײַנגעוויגט.` (vav-drop: אײַנגעויגט →
  אײַנגעוויגט "lulled")
- Speaker `פסּיטעק:` → `ספּיטעק:` (split-cue, 2nd occ. this batch)
- `און אין זײַן גנאָר וועט ער עס זאַמלען` → `... אין זײַן גנאָד ...` (**גנאָר → גנאָד**,
  ד/ר swap; "in His mercy" — meaning-bearing)
- `פאַר אַ ייִדןדטאָכטער בעט איך` → `... ייִדן-טאָכטער ...` (ד-for-hyphen)

### Folio 104 (PDF 108)
- `אויב זיי וויינען,` → `... וויינען.` (comma→period)
- Speaker `סספּיטעק:` → `ספּיטעק:` (doubled ס)
- `'וויינען אַזוי פאַלשע ייִדןדטעכטער,` → `ס'וויינען אַזוי פאַלשע ייִדן-טעכטער.`
  (dropped ס on ס'וויינען; ד-for-hyphen ייִדןדטעכטער → ייִדן-טעכטער; comma→period)
- Speaker `באָרקאָוויט ש:` → `באָרקאָוויטש:` (letter split inside the name)
- `דאָ רוֹקט זיך אָן ... אַ נײַע כמאַרע,` → `דאָ רוקט ... כמאַרע.` (stray holam רוֹקט →
  רוקט "moves/rolls up"; comma→period)
- `... וועט זי פאַרטרײַבן,` → `... פאַרטרײַבן.` (comma→period)
- Speaker + stage-direction shatter: script produced `אס תּ רק ע:` (letterspaced)
  then the entrance direction broken across lines 938–946 with its final word
  detached. Scan reads the cue **`אסתּרקע:`** and the whole direction on one line:
  **"(קומט אַרײַן וויינענדיק, דאָס פּנים פאַרשטעלט מיט הענט)"**. (This is Esterke's
  first entrance — worth getting clean.)
- `הענט אויפן פּנים ...לײַכטנדיקע הענט..` → `... פּנים... לײַכטנדיקע הענט...`
  (ellipsis spacing; 2-dot → 3-dot)
- `... דײַן געשטאַלט — ועסטו פאַרכּישופן דעם קרול` → `... וועסטו ...` (vav-drop:
  ועסטו → וועסטו "you will")
- `דוֹ קינד פון דעם מכשפים-פאָלק,` → `דו קינד ... מכשפים-פאָלק.` (stray holam דוֹ →
  דו "you"; comma→period)
- `איך וואַרט,` → `איך וואַרט.` (comma→period)

---

## Summary of error types in this batch (folios 97–104, 8 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| Period outside stage-dir paren | 5 | Possibly — mechanical rule |
| End punctuation comma→period | 14 | Partially |
| Split / doubled / letterspaced speaker cue (פסּיטעק×2, סספּיטעק, באָרקאָוויט ש, אס תּ רק ע) | 5 | Partially — cue-anchored |
| **ד-for-hyphen** compound merge (שוואַבןדלענדער, ייִדןדטאָכטער, ייִדןדטעכטער, ווײַבער-יעגער, נײַ-) | 5 | Yes — mechanical, recurring |
| Triple/extra-yud (קלוייסטערמאַן, ס'ייאָגט, פאַרגיייִקער, פאַרשטיייט) | 4 | Yes — mechanical |
| Vav-drop (וונדערלעך, על, אײַנגעויגט, ועסטו) | 4 | Partially |
| Stray holam point (אַשמוֹרה, רוֹקט, דוֹ) | 3 | Possibly |
| Dropped-letter word (יַדן→ייִדן, ס'וויינען) | 2 | Partially |
| Ellipsis spacing / 2-dot→3-dot | 4 | Partially |
| Meaning-bearing word fix (**פהילין→פּה-לין**, **גנאָר→גנאָד**) | 2 | No — per-word |
| Line-wrap / lineation | 7 | No — editorial |

**Note for a possible v2 script pass** (still frozen): the **ד-for-hyphen**
family (a compound's hyphen OCR'd as a stray ד, e.g. `שוואַבןדלענדער`,
`ייִדןדטאָכטער`, and last batch's `טראָןדיורש`) is now frequent and mechanical
enough to be worth a targeted rule. Likewise `אָפּ.)`→`אָפּ).` and the
split-cue `פסּיטעק`→`ספּיטעק`.

**Next batch:** folios 105–112 = PDF pages 109–116 (segments 26–33).

---

# Esterke — Errata List (Folios 105–112)

Baseline: `esterke_clean_scripted.txt`. Reference: scans of `nybc200294.pdf`
PDF pp. 109–116 (= folios 105–112 = segments 26–33), 150 dpi via Ghostscript.
Format: `folio cue — SCRIPT OUTPUT → CORRECTED (note)`. Period outside
stage-direction parens per the edition's rule; line-wrap-only differences noted
as formatting. Sub-resolution vowel-point micro-variants not flagged.

**Act I ends on folio 108** (Netsiel's phantom epilogue); **Act II opens on
folio 109**.

---

### Folio 105 (PDF 109)
- Speaker `א ס תּ ר ק ע :` → `אסתּרקע:` (letterspaced cue)
- `מיך בלויז  -און אַ גאַסטהויז` → `מיך בלויז — און אַ גאַסטהויז` (double-space +
  hyphen → em-dash)
- `בין איך נאָכגעלאָפן,` → `... נאָכגעלאָפן.` (comma→period)
- `נאָר זאָג מיר, טאָכטער :` → `... טאָכטער:` (displaced colon)
- `איז דאָך אַ ייִדןרטאָכטער` → `... ייִדן-טאָכטער` (**ר-for-hyphen** variant of the
  hyphen-merge family: ייִדןרטאָכטער → ייִדן-טאָכטער)
- `דאָס גלויבן פון די אָבות?!05` → `... אָבות?!` (**delete stray "05"** — folio-number
  bleed into the text)
- Stage direction reassembly: script shattered `(ציטערט אויף; נעמט אַרונטער די
  הענט פון פנים)` across lines 970–976; one line in the scan.

### Folio 106 (PDF 110)
- `(שווײַגט.)` → `(שווײַגט).` (period outside paren)
- `ציטערט דעם קעינגס האַרץ` → `... דעם קעניגס האַרץ` (**קעינגס → קעניגס**, metathesis
  in "king's")
- Speaker cue `וויעזשינעק:` was pulled onto Sukhivilk's line (`...וואַרט —  — וויעזשינעק:`);
  belongs on its own line.
- `ס'געשעט —  — -אָ, אומגליק!` → `ס'געשעט — — אָ, אומגליק!` (stray hyphen after dashes)
- `ס'איז אַ כּישוף —  — -` → `ס'איז אַ כּישוף — —` (trailing stray hyphen)
- Speaker `די איבעריקע ייִדן:` was split — `די איבעריקע` pulled onto Rov's line.
- `אֹסתּר הייסט זי` → `אסתּר הייסט זי` (stray holam: אֹסתּר → אסתּר "Esther")
- `זיך אײַנשטעלן פאַר ברידער,` → `... ברידער.` (comma→period)
- `(צו אסתקרען)` → `(צו אסתּרקען)` (**אסתקרען → אסתּרקען**, metathesis + missing
  dagesh, "to Esterke")
- `וואָלסטו אויך אַנטלאָפןן?` → `... אַנטלאָפן?` (doubled final nun)
- `יאָ. כ'האָב פײַנט די שטאַרקע,` → `... שטאַרקע.` (comma→period)

### Folio 107 (PDF 111)
- Speaker cue `לעווקאָ:` pulled onto Rov's continued line (`געלויבט איז גאָט — לעווקאָ:`);
  own line.
- `וואָס זאָגסטו, ספּיטעק? פסּיטעק:` → cue on its own line, and `פסּיטעק:` → `ספּיטעק:`
  (split-cue artifact)
- `זאָל זי שוין איצ ט אַנטלויפן` → `... שוין איצט אַנטלויפן` (letterspaced איצ ט → איצט)
- `... — איצט` / ` -וואָס פריער!` → `... איצט — וואָס פריער!` (stray leading hyphen →
  em-dash; line rejoined)
- `... צום קעפּסווײַב מאַכן, יא — ... אַראָפּדרייען דעם קאָפּ` → `... מאַכן, יאָ — ... דעם
  קאָפּ.` (יא → יאָ; missing final period on קאָפּ)
- `(פּויזע.)` → `(פּויזע).` (period outside paren)
- Speaker `אס תּ רק ע:` → `אסתּרקע:` (letterspaced) ; and `אסת רקע:` → `אסתּרקע:`
  (split + missing dagesh)
- `... די שלעכטע שלעכטס טאָן!` → `... שלעכטס טאָן?` (!→? — it's a question)
- Speaker `קאזימיר:` → `קאַזימיר:` (missing pasekh, name consistency)
- `איינער, וואָס האָט אַל ץ, איז עלנט` → `... האָט אַלץ, ...` (letterspaced אַל ץ → אַלץ)
- `שלעכט זענען די שטאַרקע, נישט די שטאַרקסטע,` → `... שטאַרקסטע.` (comma→period)
- `(וווי פון חלום אַרויס)` → `(ווי פון חלום אַרויס)` (extra-vav: וווי → ווי "as")
- `(מאַכט אַ פּאָר טריט צום קעניג.)` → `... צום קעניג).` (period outside paren)
- Ellipsis-spacing throughout Esterke's trance lines (formatting).

### Folio 108 (PDF 112)
- `מײַן קעניגס חלום ...דאָס באַגערטע ווײַב..` → `... חלום... דאָס באַגערטע ווײַב...`
  (ellipsis spacing; 2-dot → 3-dot)
- `איז דער חלום שלעכט  1ווער קאָן עס וויסן?` → `... שלעכט? ווער קאָן ...` (**"1"
  artifact** = dropped question mark)
- `באָרקאָויטש, נאָך אים די ריטערס` → `באָרקאָוויטש, ...` (vav-drop in name)
- `... שושקען זיך.)` → `... שושקען זיך).` (period outside paren; also `ספיטעק` →
  `ספּיטעק`, missing dagesh)
- `(אַ פאַנטאָם / שאָטנט אַרײַן אין זאַל.)` → `(אַ פאַנטאָם שאָטנט אַרײַן אין זאַל).`
  (rejoin; period outside paren)
- `שפּיץיפינגער,` + `56100840605` → `שפּיץ-פינגער; Ad spectatores` (**two fixes**:
  yud-for-hyphen שפּיץיפינגער → שפּיץ-פינגער "on tiptoe"; and the digit-string
  **`56100840605` is OCR garbage for the Latin stage direction `Ad spectatores`**
  — "to the audience" — the italic Latin was misread as numerals. Meaning-bearing.)
- `(פאַרהאַנג / פאַלט שנעל)` → one line (formatting; end of Act I)

### Folio 109 (PDF 113) — Act II opening
- `... אײַזערנעם צודעק פון אויבן!` → `... פון אויבן.` (stage description; !→.)
- `קומט אָן אַ גנאָסיגעשטאַלט:` → `... אַ גנאָס-געשטאַלט:` (yud-for-hyphen: גנאָסיגעשטאַלט
  → גנאָס-געשטאַלט "a grotesque/comic figure") — recurs at `— צוייטע גנאָסיגעשטאַלט`
  → `— צווייטע גנאָס-געשטאַלט` (also **צוייטע → צווייטע**, vav-drop "second")
- `בײַטשליקנאַקער,` → `בײַטשל-קנאַקער` (yud-for-hyphen "whip-cracker"); the
  Zkndl/Pastekhl insult-lists (lines 1170–1176) are one line each in the scan.

### Folio 110 (PDF 114)
- `וואָס וועט שפּעטער זײַן, דוו הפקרניק?` → `... דו הפקרניק?` (extra-vav: דוו → דו)
- `(ביידע אָפּ.)` → `(ביידע אָפּ).` (period outside paren)
- `זאָל דאָס אַ הונט אַ ביל טאָן! גאָרנישט!` → `... אַ ביל טאָן? גאָרנישט!` (!→? — "should
  a dog bark?")
- Speaker `גאַוואָרעק:` → `גאָוואָרעק:` (name consistency, pasekh→komets)
- Footnote reassembly: `* פּעטאַק (אַקצענט אויף ערשטער זילב) — שוטה.` was split across
  lines 1210–1216; one line in the scan.

### Folio 111 (PDF 115)
- `ווילסט זײַן אַ הייייליקער` → `... אַ הייליקער` (**quadruple-yud** → הייליקער "holy")
- `יל דען גאָט, דו זאָלסט אַ קעניג לעסטערן?` → `וויל דען גאָט, ...` (dropped וו: יל →
  וויל "does God then want")
- `דער קעניג ... האָט אים פרייי לאָזן געזאָלט` → `... פרײַ לאָזן ...` (triple-yud: פרייי
  → פרײַ "free")
- `... וואָס איך מיט דיר — גאַוואָרעק:` → cue on its own line, `גאַוואָרעק:` → `גאָוואָרעק:`
- `מיינסט, אַ ריגליאויף דעם צודעק דאָ —און פאַרטיק!` → `... אַ ריגל אויף דעם צודעק דאָ
  — און פאַרטיק?` (ריגליאויף → ריגל אויף; spacing דאָ —און → דאָ — און; !→?)

### Folio 112 (PDF 116)
- `אַלייין געהערט אין הויף..` → `אַליין געהערט אין הויף...` (triple-yud אַלייין →
  אַליין; 2-dot → 3-dot)
- `אַנדערש היטן מיר אַצינד,` → `... אַצינד.` (comma→period)
- `נישט אַוועקטויטן דעם קעניגס שׂונאים,` → `... שׂונאים.` (comma→period)
- `... אַרונטערלאָזן אים אין גרוב,` → `... אין גרוב.` (comma→period)
- `(לאָזט אַרונטער אויף א שטריק אַ לאָגל;` → `... אויף אַ שטריק ...` (bare א → אַ "a rope")
- `... בלייך, אויפגעשויבערט,` → `... אויפגעשויבערט.` (comma→period, within the
  stage direction)
- `קאַזימיר נידערט.)` → `... נידערט).` (period outside paren)
- `... בלייך, אויפגעשויבערט,` [cue] `נאַכטיק.` [line] → the word **נאַכטיק belongs in
  the stage direction** ("ס'איז דער קעניג — בלייך, אויפגעשויבערט, נאַכטיק" = "the king —
  pale, disheveled, nightlike"). OCR displaced it *down* between the cue `קאַזימיר:` and
  his line `וואָס מאַכט ער?`. Move it back into the direction; Kazimir's line is just
  `וואָס מאַכט ער?`. **RESOLVED at 400 dpi.**
- **Baritshka's-voice scramble** (lines 1296–1297): script gives `דַן געלעגער
  שטרוי? ... איז אויך יי`. Scan reads: **"איז אויך דײַן געלעגער שטרוי? צום
  ייִדן-קעפּסווײַב גיי."** — i.e. `איז אויך` belongs before `דײַן געלעגער`, `דַן` →
  `דײַן`, and the stray `יי` fragment is dropped. Then: "בראָך צו דיר, וואַוועל, בראָך!"

---

## Summary of error types in this batch (folios 105–112, 8 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| Split / letterspaced / mis-vocalized speaker cue | 9 | Partially |
| Hyphen-merge family (ד/ר/י-for-hyphen: ייִדןר-, גנאָסי-, בײַטשלי-, שפּיצי-, ריגלי-) | 6 | Yes — mechanical, recurring |
| End punctuation comma→period | 8 | Partially |
| `!` → `?` | 4 | No — context-dependent |
| Extra/multi-yud & extra-vav (הייייליקער, אַלייין, פרייי, וווי, דוו) | 5 | Yes — mechanical |
| Dropped-letter word (יל→וויל, א→אַ, אַנטלאָפןן) | 3 | Partially |
| Metathesis / mangled word (קעינגס→קעניגס, אסתקרען→אסתּרקען) | 2 | No — per-word |
| Stray holam / stray hyphen / stray "05" | 4 | Possibly |
| Period outside stage-dir paren | 6 | Possibly — mechanical |
| **Latin recovered** (`56100840605` → `Ad spectatores`) | 1 | No — needs eyes |
| **Text scramble** (Baritshka's voice, folio 112) | 1 | No — structural |
| Fragmented stage direction / footnote reassembly | 4 | No — structural |

**Next batch:** folios 113–120 = PDF pages 117–124 (segments 34–41).

---

# Esterke — Errata List (Folios 113–120)

Baseline: `esterke_clean_scripted.txt`. Reference: scans of `nybc200294.pdf`
PDF pp. 117–124 (= folios 113–120 = segments 34–41), 150 dpi via Ghostscript.
Format: `folio cue — SCRIPT OUTPUT → CORRECTED (note)`.

**Note on stage-direction parens:** the original is *inconsistent* — some close
`.)` (period inside), most close `).` (period outside). Each entry below reflects
what the scan actually shows; unflagged parens match the scan already.

---

### Folio 113 (PDF 117)
- `(ווערט אַנטשויגן.)` → `(ווערט אַנטשוויגן).` (vav-drop אַנטשויגן → אַנטשוויגן "falls
  silent"; period outside)
- `און אונטן דאָ —אַ קללה.` → `... דאָ — אַ קללה.` (dash spacing)
- `אַ הימל פול מיט ליבשאַפט — און אַ גרוב,` → `... אַ גרוב.` (comma→period)
- `ווײַזט זיך אויבן אויף די טרעפ.)` → `... די טרעפּ).` (period outside; טרעפ→טרעפּ)
- `איך גיי ...זײַ רויַק, קינד.` → `איך גיי... זײַ רויִק, קינד.` (ellipsis spacing;
  **רויַק → רויִק**, wrong vowel — khirik, "calm")
- `... פאַר דײַנע גבורות,` → `... גבורות.` (comma→period)
- `זאָלסטו נישט זײַן קיין שטאַרקער,` → `... שטאַרקער.` (comma→period)
- `(ביידע אָפּ.)` → `(ביידע אָפּ).` (period outside)
- `... דער ייִדנמויד, א רעשט,` → `... אַ רעשט.` (bare א → אַ; comma→period)
- `... ער האָט זי ליב — 113` → `... זי ליב —` (**delete stray "113"**, folio-number bleed)

### Folio 114 (PDF 118)
- `... קיינער נישט געחייסן זיך פאַרליבן` → `... געהייסן זיך פאַרליבן.` (**געחייסן →
  געהייסן**, ח for ה; add final period)
- `... די ברכה פון געקריייציקטן` → `... געקרייציקטן` (triple-yud "crucified" — the
  recurring קריייציקט artifact)
- `... איז דאָך אויך געווען א ייֵד` → `... אַ ייִד` (bare א → אַ; **ייֵד → ייִד**, tsere→khirik "Jew")
- `... איז ער געוואָרן אונדזער איינער,.` → `... אונדזער איינער.` (comma+period → period)
- `... אויגן אונדזעריקע, פּולישע,` → `... פּוילישע,` (**פּולישע → פּוילישע**, dropped yud "Polish")
- `אוֹן דער אסתּרקעס אַ זון` → `און דער ...` (stray holam אוֹן → און "and")
- `אַ ..אַזוי מיינסטו?` → `אַ... אַזוי מיינסטו?` (space+2-dot → ellipsis)
- `(ווערן אַנטשוויגן.)` → `(ווערן אַנטשוויגן).` (period outside)

### Folio 115 (PDF 119)
- `וואָלט כאָטש די קאָכמויד איצט געקומען, ז וואָנ קא.` → `... זוואָנקאַ.` (letterspaced/broken
  ז וואָנ קא → זוואָנקאַ "Zvonka")
- `ווייסט? ... פון קאָך. / ער היט זי אָפּ ... / ד` → `... פון קאָך. דער היט זי אָפּ ...`
  (script split **דער** into a stray `ד` on its own line + `ער`; rejoin to דער)
- `(שטיל.)` → `(שטיל).` (period outside)
- `(עס ווײַזט זיך אַ טונקעלע פרויען-פיגור אין אַ טוך.)` → `... אין אַ טוך).` (period outside)
- `ווער? זוואָנקאַ?!15` → `ווער? זוואָנקאַ?!` (**delete stray "15"**, folio-number bleed)

### Folio 116 (PDF 120)
- Speaker `וואָנקאַ:` → `זוואָנקאַ:` (dropped ז)
- `... דאָס קול דײַנס  זאָל זיך` → `... דײַנס; זאָל זיך` (double-space → semicolon)
- `צווישן מיר און דעם גאַָוואָרעק.` → `... דעם גאָוואָרעק.` (stray double vowel-point
  גאַָ → גאָ)
- `דער נאַסער האָן! די לאַנגע נאָז?` → `... האָן? די לאַנגע נאָז?` (!→?, mocking-question list)
- `האָ'ימיר אַלעבאַרדן, קעצעלע.` → `האָ'מיר אַלעבאַרדן ...` (extra-yud האָ'ימיר → האָ'מיר
  "we have")
- `און זען צי ס'קאָכט,` → `... ס'קאָכט.` (comma→period)
- `(אויבן ווײַזט זיך דער קאָך.)` → `... דער קאָך).` (period outside)

### Folio 117 (PDF 121)
- `וואָס וונדערסטו זיך?` → `וואָס וווּנדערסטו זיך?` (vav-drop וונדערסטו → וווּנדערסטו)
- `... הינער"פּרעגלער, ...` → `... הינער-פּרעגלער, ...` (**quote-mark-for-hyphen**:
  הינער"פּרעגלער → הינער-פּרעגלער "chicken-fryer" — new variant of the hyphen-merge family)
- `... בין איך געקומען.` → `... בין איך געקומען` (remove period — the sentence runs on
  into "נישט מיט בלויזע הענט…")
- Stage direction reassembly: `(טוליעט / זיך דערשראָקן / צו קאָכאַנען / און גאָוואָרעקן)`
  is one line in the scan.

### Folio 118 (PDF 122)
- `צום קאָך)` → `(צום קאָך)` (missing opening paren)
- Speaker cue `זוואָנקאַ:` was pulled onto the cook's line (`... ווער ווייס ווי אַלט —
  זוואָנקאַ:`); own line.
- `מיר אויך אַ ביסל, ווענץ,` → `... ווענץ.` (comma→period)
- `איך זע ...יאָ, יאָ ...איך זע שוין דווקא אַלץ..` → `איך זע... יאָ, יאָ... איך זע שוין דווקא
  אַלץ...` (ellipsis spacing; 2-dot → 3-dot)
- `מע טרינקט,` → `מע טרינקט.` (comma→period)
- `מיר טרינקען,` → `מיר טרינקען.` (comma→period)
- `נו, און דו, גאָוואָרעק?!18` → `נו, און דו, גאָוואָרעק?` (**delete stray "18"**; ?! → ?)

### Folio 119 (PDF 123)
- `שיין לײַט ביסטו, גאָוואָרעק,` → `... גאָוואָרעק.` (comma→period)
- `די זוואַנקאַ האָט דאָך אים` → `די זוואָנקאַ ...` (name consistency זוואַנקאַ → זוואָנקאַ)
- `אויך מי ך אַפילו — הם — אַפילו מיך -` → `אויך מיך אַפילו — הם — אַפילו מיך —`
  (letterspaced מי ך → מיך; trailing hyphen → em-dash)
- `מיר היטן, קאָכאַן. ניין 1מיר האַלטן קאָפּ,` → `... ניין? מיר האַלטן קאָפּ.` (**"1"
  artifact** = dropped question mark; comma→period)

### Folio 120 (PDF 124)
- `און דוֹ?` → `און דו?` (stray holam דוֹ → דו)
- `(געלעכטער.)` → `(געלעכטער).` (period outside)
- `אָדיאָךיאָך. ברודערל קאָך.` → `אַ-דיאָך-יאָך, ברודערל קאָך.` (merged nonsense-refrain
  restored with hyphens; period→comma)
- `(שיכורע געלעכטערם.)` → `(שיכּורע געלעכטערס).` (**געלעכטערם → געלעכטערס**, final ם→ס
  "laughters"; period outside; שיכורע→שיכּורע dagesh)
- `(צו די דרי)` → `(צו די דרײַ)` (**דרי → דרײַ** "three", dropped pasekh-yud)

---

## Summary of error types in this batch (folios 113–120, 8 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| End punctuation comma→period | 11 | Partially |
| Period outside stage-dir paren (where scan shows it) | 8 | Case-by-case |
| Vowel-point error (רויַק→רויִק, ייֵד→ייִד, stray holam ×2, dagesh) | 5 | No — needs eyes |
| Hyphen-merge family (הינער"-, letterspaced/broken names) | 2 | Partially |
| Extra/dropped yud & vav (וונדערסטו, האָ'ימיר, דרי, פּולישע, געקריייציקטן) | 5 | Yes — mechanical |
| `"1"` artifact (dropped ?) | 1 | Partially |
| `!` → `?` | 1 | No |
| Dropped-letter word (וואָנקאַ→זוואָנקאַ, א→אַ, געחייסן→געהייסן) | 3 | Partially |
| Name consistency (זוואַנקאַ→זוואָנקאַ, גאַָ→גאָ) | 2 | Partially |
| Stray punctuation (double-space→semicolon; hyphen→dash; comma+period) | 3 | Partially |
| Final-form letter (געלעכטערם→געלעכטערס) | 1 | Yes |
| **Folio-number bleed into text** (113, 15, 18) | 3 | Yes — mechanical |
| Fragmented stage direction / split-cue | 4 | No — structural |

**Next batch:** folios 121–128 = PDF pages 125–132 (segments 42–49).

---

# Esterke — Errata List (Folios 121–128)

Baseline: `esterke_clean_scripted.txt`. Reference: scans of `nybc200294.pdf`
PDF pp. 125–132 (= folios 121–128 = segments 42–49), 150 dpi via Ghostscript.
Format: `folio cue — SCRIPT OUTPUT → CORRECTED (note)`. Paren-period reflects
the scan case-by-case; line-wrap-only differences noted as formatting.

---

### Folio 121 (PDF 125)
- `וואָס?שוין ווידער טרינקען?` → `וואָס? שוין ווידער טרינקען?` (missing space after ?)
- `... בעסער שלאָפן —  — (בייגט שווער דעם קאָפּ.)` → `... (בייגט שווער דעם קאָפּ).`
  (period outside)
- `(די דרײַ שלאָפן אײַן, איינס געלענט אָן אַנדערן.)` → `... אָן אַנדערן).` (period outside)
- `זעט דער וואיעוואָדע?` → `... דער וואָיעוואָדע?` (**וואיעוואָדע → וואָיעוואָדע** "voivode")
- `... אַ לייטער.)` → `... אַ לייטער).` (period outside)

### Folio 122 (PDF 126)
- `אַ שוואַרצן סוף פאַר אַזאַ היטן,` → `... אַזאַ היטן.` (comma→period)
- `און די גרוב — אַ פּוסטע ...נאָך א מאָל פאַרראַט נישט` → `... אַ פּוסטע... נאָך אַ מאָל ...`
  (ellipsis spacing; bare א → אַ)

### Folio 123 (PDF 127)
- `דו מוזסט זיך לאָזן טויטן,` → `... טויטן.` (comma→period)
- `עס ציטערט מיר די האַנט,` → `... די האַנט.` (comma→period)
- `(שטעכט דעם קאָך.)` → `(שטעכט דעם קאָך).` (period outside)
- `זוואָנקאַ.-.` → `זוואָנקאַ...` (the cook dies on her name; period-hyphen-period →
  ellipsis)
- Speaker `באָר קאָוויטש:` → `באָרקאָוויטש:` (name split)
- Speaker `באָרקאָוויטש:` pulled onto Baritshka's-voice line (`... איך דערקען די שטים —
  באָרקאָוויטש:`); own line. (Also `באַריטשקאס קול` → `באַריטשקאַס קול`, missing pasekh.)

### Folio 124 (PDF 128)
- `אין אַלע אייביקייטן,` → `... אייביקייטן.` (comma→period)
- Speaker scramble: script split the joint cue over three lines —
  `באָרקאָוויטש` / `(פרום)` / `אַמען,` / `און די ריטערס:`. Scan reads the single cue
  **`באָרקאָוויטש און די ריטערס:`** then `(פרום)` / `אַמען.` (and comma→period on אַמען).
- `פאַר וואָס אין זאַק!` → `... אין זאַק?` (!→?)
- `שוין פאַרצויגן?!24` → `שוין פאַרצויגן?` (**delete stray "24"**; ?! → ?)

### Folio 125 (PDF 129)
- `דערוואָרגן, אַ?און ווער איז שולדיק?` → `... אַ? און ווער ...` (missing space after ?)
- `... זײַן ייִדןרטאָכטער,` → `... ייִדן-טאָכטער,` (ר-for-hyphen)
- `ווען נישט ע ר איז קרול ... אַ קריסט א הייליקן` → `... נישט ער איז ... אַ קריסט אַ
  הייליקן` (letterspaced ע ר → ער; bare א → אַ)
- `... זיי זענען שולדיק! זיי! גאַנץ פּווילן וועט עס ויסן!` → `... גאַנץ פּוילן וועט עס
  וויסן!` (**פּווילן → פּוילן** extra-vav "Poland"; **ויסן → וויסן** vav-drop "know")
- `די ייִדןדטאָכטער. פּוילן וועט עס וויסן.` → `די ייִדן-טאָכטער. ...` (ד-for-hyphen)
- `... ווּ סליגט דער קאָך-יונג,` → `... ווּ ס'ליגט דער קאָך-יונג.` (missing apostrophe
  סליגט → ס'ליגט; comma→period)
- `כ'וויל זען,` → `כ'וויל זען.` (comma→period)
- `(הויקערט זיך איבער דעם לייידיקן זאַק` → `... דעם ליידיקן זאַק` (triple-yud לייידיקן →
  ליידיקן "empty")
- `... די קרוין פון פּוילן. ווייסט :` → `... ווייסט:` (displaced colon)
- `איר אַלע וועט בײַ מיר אין גאָלד אַרומגיין,` → `... אַרומגיין.` (comma→period)
- `... גרויס-פּוילנס וואָיעוואָדע,` → `... וואָיעוואָדע.` (comma→period)

### Folio 126 (PDF 130)
- `... וואָס זאָגסטו, לעך  1ביסט דאָך אַ קלוגער,` → `... לעך? ביסט דאָך אַ קלוגער.`
  (**"1" artifact** = dropped question mark; comma→period)
- `אויך ע ר אַ מענטש — דער קאָך?` → `אויך ער אַ מענטש ...` (letterspaced ע ר → ער)
- `האָט דען וייניק בלוט פאַרגאָסן? קרוין איז בלוט,` → `... דען ווייניק בלוט ... קרוין איז
  בלוט.` (vav-drop וייניק → ווייניק "little"; comma→period)
- `שיצן זאָל אונדז דער געקריייציקטער.` → `... דער געקרייציקטער.` (triple-yud "crucified")

### Folio 127 (PDF 131)
- `(שלעפט דעם קאָכס קערפּער, קרעכצט.)` → `(שלעפּט ... קרעכצט).` (period outside;
  שלעפט→שלעפּט)
- `אַזוי, דו קאָך ...דו קעניגלעכער קאָך..` → `... דו קאָך... דו קעניגלעכער קאָך...`
  (ellipsis spacing; 2-dot → 3-dot)
- `... זײַ זשע מוֹחל,` → `... זײַ זשע מוֹחל.` (comma→period)
- `(איבערן זאַק, ווּ ס'יליגט דער קערפּער ...)` → `... ווּ ס'ליגט ...` (extra-yud ס'יליגט → ס'ליגט)
- Stage-direction interleave: script folded Barkovitsh's line **"דו, פאַרטאָג! אויך נאָך
  אַזאַ נאַכט קומסטו?"** *into* the parenthetical `(פּויזע; קוקט צום אויפגעגרויטן מיזרח,
  צלמט זיך אין געצנדינערישער שרעק)`. Scan has the direction whole, then the spoken
  line. (Also **אזַאַ → אַזאַ**, misplaced pasekh.)
- `... אויב יאָ —איז ער ...` → `... אויב יאָ — איז ער ...` (dash spacing)
- `(שטיל זיך שאַרנדיק, אָפּ מיט די זײַניקע.)` → `... די זײַניקע).` (period outside)
- `... שלאָפן. אָפּנעסמטע הינט ליגן` → `... אָפּגעסמטע הינט ליגן` (**אָפּנעסמטע → אָפּגעסמטע**,
  metathesis, "the poisoned dogs" — **CONFIRMED at 400 dpi**)
- `... דער שלעכטער חלום).)` → `... חלום).` (doubled closing paren)
- `דאָס מיידל פון אָפּאָטשנע..` → `... אָפּאָטשנע...` (2-dot → 3-dot)
- `מיט קיצלדיקע נאַרישקיייטן עס פאַרוויגט ...קאַטאָוועסיטשערעדעס` → `... נאַרישקייטן עס
  פאַרוויגט... קאַטאָוועס-טשערעדעס` (triple-yud נאַרישקיייטן → נאַרישקייטן; yud-for-hyphen
  קאַטאָוועסיטשערעדעס → קאַטאָוועס-טשערעדעס "jest-herds")

### Folio 128 (PDF 132)
- `... אין סאַמע האַרצן אסתּרקען אַרײַנגעפײַפט,` → `... אַרײַנגעפײַפט.` (comma→period)
- `... איך בין יונג — און כ'ישטעל דיר אויס אַ צונג.` → `... כ'שטעל דיר ...` (extra-yud
  כ'ישטעל → כ'שטעל "I stick out")
- `(יאָגט אַוועק דעם זקנדל, ... שטייט איף` → `... שטייט אויף` (vav-drop איף → אויף "up")
- `פון באַגינעטוי / נאַס, טאַנצט אַוועק אין קשאַקעס אַרײַן.)` → `פון באַגינען-טוי נאַס ...
  אַרײַן).` (**באַגינעטוי → באַגינען-טוי** "dawn-dew", merged compound + dropped nun;
  period outside)
- `דער באַפעל דעם בוראס,` → `... דעם בוראס.` (comma→period)

---

## Summary of error types in this batch (folios 121–128, 8 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| End punctuation comma→period | 15 | Partially |
| Period outside stage-dir paren (per scan) | 7 | Case-by-case |
| Hyphen-merge family (ד/ר/י-for-hyphen; באַגינען-, קאַטאָוועס-, ייִדן- ×2) | 5 | Yes — recurring |
| Extra/dropped yud & vav (פּווילן, ויסן, וייניק, לייידיקן, נאַרישקיייטן, ס'יליגט, כ'ישטעל, איף) | 8 | Yes — mechanical |
| Letterspaced fragment (ע ר ×2) | 2 | Partially |
| `"1"` artifact (dropped ?) | 1 | Partially |
| `!` → `?` / missing space after ? | 3 | Partially |
| Metathesis / scramble (אָפּנעסמטע→אָפּגעסמטע, וואיעוואָדע→וואָיעוואָדע) | 2 | No — per-word |
| Ellipsis spacing / 2-dot→3-dot (incl. זוואָנקאַ.-.→…) | 5 | Partially |
| **Speaker-cue scramble** (folio 124 "באָרקאָוויטש און די ריטערס") | 1 | No — structural |
| **Stage-direction interleave** (folio 127, spoken line folded into paren) | 1 | No — structural |
| Split cue / name split (באָר קאָוויטש) | 3 | No — structural |
| Folio-number bleed (24) | 1 | Yes |
| Doubled paren `).)` | 1 | Yes |

**Next batch:** folios 129–136 = PDF pages 133–140 (segments 50–57).

---

# Esterke — Errata List (Folios 129–136)

Baseline: `esterke_clean_scripted.txt`. Reference: scans of `nybc200294.pdf`
PDF pp. 133–140 (= folios 129–136 = segments 50–57), 150 dpi via Ghostscript.
Format: `folio cue — SCRIPT OUTPUT → CORRECTED (note)`.

**Act II ends on folio 129** (Netsiel's song, curtain); **Act III opens on
folio 129** (Esterke's castle at Łobzów). This act has many long stage
directions that the OCR shattered into letterspaced fragments — reassembly is
noted structurally rather than token-by-token.

---

### Folio 129 (PDF 133)
- `כ'ווייס נישט, נאָר כ'פאַרטרוי אים,` → `... כ'פאַרטרוי אים.` (comma→period)
- Act heading `דריטער אקט` → `דריטער אַקט` (missing pasekh)
- `... אַז דאָס האָט ע ר` → `... האָט ער` (letterspaced ע ר → ער)
- stray `1209` (line 2019) → **delete** (garbled folio-number bleed for "129")

### Folio 130 (PDF 134)
- `און אסתּרקען אַלייין` → `... אַליין` (triple-yud)
- `... אַפּילו דאָ ס` → `... אַפּילו דאָס` (split דאָ ס → דאָס) — twice (lines 2037, 2041)
- `... זיך באַהאַלטןן?` → `... זיך באַהאַלטן?` (doubled final nun)
- Speaker `אסת רקע:` → `אסתּרקע:` (split + missing dagesh)
- `כ'האָב דאָך ליב נאָר אים אַלין,` → `... נאָר אים אַליין,` (dropped yud אַלין → אַליין)
- `... מלך איבער פּוילן?!30` → `... איבער פּוילן?` (**delete "30"**; ?! → ?)

### Folio 131 (PDF 135)
- `... נאָך גאָר אַ קינד —  —  — -איך, לעווקאָ,` → `... — — — איך, לעווקאָ,` (stray hyphen
  before איך)
- `ס'וועט די צווייטע אֹסתּר` → `... אסתּר` (stray holam)
- `דערצו אַ נישטיגעשמדטע.` → `... אַ נישט-געשמדטע.` (yud-for-hyphen "not-baptized")
- `אַז צוישן דיר, אסְתּר בת-ירוחם,` → `אַז צווישן דיר, אסתּר בת-ירוחם,` (vav-drop צוישן →
  צווישן; stray shva אסְתּר → אסתּר)
- Speaker cue `אסתּרקע:` pulled onto Levko's line (`... אַ ממזר בלויז —  — אסתּרקע:`);
  own line.
- `דו רופסט מײַן פּעלקאָן / ממ זר?` → `... פּעלקאָן ממזר?` (split ממ זר → ממזר "bastard")
- `עס איז אין פאָלק אַרײַן א מורא` → `... אַ מורא` (bare א → אַ)
- `... אַ ייִד פאַר אַ הערשער ;` → `... אַ הערשער;` (displaced semicolon)
- `אַפּילן יאַן סוכיווילק` → `אַפּילו יאַן ...` (**אַפּילן → אַפּילו**, nun for vav "even")
- `... דעם ייִדנשטאַם — 111` → `... דעם ייִדנשטאַם —` (**delete "111"**, folio bleed for "131")

### Folio 132 (PDF 136)
- `זי מיינען, אַז מיר, ...` → `זיי מיינען, ...` (**זי → זיי**, "they" — meaning-bearing)
- `... צו מערדערן באַצײַטגס אונדז` → `... באַצײַטנס אונדז.` (**באַצײַטגס → באַצײַטנס**, ג for
  נ, "betimes"; add period)
- `וואָס פאַרשטיייסטו פון דעם אַלעמען?` → `וואָס פאַרשטייסטו ...` (triple-yud)
- `און איך ער בין?` → `און איך ווער בין?` (**ער → ווער**, "and who am I?" — meaning-bearing)
- `(עס ווײַזט זיך אַ ייד ...)` → `(... אַ ייִד ...)` (missing khirik); and speaker `דער /
  ייִד מיטן זקעל:` → `דער ייִד מיטן זעקל:` (**זקעל → זעקל**, metathesis "little sack")
- `קרייצן מיך גוייַם` → `... גוייִם` (pasekh→khirik "goyim")
- `ויל איך מיט אַ זעקל` → `וויל איך ...` (vav-drop ויל → וויל)
- `מײַן קינד האָט דעם גוייַשן מלך` → `... דעם גוייִשן מלך` (pasekh→khirik "gentile")

### Folio 133 (PDF 137)
- Long entrance direction (Kazimir emerging from the cave) shattered across lines
  2137–2153; scan has it whole. Also `קאַזימיר,)` → `קאַזימיר.)` (comma→period inside)
- `(צו אסתּרקען, וואָס קוקט איף אים ...)` → `... קוקט אויף אים ...` (vav-drop איף → אויף)
- `ס'רופן נישט דייאַגדיהערנער..` → `ס'רופן נישט די יאַגד-הערנער...` (mega-merge →
  "the hunt-horns"; 2-dot → 3-dot)
- `דו רופסט — איך גי..` → `... איך גיי...` (dropped yud; 2-dot → 3-dot)
- `... די בלוטשפּיל פון די שטאַרקע,` → `... פון די שטאַרקע.` (comma→period)
- `... פאַרשמעקט מיט דײַנע האַר.` → `... מיט דײַנע האָר.` (**האַר → האָר**, "hair" not
  "lord" — meaning-bearing)

### Folio 134 (PDF 138)
- `נישט רעד פון יאַגד, נישט רעד פון וואַלד,` → `... פון וואַלד.` (comma→period)
- Scramble: `גמוזט. / כ'האָב ע` → `כ'האָב געמוזט.` (script split/reversed "I had to")
- `אַרײַן דערווײַל אין שלאָס(. אַלע דרײַ — אָפּ.)` → `... אין שלאָס. (אַלע דרײַ — אָפּ).`
  (paren/period displacement)
- **Stage-direction shatter (major):** two directions — the riders' gallop / the
  small crowned figure approaching (Łokietek's ghost) — were fragmented into
  letterspaced lines 2220–2238 and 2243–2255 and *interleaved with Łokietek's
  spoken line*. Scan reads the first direction whole, then the line. (Łokietek's
  line **CONFIRMED at 400 dpi as `פּוילן, שאַל אויף — איך בין געקומען` — no change**;
  the earlier `שאַל אַרויף` guess was wrong.)

### Folio 135 (PDF 139)
- Scramble: `יןךא, לאָקיעטעק, / דאָס בי` → `דאָס בין איך, לאָקיעטעק.` (RTL-shattered
  "This is I, Łokietek.")
- `(רײַטער גאַלאָפּ דערהערט זיך פון דאָס (ײַ)` → `(רײַטער-גאַלאָפּ דערהערט זיך פון דאָס נײַ)`
  (missing hyphen; **`דאָס (ײַ)` → `דאָס נײַ`** "anew", OCR scrambled)
- `(אָפ.)` → `(אָפּ.)` (missing dagesh)
- **Stage-direction shatter (major):** the two-hosts direction (Barkovitsh vs.
  Chancellor Sukhivilk's party) fragmented across lines 2274–2305; scan has it as
  flowing prose.
- `... פאַר א ים זי אוייסבאַהאַלטן` → `... פאַר אים זי אויסבאַהאַלטן` (split א ים → אים;
  extra-yud אוייסבאַהאַלטן → אויסבאַהאַלטן)
- `וואָס איז דער קעניג שולדיק  1און אויך זי — 135` → `... שולדיק? און אויך זי —`
  (**"1" artifact** = dropped ?; **delete "135"**)

### Folio 136 (PDF 140)
- `נעמט דעם כּישוף פון אים צוֹ —` → `... פון אים צו —` (stray holam צוֹ → צו)
- `און קאַזימירס. רוֹיִק און באַדאַכט` → `... רויִק און באַדאַכט` (stray holam רוֹיִק → רויִק)
- `פון איר גרויסן הערשער,` → `... הערשער.` (comma→period)
- `גרויס — מיט וואָס! איז דען נישט ער` → `גרויס — מיט וואָס? ...` (!→?)
- `שולדיק אינעם טויט פון גוֹטן דינער` → `... פון גוטן דינער` (stray holam גוֹטן → גוטן)
- `דעם היייליקן באַריטשקאַ  1און דײַן הערשערס קעפּסווײַב` → `דעם הייליקן באַריטשקאַ? און
  ...` (**quadruple-yud** היייליקן → הייליקן; **"1" artifact** = dropped ?)
- `אוֹן האָט זי דען נישט אָנגערעדט` → `און האָט זי ...` (stray holam אוֹן → און)
- `פאַר באַריטשקאַס היייליק בלוט` → `... הייליק בלוט` (quadruple-yud)

---

## Summary of error types in this batch (folios 129–136, 8 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| **Stray-holam cluster** (צוֹ, רוֹיִק, גוֹטן, אוֹן, אֹסתּר) | 5 | Possibly — recurring on f.136 |
| pasekh↔khirik vowel error (גוייַם, גוייַשן, אסְתּר) | 3 | No — needs eyes |
| End punctuation comma→period | 7 | Partially |
| `"1"` artifact (dropped ?) | 3 | Partially |
| `!`→`?` | 2 | No |
| Multi-yud (triple/quadruple: היייליקן ×2, פאַרשטיייסטו, אַלייין) | 4 | Yes — mechanical |
| Vav-drop / dropped-letter (ויל, איף, צוישן, אַלין, אַפּילן, גיי) | 6 | Partially |
| Hyphen-merge family (נישט-, די יאַגד-, רײַטער-) | 3 | Yes — recurring |
| **Meaning-bearing word fixes** (זי→זיי, איך ער→איך ווער, האַר→האָר, באַצײַטגס→באַצײַטנס) | 4 | No — per-word |
| Split token (דאָ ס→דאָס ×2, ממ זר→ממזר, א ים→אים, ע ר→ער) | 5 | Partially |
| **Text/stage-direction scramble** (Kazimir entrance, Łokietek's line, two-hosts dir., כ'האָב געמוזט, דאָס בין איך) | 5 | No — structural |
| Doubled nun / paren-period displacement | 2 | Partially |
| Folio-number bleed (1209, 30, 111, 135) | 4 | Yes |

**Next batch:** folios 137–144 = PDF pages 141–148 (segments 58–65).

---

# Esterke — Errata List (Folios 137–144)

Baseline: `esterke_clean_scripted.txt`. Reference: scans of `nybc200294.pdf`
PDF pp. 141–148 (= folios 137–144 = segments 58–65), 150 dpi via Ghostscript.
Format: `folio cue — SCRIPT OUTPUT → CORRECTED (note)`. This is the battle /
tribunal sequence; several long stage directions were shattered and interleaved
with dialogue (noted structurally).

---

### Folio 137 (PDF 141)
- `פאַר באַריטשקאַס היייליק בלוט!` → `... הייליק בלוט!` (quadruple-yud)
- `(אַנדערע פון זײַנע לײַט וואַקלען זיך, קערן שוטיל` → `... קערן זיך שטיל` (scramble:
  שוטיל → זיך שטיל)
- `אין סוכיווילקס זײַט.)` → `... זײַט).` (period outside)
- `ווי קאַזימיר דאָרט אין ווישליץ!1` → `... אין ווישליץ?!` (**"1" artifact** = the
  question mark; order restored)
- `איך וואָלט — 137` → `איך וואָלט —` (**delete "137"**, folio bleed)

### Folio 138 (PDF 142)
- `... ווייסטו וואָס? אַ קאָפּ` → `... אַ קאָפּ.` (add final period)
- **Stage-direction shatter (major):** the "swords drawn / passages blocked"
  direction (`(באָרקאָוויטשעס ריטערס ציִען די שווערדן ... פאַרשטעלן די דורכגענג.)`) was
  fragmented across lines 2430–2457 with Sukhivilk's line `איבער מײַן קערפּער!
  אָפּטרעטן! צוריק!` interleaved into it. Scan: direction whole, then the line.

### Folio 139 (PDF 143)
- `... הייבן אָן זיך צוריקציען.)` → `... צוריקציִען).` (khirik; period outside)
- `מיר וועלן זי אַרוסרופן` → `... אַרויסרופן` (dropped yud "call out")
- `מיט ערפּאָרכט וועלן מיר` → `מיט ערפּורכט ...` (**ערפּאָרכט → ערפּורכט**, "reverence")
- Speaker `באַרקאָוויטש:` → `באָרקאָוויטש:` (name consistency, pasekh→komets)
- `דאָס ביסט דו, באָרקאָוויטש!` → `... באָרקאָוויטש?` (!→?)
- Speaker cue `באָרקאָוויטש:` pulled onto Levko's line; own line.
- `וווילשטאַנד פונעם לאַנד — 139` → `... פונעם לאַנד —` (**delete "139"**)

### Folio 140 (PDF 144)
- Speaker `באַרקאָוויטשעס לײַט:` → `באָרקאָוויטשעס לײַט:` (name consistency; also
  de-split across lines 2505/2507 and 2512/2514)
- Speaker `באָרקאָוויט ש:` → `באָרקאָוויטש:` (name split)
- `וער פאַר מאַטשקאָן — שנײַד!` → `ווער פאַר מאַטשקאָן ...` (dropped vav וער → ווער)
- `פאַָרן קעניג!` → `פאַרן קעניג!` (stray double vowel-point פאַָ → פאַ)
- `(שווערדן געראַנגל. ...)` → `(שווערדן-געראַנגל. ...)` (missing hyphen)
- `(לויפט צו צו באָרקאָויטשן, ...)` → `... באָרקאָוויטשן ...` (dropped vav in name)
- Speaker cues `וויעזשינעק:` and `ספּיטעק:` each pulled onto the prior line;
  own lines.

### Folio 141 (PDF 145)
- `(די קעניגיגעטרײַע בינדן אים.)` → `(די קעניג-געטרײַע ...)` (yud-for-hyphen
  "king-loyal")
- Speaker `באָרקאָוויט ש:` → `באָרקאָוויטש:` (name split)
- `וועמען בינדט איר?! מיך!?` → `וועמען בינדט איר? מיך?` (scan shows single ? each)
- `(אַ טייל לויפן.)` → `(אַ טייל לויפן).` (period outside)
- `איצט, וואיעוואָדע, הערש!` → `... וואָיעוואָדע ...` (וואיעוואָדע → וואָיעוואָדע)
- `אַנטלופן? קאָנען מיר דען איבערלאָזן גוֹססע?` → `אַנטלויפן? ... גוססע?` (dropped yud
  אַנטלופן → אַנטלויפן; stray holam גוֹססע → גוססע "corpses")

### Folio 142 (PDF 146)
- Speaker cue `קאַזימיר:` pulled onto Sukhivilk's line (`... אָבער — קאַזימיר:`); own line.
- `כ'הער,` → `כ'הער.` (comma→period)
- `פאַר דײַן האַרץיגעליבטערס שלאָס, מײַן קעניג,` → `... האַרץ-געליבטערס שלאָס, מײַן קעניג.`
  (yud-for-hyphen "heart's-beloved"; comma→period)
- `(שווײַגט.)` → `(שווײַגט).` (period outside)

### Folio 143 (PDF 147)
- `(שטילקייט.)` → `(שטילקייט).` (period outside)
- `עס רעדט נישט אַזוי איינער / -ס'רעדט אַ שטאַם.` → `... איינער — ס'רעדט אַ שטאַם.`
  (stray leading hyphen → em-dash; rejoined)
- Speaker `אַן אַלטער / ריטער:` → `אַן אַלטער ריטער:` (de-split)
- Speaker `באָרקאָוויט ש:` → `באָרקאָוויטש:` (name split)
- (Ellipsis-spacing throughout Lekh's dying lines — formatting.)

### Folio 144 (PDF 148)
- `קום אום — און שווליג — לעך:` → `קום אום — און שווײַג —` + cue `לעך:` on own line
  (**שווליג → שווײַג** "be silent"; speaker split)
- `זײַט וויסן..` / `מאַטשקאָ..` / `יענער נאַכט..` → `... זײַט וויסן...` etc. (2-dot → 3-dot,
  several)
- `... דער ייִדישקע אַרופגעלייגט,..` → `... אַרויפגעלייגט...` (dropped yud אַרופגעלייגט →
  אַרויפגעלייגט; `,..` → `...`) — אַרופגעלייגט → אַרויפגעלייגט recurs at line 2677
- `(שטאַרבט.)` → `(שטאַרבט).` (period outside)
- Speaker cues `סוכיווילק:` and `ספּיטעק:` pulled onto prior lines; own lines
  (and `פסּיטעק:` → `ספּיטעק:`, split-cue)
- `... אין פּוילנס נאָמען :` → `... נאָמען:` (displaced colon)
- `פאַרטיליקט מוזן ווערן אַלע מאַטשקאָס,` → `... אַלע מאַטשקאָס.` (comma→period)
- `... און וואָס שווײַגט עסטעראַ?!44` → `... עסטעראַ?` (**delete "44"**; ?! → ?)

---

## Summary of error types in this batch (folios 137–144, 8 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| Name split/consistency (באָרקאָוויט ש, באַרקאָוויטשעס, פסּיטעק) | 6 | Partially |
| Period outside stage-dir paren | 6 | Case-by-case |
| End punctuation comma→period / add period | 4 | Partially |
| `"1"` artifact / `?!`→`?` / `!`→`?` | 5 | Partially |
| Hyphen-merge family (קעניג-, האַרץ-, שווערדן-) | 3 | Yes — recurring |
| Dropped yud/vav (אַרוסרופן, וער, אַנטלופן, אַרופגעלייגט ×2, באָרקאָויטשן) | 6 | Partially |
| Scramble (שוטיל→זיך שטיל, שווליג→שווײַג) | 2 | No — per-word |
| Vowel/stray-point (ערפּאָרכט→ערפּורכט, פאַָרן, גוֹססע, quad-yud היייליק) | 4 | No — needs eyes |
| 2-dot → 3-dot ellipsis | 4 | Partially |
| Displaced colon | 1 | Partially |
| **Stage-direction shatter** (folio 138, major) | 1 | No — structural |
| Speaker-cue pulled onto prior line | 6 | No — structural |
| Folio-number bleed (137, 139, 44) | 3 | Yes |

**Next batch (final):** folios 145–150 = PDF pages 149–154 (segments 66–71).

---

# Esterke — Errata List (Folios 145–150, final)

Baseline: `esterke_clean_scripted.txt`. Reference: scans of `nybc200294.pdf`
PDF pp. 149–154 (= folios 145–150 = segments 66–71), 150 dpi via Ghostscript.
Format: `folio cue — SCRIPT OUTPUT → CORRECTED (note)`.

**This is the end of the play** — Act III close (folio 145) and the EPILOGUE
(folios 146–150), a dream-vision on the ruins of the inn in which later Jewish
figures (Peretz, Mickiewicz, the Eternal Jew Netsiel) appear. The epilogue's
long stage directions and the Mickiewicz footnote were badly fragmented by the
OCR.

---

### Folio 145 (PDF 149)
- `איידער מײַע קושן ווערן קושן,` → `איידער מײַנע קושן ...` (dropped nun מײַע → מײַנע)
- `און איך אַלייין =` → `און איך אַליין —` (triple-yud אַלייין → אַליין; `=` → em-dash)
- `וואָס וועט זײַן מיט מיר! איך ווייס נישט.` → `... מיט מיר? ...` (!→?)
- `(ביידע אָפּ. טיפע שטילקייט.)` → `... טיפע שטילקייט).` (period outside)

### Folio 146 (PDF 150) — Epilogue opening
- **Stage-direction shatter:** the epilogue setting was fragmented across lines
  2736–2753. Scan reads: **"אויף די חורבות פון ירוחמס גאַסטהויז אין אָפּאָטשנע.
  סודותדיקע שטיל-אויסגעשטערנטע נאַכט."** (Also **שטיליאויסגעשטערנטע →
  שטיל-אויסגעשטערנטע**, yud-for-hyphen "star-strewn".)
- `... וואָס זענען איינס :` → `... איינס:` (displaced colon)
- `ס'קראַכן באַלקנס, טירן, ווענט,..` → `... ווענט...` (comma+2-dot → ellipsis)
- `ווערט דער ייד פאַרברענט` → `... דער ייִד פאַרברענט` (missing khirik ייד → ייִד)
- `גייט ער, גייט ער, גייט ער..` → `... גייט ער...` (2-dot → 3-dot)
- Speaker `אסת רקע:` → `אסתּרקע:` (split + dagesh)

### Folio 147 (PDF 151)
- `שבת-יליכט צו צינדן — לעווקאָ:` → `שבת-ליכט צו צינדן —` + cue `לעווקאָ:` on own
  line (extra-yud שבת-יליכט → שבת-ליכט "Sabbath-candles")
- Stage direction `(צום משוגענעם, ... אויף אַ שאָטן)` fragmented across 2788–2795;
  Levko's spoken line `ווער איז יענער?` was split (its `ווער איז` pulled into the
  direction). Reassemble.
- `פון דעם נישטאַָינאָך, ... שפּעטער..` → `פון דעם נישטאָ-נאָך, ... שפּעטער...` (stray
  double-point + yud-for-hyphen נישטאַָינאָך → נישטאָ-נאָך "the not-yet"; 2-dot→3-dot)
- `עפּעס רעדט ער..` → `... ער...` (2-dot → 3-dot)
- Scramble: `דַן נאַכט און מײַנע / פּוילן, יי` → `פּוילן, דײַן נאַכט און מײַנע` (Peretz:
  "Poland, your night and mine"; **דַן → דײַן**, fragment `יי` rejoined)
- `פּויילנס נאַכט,` → `פּוילנס נאַכט,` (extra-yud)
- `כ'מוז גיין —  — -מוז גיין —  —` → `כ'מוז גיין — — מוז גיין — —` (stray hyphen after
  dashes); the following direction goes on its own line.
- Speaker `מיצקעוויטש.:` → `מיצקעוויטש:` (stray period before colon)
- `מײַן טאַטע — פון אדוֹם,` → `... פון אדום,` (stray holam אדוֹם → אדום "Edom")

### Folio 148 (PDF 152)
- `פיר-דאון-פערציק הייס איך* ,` → `פיר-און-פערציק הייס איך.*` (**פיר-דאון- →
  פיר-און-** "four-and-forty", stray ד; comma→period; footnote marker reseated)
- `דם — און ס'פעלט דער אַלף,` → `... דער אַלף.` (comma→period)
- `וער דו ביסט — דאָס ווייס איך,` → `ווער דו ביסט ...` (dropped vav וער → ווער)
- `דאָך ווער איך בין ווייסטו נישט..` → `... נישט...` (2-dot → 3-dot)
- `סיאָגט פּוילנס נאַכט אויך מיך,` → `ס'יאָגט פּוילנס נאַכט ...` (missing apostrophe
  סיאָגט → ס'יאָגט "it chases")
- Speaker scramble: `דער / זעקל: / ייד מיטן` → `דער ייִד מיטן זעקל:` (RTL-shattered "the
  Jew with the sack"; ייד → ייִד)
- **Footnote shatter:** the Mickiewicz footnote (2867–2887), a quotation from the
  *Great Improvisation* on the mysterious "forty-four", was fragmented and
  interleaved. Scan: `* "פון אַ פרעמדער מאַמען, אַלט גיבוריש-בלוט זײַן בלוט, און דער
  נאָמען זײַנער — פיר און פערציק" (די גרויסע אימפּראָוויזאַציע).` (Also **delete "148"**,
  folio bleed.)

### Folio 149 (PDF 153)
- `גי איך, גיי איך, אַלע גייימיר — אסתּרקע, קום מיט!` → `גיי איך, גיי איך, אַלע גיי'מיר
  ...` (dropped yud גי → גיי; **גייימיר → גיי'מיר** "let's all go", merged apostrophe) —
  גייימיר → גיי'מיר recurs at line 2901
- `דײַנע אויגן די קלוגע — -` → `... די קלוגע —` (trailing stray hyphen)
- `פון ייִדישע שׂרפוֹת — טרייף איז זי` → `... שׂרפות ...` (stray holam שׂרפוֹת → שׂרפות
  "burnings")

### Folio 150 (PDF 154) — final page
- `זינג מיר אַ ליד..` → `זינג מיר אַ ליד...` (2-dot → 3-dot)
- `אַזוי דער גזרידין,` → `אַזוי דער גזר-דין,` (yud-for-hyphen גזרידין → גזר-דין "the
  decree")
- `קיין ירושלים וועט מען גיין,` → `... וועט מען גיין.` (comma→period, final line of
  the song)
- `איבערגעאַרבעטע ווערסיע — .7691` → `... ווערסיע — 1967.` (**RTL digit reversal**:
  the colophon "reworked version" is dated **1967**, OCR'd as "7691"; period reseated)

---

## Summary of error types in this batch (folios 145–150, 6 pages)
| Type | Count | Script-fixable? |
|---|---|---|
| Hyphen-merge family (שטיל-, נישטאָ-, גזר-, פיר-און-, שבת-ליכט) | 5 | Yes — recurring |
| Dropped yud/vav/nun (מײַע, וער, גי, פּויילנס, אַלייין) | 5 | Partially |
| Missing apostrophe (סיאָגט→ס'יאָגט, גייימיר→גיי'מיר ×2) | 3 | Partially |
| Stray holam / stray point (אדוֹם, שׂרפוֹת, נישטאַָ, ייד→ייִד) | 4 | No — needs eyes |
| End punctuation comma→period | 4 | Partially |
| 2-dot → 3-dot ellipsis | 5 | Partially |
| `!`→`?` / stray-hyphen-for-dash / `=`→dash | 4 | Partially |
| **RTL digit reversal** (colophon 7691 → 1967) | 1 | No — needs eyes |
| **Text/stage-direction/footnote scramble** (epilogue setting; Peretz line; "Jew with the sack" cue; Mickiewicz footnote) | 4 | No — structural |
| Speaker split / stray period on cue | 3 | No — structural |
| Folio-number bleed (148) | 1 | Yes |

---

## Errata pass complete
Folios **81–150** (the whole play, Acts I–III + Epilogue) are now covered:
`esterke_errata.md` (81–88) and `esterke_errata_folios_89-96` … `_145-150.md`.
A companion paraphrase runs alongside in `esterke_dialogue_summary.md`.

---

