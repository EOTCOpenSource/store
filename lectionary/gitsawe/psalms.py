#!/usr/bin/env python3
"""Septuagint (LXX) ↔ Masoretic (MT) psalm numbering.

The Ethiopic psalter descends from the Septuagint, so every መዝሙር/ምስባክ citation in
this book uses LXX numbering. Most English Bibles use the Masoretic numbering.
They diverge by one across most of the psalter because LXX merges MT 9+10 and
MT 114+115, and splits MT 116 and MT 147.

    LXX 1-8      = MT 1-8            (same)
    LXX 9        = MT 9 + 10         (merged)
    LXX 10-112   = MT 11-113         (MT = LXX + 1)
    LXX 113      = MT 114 + 115      (merged)
    LXX 114      = MT 116:1-9        (split)
    LXX 115      = MT 116:10-19      (split)
    LXX 116-145  = MT 117-146        (MT = LXX + 1)
    LXX 146      = MT 147:1-11       (split)
    LXX 147      = MT 147:12-20      (split)
    LXX 148-150  = MT 148-150        (same)
    LXX 151      = not in MT

So a ምስባክ citing መዝ· ፻፲፰ (Ps 118 LXX) is Psalm 119 in an English Bible — the long
acrostic. This is the single most likely source of confusion for anyone using this
data against a modern translation.
"""

# Psalm 118 (LXX) = 119 (MT) is the great acrostic: 22 stanzas of 8 verses, one per
# Hebrew letter. The Ethiopic tradition keeps the stanza names, and the book cites them
# by name in the funeral rubric on printed page 416:
#   "የመጀመሪያ ምዕራፍ አሌፍ ....... ቤት .......ጋሜል ....... በል"
# Each stanza's first word in Ge'ez begins with its letter — ጻዴ opens ጻድቅ አንተ እግዚአ.
PS118_STANZAS = [
    ('አሌፍ',   'Aleph',  1,   8), ('ቤት',    'Beth',   9,  16),
    ('ጋሜል',   'Gimel', 17,  24), ('ዳሌጥ',   'Daleth',25,  32),
    ('ሄ',     'He',    33,  40), ('ዋው',    'Waw',   41,  48),
    ('ዛይ',    'Zayin', 49,  56), ('ሔት',    'Heth',  57,  64),
    ('ጤት',    'Teth',  65,  72), ('ዮድ',    'Yod',   73,  80),
    ('ካፍ',    'Kaph',  81,  88), ('ላሜድ',   'Lamed', 89,  96),
    ('ሜም',    'Mem',   97, 104), ('ኖን',    'Nun',  105, 112),
    ('ሳምኬት',  'Samekh',113,120), ('ዐይን',   'Ayin', 121, 128),
    ('ፌ',     'Pe',   129, 136), ('ጻዴ',    'Tsade',137, 144),
    ('ቆፍ',    'Qoph', 145, 152), ('ሬስ',    'Resh', 153, 160),
    ('ሳን',    'Shin', 161, 168), ('ተው',    'Taw',  169, 176),
]

def ps118_stanza(verse):
    """Which acrostic stanza a Ps 118 (LXX) verse falls in."""
    for i, (geez, latin, lo, hi) in enumerate(PS118_STANZAS, 1):
        if lo <= verse <= hi:
            return {'number': i, 'name': geez, 'latin': latin, 'verses': [lo, hi]}
    return None

def ps118_stanzas_for_range(lo, hi=None):
    """Every stanza a verse range touches (a citation may straddle two)."""
    hi = hi or lo
    out = []
    for v in (lo, hi):
        st = ps118_stanza(v)
        if st and st not in out: out.append(st)
    return out


def lxx_to_mt(n):
    """Return the Masoretic reference for an LXX psalm number, as a string."""
    if not isinstance(n, int) or not (1 <= n <= 151):
        return None
    if n <= 8:            return str(n)
    if n == 9:            return "9-10"
    if 10 <= n <= 112:    return str(n + 1)
    if n == 113:          return "114-115"
    if n == 114:          return "116:1-9"
    if n == 115:          return "116:10-19"
    if 116 <= n <= 145:   return str(n + 1)
    if n == 146:          return "147:1-11"
    if n == 147:          return "147:12-20"
    if 148 <= n <= 150:   return str(n)
    return "not in the Masoretic psalter (LXX/Ethiopic only)"

if __name__ == '__main__':
    for lxx in (1, 8, 9, 10, 22, 50, 83, 112, 113, 114, 115, 116, 118, 145, 146, 147, 148, 150, 151):
        print(f"  LXX {lxx:>3}  ->  MT {lxx_to_mt(lxx)}")
    print("\n  Ps 118 (LXX) = 119 (MT) acrostic stanzas:")
    for i,(g,l,lo,hi) in enumerate(PS118_STANZAS,1):
        print(f"    {i:>2}. {g:<7} {l:<7} vv {lo}-{hi}")
