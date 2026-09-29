# መጽሐፈ ግጻዌ — Ethiopian Orthodox Tewahedo Lectionary

A machine-readable transcription and structured dataset of **መጽሐፈ ግጻዌ ወመዝሙር ከነምልክቱ** (Aksum Press, Addis Ababa), appointing scripture readings for every day of the Ethiopian Orthodox Tewahedo liturgical year.

**366 days across 13 months, plus 166 sections of movable feasts, Sunday hymns, funeral readings and a ባሕረ ሐሳብ computus table — the complete book, 427 pages.**

## What is in here

| File / Folder | Contents | Description |
|---|---|---|
| `months/01-meskerem.json` … `13-paguemen.json` | 13 files, one per month | **366 days** of readings |
| `daily-gitsawe.json` | Single compiled daily file | All 366 days keyed by `dd-mm` |
| `gitsawe-master.json` | The whole lectionary book | All five liturgical parts |
| `gitsawe-structure.json` | Liturgical skeleton | Parts, chapters, page ranges |
| `parts/` | The four non-month parts | 166 liturgical sections |
| `source-pages/` | Page scan audit trails | 377 scanned reference records |

Each day carries its commemoration and liturgical services — `negh` (matins / ዘነግህ), `kidassie` (Divine Liturgy / ዘቅዳሴ), and `serk` (vespers / ዘሠርክ) — each with its `msbak` (psalm chants), `gospel` / `wengel`, and for the Liturgy, Pauline epistle (`pauline`), Catholic epistle (`catholic`), Acts (`acts`), and appointed anaphora (`anaphora`).

## Data Structure & Developer Experience

### 1. Unified Date Format (`dd-mm`)
Dates are keyed using `dd-mm` (e.g. `01-01` for 1st Meskerem to `06-13` for 6th Paguemen), matching the Sinq lectionary standard.

### 2. English Key Naming
Services and readings use standardized English key names (`negh`, `kidassie`, `serk`, `msbak`, `gospel`, `pauline`, `catholic`, `acts`, `anaphora`), with full backward-compatibility aliases (`wengel`, `firstDeacon`, `secondDeacon`, `secondKahn`).

### 3. Multiple Misbaks & Multilingual Support
To accommodate days with multiple misbaks (including *ዓዲ* occurrences) and enable contributors to add multiple translations, `msbak` is structured as an array with localized text maps:

```json
"msbak": [
  {
    "text": {
      "geez": "እስመ ትቤ ለዓለም አሐንጽ ምሕረተ።\nበሰማይ ጸንዐ ጽድቅከ።\nኪዳነ ተካየድኩ ምስለ ኅሩያንየ።",
      "amharic": "...",
      "english": "..."
    },
    "verse": {
      "bookTitle": "መዝሙረ ዳዊት",
      "chapter": 88,
      "citation": "፹፰ ቍ ፪ – ፫",
      "start": 2,
      "end": 3
    },
    "voice": "https://..."
  }
]
```

### 4. Canonical Septuagint (LXX) Psalm Numbering
All Psalm citations follow the **canonical Septuagint (LXX) numbering (1–151)** as in the Ethiopic Psalter (*መዝሙረ ዳዊት*). Consumers targeting Masoretic numbering can easily map chapters according to the standard LXX-MT offset table:

```
LXX 1–8     = MT 1–8         LXX 113     = MT 114+115
LXX 9       = MT 9+10        LXX 114/115 = MT 116 (split)
LXX 10–112  = MT 11–113      LXX 116–145 = MT 117–146
                             LXX 146/147 = MT 147 (split)
                             LXX 148–150 = MT 148–150
                             LXX 151     — not in MT
```

## Validation & Verification

Run the validation suite anytime with:

```bash
python3 validate.py
```

## Licence and contributions

The underlying text is a liturgical work of the Ethiopian Orthodox Tewahedo Church.
This repository is the machine-readable transcription and its accompanying open developer tooling.
