# Known issues

Everything below is **disclosed, not hidden**. Each item is traceable to a printed
page, and none of it is silently corrected in the data.

If you hold a physical copy, these are the highest-value things to check.
Please cite the **printed page** (`printed_page`, not the scan number).

---

## 1. Citations that are impossible as printed

A verse number beyond its chapter's length, or a range that descends. Some are the
book's own misprints; some are glyph misreads we could not settle. **32 of ~3,600**
citations (0.9%). The `incipit` on each is reliable and identifies the true reading.

Regenerate with `python3 check_citations.py`.

```
=== impossible citations: 32

  scan 55 day ፲፮   ዘነግህ/ወንጌል
      ም· ፲፪ ቍ· ፶፬ – ፍ፡ም፡   →  verse 54 > ማቴዎስ 12 has 50
      incipit: ወእምከመ ወጽአ መንፈስ ።
  scan 57 day ፲፰   ዘቅዳሴ/ግብ፡ ሐዋ፡
      ም· ፰ ቍ· ፶፬ – ፍ፡ም፡   →  verse 54 > ግብ 8 has 40
      incipit: ወይእዜኒ ትግሁ ወተዘከሩ ።
  scan 60 day ፳፩   ዘቅዳሴ/ወንጌል
      ም· ፲፭ ቍ· ፶፫ – ፶፭   →  verse 55 > ዮሐንስ 15 has 27
      incipit: ወካዕበ ተከዘ በልቡ ።
  scan 65 day ፳፮   ዘቅዳሴ/ዮሐ፡ ፩
      ም· ፪ ቍ· ፳፰ – ፲   →  range descends 28–10
      incipit: ወይእዜኒ ደቂቅየ ንበሩ ባቲ ።
  scan 68 day ፳፱   ዘቅዳሴ/ወንጌል
      ም· ፰ ቍ· ፴፬ – ም ፱ ቍ· ፩ – ፪   →  range descends 34–2
      incipit: ወጸውዖሙ ለሕዝብ ምስለ አርዳኢሁ ።
  scan 75 day ፮    ዘሠርክ/ወንጌል
      ም· ፪ ቍ· ፳፪ – ፳፬   →  verse 24 > ማቴዎስ 2 has 23
      incipit: ወሰሚዖ ከመ አርኬላአስ ነግሠ ።
  scan 88 day ፳    ዘሠርክ/ወንጌል
      ም· ፳፩ ቍ· ፵፬ – ፵፯   →  verse 47 > ማቴዎስ 21 has 46
      incipit: ወዘሰ ወድቀ ዲበ ይእቲ እብን ይትቀጠቀጥ ።
  scan 93 day ፳፮   ዘሠርክ/ወንጌል
      ም· ፲፬ ቍ· ፴፯ – ፴፱   →  verse 39 > ማቴዎስ 14 has 36
      incipit: ወይእተ ጊዜ አእኰተ ወፈተተ ።
  scan 100 day ፬    ዘቅዳሴ/ግብ፡ ሐዋ፡
      ም· ፩ ቍ· ፳፱ – ፍ፡ም፡   →  verse 29 > ግብ 1 has 26
      incipit: ወይእዜኒ እግዚአ ርኢ ።
  scan 124 day ፳፰   ዘነግህ/ወንጌል
      ም· ፩ ቍ· ፳፮ – ፻፯   →  verse 107 > ሉቃስ 1 has 80
      incipit: ወበሳድስ ወርኅ ተፈነወ ።
  scan 127 day ፩    ዘቅዳሴ/ግብ፡ሐዋ፡
      ም·፯ ቍ· ፶፩ ም·፰ ቍ·፫   →  range descends 51–3
      incipit: አጽኑዓነ ክሣድ ።
  scan 142 day ፲፯   ዘሠርክ/ወንጌል
      ም· ፲፭ ቍ· ፴፭ – ፴፯   →  verse 37 > ሉቃስ 15 has 32
      incipit: ንግሥተ አዜብ ትትነሣእ ምስለ ዛቲ ትውልድ ።
  scan 143 day ፲፰   ዘነግህ/ወንጌል
      ም· ፲፭ ቍ· ፲፱ – ፴፫   →  verse 33 > ዮሐንስ 15 has 27
      incipit: ወብዙኃን እምነ አይሁድ ።
  scan 145 day ፳    ዘነግህ/ወንጌል
      ም· ፩ ቍ·፴፱–፶፭   →  verse 55 > ዮሐንስ 1 has 51
      incipit: ወአመ ሳኒታ ።
  scan 146 day ፳    ዘሠርክ/ወንጌል
      ም· ፳ ቍ· ፴፫ – ፴፭   →  verse 35 > ማቴዎስ 20 has 34
      incipit: ወአንሶሰወ እግዚእ ኢየሱስ ።
  scan 146 day ፳፩   ዘነግህ/ወንጌል
      ም· ፪ ቍ· ፴፯ – ፴፫   →  range descends 37–33
      incipit: ወሀለው ኖሎት ውስተ ውእቱ ብሔር ።
  scan 147 day ፳፩   ዘሠርክ/ወንጌል
      ም· ፯ ቍ· ፶፬ና፶፯   →  verse 57 > ማርቆስ 7 has 37
      incipit: ወአገበሮሙ ሶቤሃ ለአርዳኢሁ ።
  scan 148 day ፳፪   ዘሠርክ/ወንጌል
      ም· ፫ ቍ· ፶፬ – ፶፯   →  verse 57 > ዮሐንስ 3 has 36
      incipit: ወዘእግዚአብሔር ፈነዎ ቃለ እግዚአብሔር ።
  scan 151 day ፳፯   ዘቅዳሴ/ዕብ
      ም· ፲፭ ቍ· ፭ – ፫   →  range descends 5–3
      incipit: በተአምኖ ፈለሰ ሄኖክ ።
  scan 152 day ፳፰   ዘቅዳሴ/ግብ፡ ሐዋ፡
      ም· ፪ ቍ· ፴፪ – ፴   →  range descends 32–30
      incipit: ሎቱ ለኢየሱስ አንሥአ እግዚአብሔር ።
  scan 156 day ፩    ዘቅዳሴ/ወንጌል
      ም· ፲፭ ቍ· ፳፮ – ፲፯   →  range descends 26–17
      incipit: ወሶበ መጽአ ጰራቅሊጦስ ።
  scan 167 day ፲፫   ዘቅዳሴ/ግብ፡ ሐዋ፡
      ም· ፲፬ ቍ· ፳፩ – ፴፮   →  verse 36 > ግብ 14 has 28
      incipit: ወእምዝ ጐብኡ ሐዋርያት ።
  scan 179 day ፳፭   ዘነግህ/ወንጌል
      ም· ፬ ቍ· ፶፫ – ፶፭   →  verse 55 > ሉቃስ 4 has 44
      incipit: ወእምዝ በሳኒታ ዕለት ።
  scan 199 day ፲፯   ዘሠርክ/ወንጌል
      ም· ፯ ቍ· ፶ – ፶፬   →  verse 54 > ዮሐንስ 7 has 53
      incipit: ወይቤሎሙ ኒቆዲሞስ ዘሐረ ኀቤሁ ።
  scan 224 day ፲፬   ዘቅዳሴ/ግብ፡ ሐዋ፡
      ም· ፭ ቍ· ፴፭ – ፴፫   →  range descends 35–33
      incipit: ወይቤሎሙ አንትሙ ሰብአ እስራኤል ።
  scan 244 day ፭    ዘሠርክ/ወንጌል
      ም· ፳፬ ቍ· ፴፫ – ፴፬   →  chapter 24 > ማርቆስ has 16
      incipit: ወተነሥኡ ሶቤሃ ይእተ ሰዓተ ።
  scan 273 day ፭    ዘሠርክ/ምስባክ
      ፶፬ ቍ· ፲፯ – ፲፫   →  range descends 17–13
  scan 292 day ፳፯   ዘቅዳሴ/ዮሐ ፩
      ም· ፪ ቍ· ፳፯ – ፱   →  range descends 27–9
      incipit: ወአንትሙሰ ቅብዐት ብክሙ ።
  scan 300 day ፮    ዘቅዳሴ/ግብ፡ ሐዋ፡
      ም· ፲፮ ቍ· ፲፬ – ፲፫   →  range descends 14–13
      incipit: ወሀለወት ማዕከሎን አሐቲ ብእሲት ።
  scan 315 day ፳፪   ዘቅዳሴ/ግብ፣ ሐዋ፣
      ም· ፭ ቍ· ፴፯ – ፶፬   →  verse 54 > ግብ 5 has 42
      incipit: ወእምዝ ሐረ መጋቤ ምኵራብ ።
  scan 315 day ፳፪   ዘሠርክ/ወንጌል
      ም· ፰ ቍ· ፴፫ – ፴፭   →  verse 35 > ማቴዎስ 8 has 34
      incipit: ወጐዩ ኖሎት ወአተዉ ሀገረ ወዜነዉ ኵሎ ።
  scan 317 day ፳፬   ዘሠርክ/ወንጌል
      ም· ፲፫ ቍ· ፶፯ – ፶፱   →  verse 59 > ማቴዎስ 13 has 58
      incipit: ወይቤሎሙ እግዚእ ኢየሱስ ።
```

