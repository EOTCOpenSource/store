# Field reference

Every file opens with `_meta` (the caveats in brief) and `book` (title, publisher,
provenance). Below that, month files carry `days[]`; part files carry `sections[]`
or, for Part 5, a single `table`.

## A day

```json
{
  "day_number": "፲፩",                       // Ge'ez numeral, ፩–፴
  "commemoration": "አባ ያዕቆብ ወቅድስት ዲላግየ…",   // the red heading; absent if the heading
                                            //   is on the previous page
  "source_scan_pages": [51, 52],            // which scans this day was read from
  "services": { "ዘነግህ": {…}, "ዘቅዳሴ": {…}, "ዘሠርክ": {…} }
}
```

`services` may hold fewer than three. **Absence was recorded, not invented** — a day
genuinely without vespers is stored without ዘሠርክ.

## A service

| key | meaning |
|---|---|
| `ምስባክ` | the psalm verses chanted before the gospel |
| `ምስባክ_ዓዲ` | a second ምስባክ, introduced in the book by **ዓዲ** ("again") |
| `ወንጌል` | the gospel reading |
| `ወንጌል_ዓዲ` | a second gospel in a ዓዲ block |
| `epistles_and_acts` | array — Pauline epistle, catholic epistle, Acts |
| `ቅዳሴ` | the anaphora appointed (a **name**, not a reading). Omitted where the book prints the label with no name beside it. |

## A reading

```json
"ወንጌል": { "book": "ሉቃስ", "chapter_verse": "ም· ፰ ቍ· ፲፱ – ፳፯", "incipit": "ወአንዘ ይመስል ሎሙ ።" }
```

```json
"ምስባክ": { "book": "መዝ·", "chapter_verse": "፻፲፰ ቍ· ፹፮ – ፹፯",
           "psalm_lxx": 118, "psalm_masoretic": "119",     // ← DERIVED, not printed
           "verses": ["በዐመፃ ሰደዱኒ ርድአኒ ።", "…"] }
```

For **Ps 118** (the 176-verse acrostic) a further derived key gives the stanza:

```json
"ps118_stanza": [{ "number": 11, "name": "ካፍ", "latin": "Kaph", "verses": [81, 88] }]
```

`epistles_and_acts` entries add `reading_type` (`ቆሮ ፪`, `ያዕቆብ`, `ግብ፡ ሐዋ፡` …).

**`book` may be absent** on a handful of readings where the page prints a citation
with no book name. That is the print, not a gap.

### Citation format

`ም·` = ምዕራፍ, chapter · `ቍ·` = ቍጥር, verse · `ፍ፡ም፡` = to the end of the chapter.

**ምስባክ citations put the psalm number first, before `ቍ·`** — `፻፲፰ ቍ· ፹፮ – ፹፯` is
Ps 118:86–87. Every other reading puts the chapter after `ም·`.

## Parts 2–5

Parts 2 and 4 use `sections[]` keyed by `section_title`; Part 3 uses `period`
(a date range) plus `hymn` (the መዝሙር incipit) and `readings`. Part 5 is one
`table` with `columns` and `rows`.

Part 3's `chapters` carry `boundary_source` and `boundary_confidence`: **no `ክፍል`
heading is printed anywhere in the body** — the 11 chapters are a table-of-contents
scheme, and the ranges are derived from red divider lines, hymn-ordinal resets and
running-head changes. Each says which.

## Provenance and quality fields

| key | meaning |
|---|---|
| `source_scan_pages` | which scan(s) a record came from |
| `scan_pages` / `printed_pages` | `printed_page = scan_page − 3` |
| `review_notes` | uncertain readings and printing oddities, per page or per day |
| `status`, `days_extracted` | completeness bookkeeping |

`days_extracted` counts day *numbers* present. A day can be present but thin —
missing a service because its page was not reached. `validate.py` reports those
separately; there is exactly one in the corpus (ኅዳር ፳፰).
