# መጽሐፈ ግጻዌ — Ethiopian Orthodox Tewahedo Lectionary

A machine-readable transcription of **መጽሐፈ ግጻዌ ወመዝሙር ከነምልክቱ** (Aksum Press, Addis
Ababa), the lectionary appointing the scripture readings for every day of the
Ethiopian Orthodox Tewahedo liturgical year.

**366 days across 13 months, plus 166 sections of movable feasts, Sunday hymns,
funeral readings and a ባሕረ ሐሳብ computus table — the complete book, 427 pages.**

## What is in here

| | | |
|---|---|---|
| `months/01-meskerem.json` … `13-paguemen.json` | 13 files, one per month | **366 days** |
| `gitsawe-master.json` | the whole book in one file | all five parts |
| `gitsawe-structure.json` | skeleton only: parts, chapters, page ranges | no readings |
| `parts/` | the four non-month parts | 166 sections |
| `source-pages/` | one file per scanned page — the audit trail | 377 files |

Each day carries its **commemoration** and up to three services — ዘነግህ (matins),
ዘቅዳሴ (the Divine Liturgy), ዘሠርክ (vespers) — and each service its ምስባክ (psalm
verses), ወንጌል (gospel) and, for the Liturgy, the epistle and Acts readings.

## ⚠ Psalm numbering — read this first

**ምስባክ psalm numbers follow the Septuagint**, as the Ethiopic psalter does.
Most English Bibles use the Masoretic numbering, and the two differ by one across
most of the psalter.

> `መዝ· ፻፲፰` in this book is **Psalm 119** in an English Bible.

Every ምስባክ carries two **derived** fields we added — they are not printed on the page:

```json
"ምስባክ": {
  "book": "መዝ·",
  "chapter_verse": "፻፲፰ ቍ· ፹፮ – ፹፯",   ← as printed (Septuagint)
  "psalm_lxx": 118,                      ← derived
  "psalm_masoretic": "119",              ← derived
  "verses": ["በዐመፃ ሰደዱኒ ርድአኒ ።", …]
}
```

### Psalm 118 and its 22 stanzas

Ps 118 (LXX) = 119 (MT) is the great acrostic — 176 verses in **22 stanzas of 8**, one
per Hebrew letter. The Ethiopic tradition keeps the stanza names, and this book cites
them by name: the funeral rubric on printed p. 416 reads
*"የመጀመሪያ ምዕራፍ **አሌፍ** ....... **ቤት** ....... **ጋሜል** ....... በል"*.

It is by far the most-cited psalm here — **43 citations**, spread across every month.
Each carries a derived `ps118_stanza`:

```json
"chapter_verse": "፻፲፰ ቍ· ፻፴፯ – ፻፴፰",
"ps118_stanza": [{ "number": 18, "name": "ጻዴ", "latin": "Tsade", "verses": [137, 144] }]
```

The acrostic sometimes survives into Ge'ez — stanza **ጻዴ** opens *ጻድቅ አንተ እግዚአ*.
A citation straddling two stanzas lists both. `ps118_stanza(v)` and
`ps118_stanzas_for_range(lo, hi)` are importable from `psalms.py`.

The full LXX↔MT mapping is in [`psalms.py`](psalms.py); `lxx_to_mt(n)` is importable.

```
LXX 1–8     = MT 1–8         LXX 113     = MT 114+115
LXX 9       = MT 9+10        LXX 114/115 = MT 116 (split)
LXX 10–112  = MT 11–113      LXX 116–145 = MT 117–146
                             LXX 146/147 = MT 147 (split)
                             LXX 148–150 = MT 148–150
                             LXX 151     — not in MT
```

**Verse** numbers also run 1–2 lower than modern editions in places. A small
discrepancy against a modern Bible is usually this edition's own convention.

## Transcription policy

**Everything is as printed.** Nothing was normalised or corrected. Malformed
citations, missing `ቍ·`, descending verse ranges and duplicated marks are all in
the book, and they are preserved so the data can be checked against the source.

**The incipit is the reliable key.** It is always legible and identifies a reading
unambiguously. The Ge'ez numerals are the fragile part: at scan resolution
**፰ / ፳ / ፷** share one glyph form, as do **፴ / ፵** and **፮ / ፯**.

`check_citations.py` lists every citation that is impossible as printed (a verse
beyond its chapter's length). There are 32, out of roughly 3,600.

## Provenance

Transcribed from 427 page scans (CamScanner, ~190 ppi, **no text layer** — every
page was read visually). `printed_page = scan_page − 3`; the table of contents is
bound at the front but numbered 422–426.

Each day records `source_scan_pages`. 107 `review_notes` mark uncertain readings
and printing oddities. Reproduce the QA with:

```bash
python3 validate.py          # structure, coverage, month endpoint anchors
python3 check_citations.py   # citations impossible as printed
```

## Known issues

See **[KNOWN_ISSUES.md](KNOWN_ISSUES.md)** — 32 impossible citations, one incomplete
day, 107 uncertain readings, and three structural findings that look like errors but
are properties of the book. All disclosed, all traceable to a printed page.

## Licence and contributions

The underlying text is a liturgical work of the Ethiopian Orthodox Tewahedo Church.
This repository is the transcription and its tooling.

Corrections are welcome — especially from anyone holding a physical copy. The most
useful contributions are the items in `review_notes` and the citations flagged by
`check_citations.py`. **Please cite the printed page** (`printed_page`, not the scan
number) when reporting a correction.