---

## 2. Incomplete records

- **ኅዳር ፳፰** has only ዘቅዳሴ, ዘነግህ — missing one service. Scans [95].

That is 1 incomplete day out of 366.

---

## 3. Structural findings that may look like errors

**Part 2 numbering skips ፬.** The book prints ፩ ፪ ፫ then jumps to ፭. The five Lenten
Sunday weeks (ምኵራብ, መጻጕዕ, ደብረ ዘይት, ገብር ኄር, ኒቆዲሞስ) are unnumbered. Recorded as printed;
we did not invent a ፬.

**Part 3's 11 ክፍል are not printed in the body.** Three independent passes over all 36
pages found no `ክፍል <n>` heading. The chapters are a table-of-contents scheme; the page
ranges are derived from red divider lines, hymn-ordinal resets to ፩ኛ, running-head
changes and closing ornaments. Each chapter carries its `boundary_source`.

**ክፍል ፯ ዘሆሣዕና is not a division at all.** ሆሣዕና enters at scan 397 as an ordinary section
with no ክፍል number and no መዝሙር ordinal, while the running head stays ዘዐቢይ ጾም.

**Verse numbers run 1–2 lower** than modern editions in many places — this edition's own
convention, not an error. See the psalm section in README.md.

---

## 4. Unresolved conflict

