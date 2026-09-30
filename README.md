# EOTC Open Source Store

Open-access, standardized, machine-readable liturgical and prayer datasets of the **Ethiopian Orthodox Tewahedo Church (EOTC)**.

This repository serves as a canonical open data store for mobile developers, web apps, researchers, and content creators building modern software for the Church.

---

## Repository Structure

```
.
├── lectionary/
│   └── gitsawe/                      # መጽሐፈ ግጻዌ — The Annual Liturgical Lectionary
│       ├── months/                   # 13 month files (01-meskerem.json … 13-paguemen.json)
│       │                             # (366 days of appointed scripture readings)
│       ├── parts/                    # Non-month liturgical sections
│       │   ├── 02-movable-feasts.json # Great Fast, Pascha, and Movable Feasts (49 sections)
│       │   ├── 03-sunday-hymns.json   # Seasonal Sunday hymn sections (91 sections)
│       │   ├── 04-atnatewos.json      # Funeral & departure readings (25 sections)
│       │   └── 05-bahre-hasab.json    # Computus reference table (ባሕረ ሐሳብ)
│       ├── daily-gitsawe.json        # Compiled bundle of all 366 days keyed by dd-mm
│       ├── gitsawe-master.json       # Complete unified book (all 5 parts)
│       ├── gitsawe-structure.json    # Liturgical skeleton & page index
│       ├── validate.py               # Dataset validation test suite
│       ├── SCHEMA.md                 # Lectionary JSON schema specification
│       └── README.md                 # Lectionary dataset documentation
│
└── prayers/
    └── wudasie-maryam/               # ውዳሴ ማርያም — Praises of St. Mary (Weekly Cycle)
        ├── geez/                     # Ge'ez text (01-monday.json … 07-sunday.json)
        ├── am/                       # Amharic text (01-monday.json … 07-sunday.json)
        ├── en/                       # English text (01-monday.json … 07-sunday.json)
        ├── index.json                # Language & day catalog
        └── wudasie maryam.md         # Prayer checklist & notes
```

---

## Core Datasets

### 1. መጽሐፈ ግጻዌ (Lectionary)
Appoints the scripture readings, psalm verses (ምስባክ), and anaphora (ቅዳሴ) for every day of the Ethiopian liturgical calendar:
- **366 Days** across 13 months.
- **166 Liturgical Sections** in movable feasts, seasonal Sunday hymns, and funerary lections.
- **Services Covered**: Matins (`negh`), Divine Liturgy (`kidassie`), and Vespers (`serk`).
- **Liturgical Readings**: Misbak chants (`msbak`), Gospels (`gospel`), Pauline epistles (`pauline`), Catholic epistles (`catholic`), Acts (`acts`), and Anaphoras (`anaphora`).

### 2. ውዳሴ ማርያም (Wudasie Maryam)
Daily praises of the Virgin Mary organized by day of the week (Monday through Sunday) with multilingual translations in **Ge'ez**, **Amharic**, and **English**.

---

## Design Principles & Data Standards

1. **Unified Date Convention (`dd-mm`)**:
   - Dates are formatted as a single zero-padded string `dd-mm` (e.g. `01-01` for 1st Meskerem to `06-13` for 6th Paguemen), matching the calendar convention used in apps like Sinq.
2. **Canonical Septuagint (LXX) Psalter**:
   - Psalm citations follow canonical Septuagint (1–151) numbering as printed in the Ethiopic Psalter (*መዝሙረ ዳዊት*).
3. **Array-Based Multi-Chant Support**:
   - Readings that may occur multiple times within a single service (such as multiple misbaks or *ዓዲ* chants) are modeled as structured arrays.
4. **Multilingual Architecture**:
   - Text fields are structured under language keys (`text: { "geez": "...", "amharic": "...", "english": "..." }`) to allow community contributors to add translations without changing schema.
5. **Canonical Ethiopic Punctuation**:
   - Ge'ez texts use standard Ethiopic punctuation marks: word-separator colons (**`፡`**), sentence full stops (**`።`**), clause semicolons (**`፤`**), and preface colons (**`፦`**).

---

## Developer Quick Start

### Validating the Lectionary Dataset

To verify structural integrity and scripture citation validity:

```bash
python3 lectionary/gitsawe/validate.py
```

### Loading Daily Readings (JavaScript / TypeScript)

```typescript
import dailyGitsawe from './lectionary/gitsawe/daily-gitsawe.json';

// Query readings for Meskerem 1 (01-01)
const today = '01-01';
const readings = dailyGitsawe[today];

console.log('Commemoration:', readings.title);
console.log('Liturgy Psalm Verse:', readings.kidassie.msbak[0].text.geez);
console.log('Liturgy Gospel:', readings.kidassie.gospel[0].verse);
```

### Loading Daily Readings (Python)

```python
import json

with open("lectionary/gitsawe/daily-gitsawe.json", encoding="utf-8") as f:
    daily = json.load(f)

# Get today's liturgical readings (e.g. 1st Meskerem)
day = daily.get("01-01")
print(f"Title: {day['title']}")
print(f"Liturgy Misbak: {day['kidassie']['msbak'][0]['verse']}")
```

---

## Contributing

Contributions, text corrections, and additional translations (e.g., Afaan Oromoo, Tigrinya) are welcome!

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/my-feature`).
3. Verify all validation suites pass (`python3 lectionary/gitsawe/validate.py`).
4. Submit a Pull Request.

---

## License

The underlying liturgical texts belong to the living heritage and tradition of the Ethiopian Orthodox Tewahedo Church.
The machine-readable transcriptions, JSON schemas, and accompanying tooling are open source under the MIT License.
