# Gitsawe Lectionary JSON Schema & Developer Reference

This document outlines the JSON structure and schema for the Ethiopian Orthodox Tewahedo Church (EOTC) Lectionary (*መጽሐፈ ግጻዌ*).

The dataset covers all **366 days** of the liturgical calendar (13 months) plus the non-month liturgical parts (movable feasts, Sunday hymns, funeral rites, and computus).

---

## 1. File Structure Overview

- **`months/01-meskerem.json` … `13-paguemen.json`**: Individual month lectionary files.
- **`daily-gitsawe.json`**: Flat bundle containing all 366 daily lectionary records keyed by `dd-mm`.
- **`gitsawe-master.json`**: The complete lectionary including all 5 liturgical parts in a unified document.
- **`parts/`**:
  - `02-movable-feasts.json`: The Great Fast, Pascha, and Movable Feasts.
  - `03-sunday-hymns.json`: 11 seasonal Sunday hymn sections.
  - `04-atnatewos.json`: Funeral, memorial, and departure services.
  - `05-bahre-hasab.json`: Computus reference matrix (19-year Awde Abektie cycle).

---

## 2. Daily Lectionary Record Structure

Each day entry uses consistent English keys and date format:

```json
{
  "date": "01-01",
  "title": "ኢዮብ ራጉኤል ሚልኪ በርተሎሜዎስ ።",
  "negh": { ... },
  "kidassie": { ... },
  "serk": { ... }
}
```

### Date Format
- **Format**: `dd-mm` (zero-padded 2-digit day and 2-digit month).
- Matches the Sinq lectionary date keying convention:
  - `01-01` to `30-01` (Meskerem)
  - ...
  - `01-13` to `06-13` (Paguemen)

### Services
Each day contains up to three liturgical services:
- **`negh`**: Matins (*ዘነግህ*)
- **`kidassie`**: Divine Liturgy (*ዘቅዳሴ*)
- **`serk`**: Vespers (*ዘሠርክ*)

---

## 3. Service Structure & Readings

Each service contains scripture readings organized with English key names and array values:

| Key | Description | Liturgical Role |
|---|---|---|
| `msbak` | Array of Misbak psalm chants | Pre-gospel chant (supports multiple chants / *ዓዲ*) |
| `gospel` (or `wengel`) | Array of Gospel readings | Holy Gospel |
| `pauline` (or `firstDeacon`) | Array of Pauline Epistle readings | 1st Epistle (Liturgy only) |
| `catholic` (or `secondDeacon`) | Array of General/Catholic Epistle readings | 2nd Epistle (Liturgy only) |
| `acts` (or `secondKahn`) | Array of Acts of the Apostles readings | Book of Acts (Liturgy only) |
| `anaphora` (or `kidassie`) | Anaphora name string | Liturgical Anaphora appointed |

---

## 4. Misbak & Translation Structure

To support multiple misbaks (including *ዓዲ* occurrences) and multilingual translations, `msbak` is structured as an array of items:

```json
"msbak": [
  {
    "text": {
      "geez": "ወትባርክ አክሊለ ዓመተ ምሕረትከ ።\nወይጸግቡ ጠላተ ገዳም ።\nወይረውዩ አድባረ በድው ::",
      "amharic": "...",
      "english": "..."
    },
    "verse": {
      "bookTitle": "መዝሙረ ዳዊት",
      "chapter": 64,
      "citation": "፷፬ ቍ ፲፩ – ፲፪",
      "start": 11,
      "end": 12
    },
    "voice": "https://..."
  }
]
```

### Psalm Numbering (Septuagint / LXX)
All Psalm chapters strictly follow the **canonical Septuagint (LXX) numbering (1–151)** as used in the Ethiopian Orthodox Tewahedo Church Psalter (*መዝሙረ ዳዊት*).
- Users targeting Masoretic-based translations (e.g. standard Western Protestant Bibles) can convert chapter numbers using standard LXX-to-MT mapping offset tables.

---

## 5. Clean Metadata & No Local Paths

- All developer files omit machine-specific local filesystem paths (`/home/...`).
- Extraneous repeated publisher / scan metadata has been removed from individual daily records to ensure lightweight payloads for frontend and mobile apps.
