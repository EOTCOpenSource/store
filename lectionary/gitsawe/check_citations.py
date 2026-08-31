#!/usr/bin/env python3
"""Flag impossible citations automatically, so agents don't have to zoom every one.

Parses the Ge'ez numerals in chapter_verse fields and tests them against real
chapter/verse counts. What it catches is exactly the class of error that costs a
900dpi round-trip to find by eye.
"""
import json, glob, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
G = {'፩':1,'፪':2,'፫':3,'፬':4,'፭':5,'፮':6,'፯':7,'፰':8,'፱':9,
     '፲':10,'፳':20,'፴':30,'፵':40,'፶':50,'፷':60,'፸':70,'፹':80,'፺':90,'፻':100}

def g2i(s):
    """Ge'ez numeral -> int. ፻ multiplies what precedes it (፪፻=200)."""
    total = run = 0
    for ch in s:
        v = G.get(ch)
        if v is None: continue
        if v == 100:
            total += (run or 1) * 100; run = 0
        else:
            run += v
    return total + run

VERSES = {  # verses per chapter
 'ማቴዎስ':[25,23,17,25,48,34,29,34,38,42,30,50,58,36,39,28,27,35,30,34,46,46,39,51,46,75,66,20],
 'ማርቆስ':[45,28,35,41,43,56,37,38,50,52,33,44,37,72,47,20],
 'ሉቃስ':[80,52,38,44,39,49,50,56,62,42,54,59,35,35,32,31,37,43,48,47,38,71,56,53],
 'ዮሐንስ':[51,25,36,54,47,71,53,59,41,42,57,50,38,31,27,33,26,40,42,31,25],
 'ግብ':[26,47,26,37,42,15,60,40,43,48,30,25,52,28,41,40,40,34,41,38,40,30,35,27,27,32,44,31],
}
ALIAS = {'ማቴ':'ማቴዎስ','ማር':'ማርቆስ','ዮሐ':'ዮሐንስ','ግብ፡ ሐዋ፡':'ግብ','ግብ· ሐዋ·':'ግብ',
         'ግብ፡ሐዋ፡':'ግብ','ግብ: ሐዋ:':'ግብ'}

def norm(book):
    b = (book or '').strip().rstrip('·:፡').strip()
    if re.search(r'(ዮሐ|ጴጥ|ቆሮ|ቆር|ተሰሎ|ጢሞ)[፡\.\s·]*[፩፪፫]\s*$', b) or re.match(r'^[፩፪፫]', b):
        return None   # numbered epistle, not a gospel/Acts
    if b in VERSES: return b
    if b in ALIAS:  return ALIAS[b]
    for k in ('ግብ','ማቴ','ማር','ሉቃስ','ዮሐንስ','ዮሐ'):
        if b.startswith(k): return ALIAS.get(k, k if k in VERSES else None)
    return None

def scan(cv, book):
    """Return problems for one chapter_verse field.

    Layout differs by kind:
      ምስባክ  ->  "፻፲፰ ቍ· ፹፮ – ፹፯"      psalm first, no ም· marker
      others ->  "ም· ፰ ቍ· ፲፱ – ፳፯"      explicit ም· chapter
    So always split on the ቍ·/ቄ· marker: left = chapter, right = verses.
    """
    out = []
    cv = cv or ''
    parts = re.split(r'[ቍቄ][·\.:፡]?', cv, maxsplit=1)
    left, right = (parts[0], parts[1]) if len(parts) == 2 else (cv, '')
    m = re.search(r'([፩-፼]+)', re.sub(r'^\s*ም[·\.:፡]?', '', left))
    ch = g2i(m.group(1)) if m else None
    vs = [v for v in (g2i(x) for x in re.findall(r'[፩-፼]+', right)) if v]
    b = norm(book)
    if b and ch:
        nch = len(VERSES[b])
        if ch > nch:
            out.append(f'chapter {ch} > {b} has {nch}')
        elif vs:
            mx = VERSES[b][ch-1]
            over = [v for v in vs if v > mx]
            if over: out.append(f'verse {max(over)} > {b} {ch} has {mx}')
    if len(vs) >= 2 and vs[0] > vs[-1] and 'ፍ' not in (cv or ''):
        out.append(f'range descends {vs[0]}–{vs[-1]}')
    return out

def walk(day, page, hits):
    for sname, svc in (day.get('services') or {}).items():
        if not isinstance(svc, dict): continue
        for key, body in svc.items():
            if key == 'epistles_and_acts':
                for r in body or []:
                    for p in scan(r.get('chapter_verse'), r.get('reading_type')):
                        hits.append((page, day.get('day_number'), f'{sname}/{r.get("reading_type")}', r.get('chapter_verse'), p, r.get('incipit','')))
            elif isinstance(body, dict) and 'chapter_verse' in body:
                for p in scan(body.get('chapter_verse'), body.get('book')):
                    hits.append((page, day.get('day_number'), f'{sname}/{key}', body.get('chapter_verse'), p, body.get('incipit','')))

hits = []
for f in sorted(glob.glob(f'{D}/source-pages/p*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for day in d.get('days', []):
        walk(day, d['scan_page'], hits)

print(f'=== impossible citations: {len(hits)}\n')
for pg, dn, where, cv, why, inc in hits:
    print(f'  scan {pg} day {dn:4} {where}')
    print(f'      {cv}   →  {why}')
    if inc: print(f'      incipit: {inc[:52]}')