**ጊዜ index at the 394/395 boundary.** Two transcribers disagree: p394 records ዘወረደ as ፴፫,
p395 records ቅድስት as ፴፫. Both cannot hold. The arithmetic favours ዘወረደ = ፴፪ (ኒቆዲሞስ reads
unambiguously ፴፰; counting back gives ቅድስት ፴፫, ዘወረደ ፴፪). The section **content** agrees in
both files — only this index differs. Left as transcribed, flagged on both pages.

---

## 5. Uncertain readings

**132 `review_notes`** across the page files record uncertain glyphs and printing
oddities at the point they occur. The most common classes:

- Large compound numerals in commemorations (martyr counts) — the least recoverable
  thing in the book; several are flagged from ጥቅምት onward.
- `፰ / ፳ / ፷` share one glyph form at scan resolution, as do `፴ / ፵` and `፮ / ፯`.
- Malformed citations: missing `ቍ·`, doubled `ቍ· ቍ·`, a bare `·`, `ም·` where `ቍ·` belongs.
- A few incipits that run off the scanned edge mid-word — not recoverable by re-reading.

Extract them all with:

```bash
python3 -c "import json,glob;[print(f, n) for f in glob.glob('pages*/p*.json') \
  for n in json.load(open(f,encoding='utf-8')).get('review_notes',[])]"
```
