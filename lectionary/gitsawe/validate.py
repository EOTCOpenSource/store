#!/usr/bin/env python3
"""QA over pages/*.json and the merged master.

Checks structure and coverage, and surfaces every review_note in one place.
Does not touch the data — read-only.
"""
import json, glob, os, sys, re

D = os.path.dirname(os.path.abspath(__file__))
GEEZ = {'፩':1,'፪':2,'፫':3,'፬':4,'፭':5,'፮':6,'፯':7,'፰':8,'፱':9,
        '፲':10,'፳':20,'፴':30,'፵':40,'፶':50,'፷':60,'፸':70,'፹':80,'፺':90,'፻':100}

def g2i(s):
    return sum(GEEZ.get(c, 0) for c in s)

struct = json.load(open(f'{D}/gitsawe-structure.json', encoding='utf-8'))
ranges = {}
for season in struct['parts'][0]['seasons']:
    for m in season['months']:
        ranges[m['month']] = tuple(m['scan_pages'])

problems, notes, pages = [], [], {}

for path in sorted(glob.glob(f'{D}/source-pages/p*.json')):
    base = os.path.basename(path)
    try:
        p = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        problems.append(f'{base}: UNPARSEABLE — {e}')
        continue
    if 'part' in p:      # Parts 2-5 use the sections schema, not days — checked separately
        continue
    n = p.get('scan_page')
    if n is None:
        problems.append(f'{base}: missing scan_page'); continue
    if int(base[1:-5]) != n:
        problems.append(f'{base}: filename does not match scan_page {n}')
    if p.get('printed_page') != n - 3:
        problems.append(f'{base}: printed_page {p.get("printed_page")} != scan {n} - 3')
    mo = p.get('month')
    if mo in ranges and not (ranges[mo][0] <= n <= ranges[mo][1]):
        problems.append(f'{base}: scan {n} outside {mo} range {ranges[mo]}')
    pages[n] = p
    for note in p.get('review_notes', []):
        notes.append(f'  scan {n} ({mo}): {note}')
    if not p.get('days'):
        problems.append(f'{base}: no days')
    for d in p.get('days', []):
        dn = d.get('day_number')
        if not dn:
            problems.append(f'{base}: a day has no day_number')
        # a day continued from the previous page carries its heading there
        if not d.get('commemoration') and 'continued_from_scan_page' not in d:
            problems.append(f'{base} day {dn}: no commemoration and not marked as continued')
        svc = d.get('services') or {}
        if not svc:
            problems.append(f'{base} day {dn}: no services')
        for name, body in svc.items():
            if name not in ('ዘነግህ', 'ዘቅዳሴ', 'ዘሠርክ'):
                problems.append(f'{base} day {dn}: unexpected service "{name}"')
            for key in ('ምስባክ', 'ምስባክ_ዓዲ'):
                ms = body.get(key) if isinstance(body, dict) else None
                if isinstance(ms, dict) and not ms.get('verses'):
                    problems.append(f'{base} day {dn} {name}/{key}: no verses')

# month endpoint anchors: a uniform day-number shift is invisible to a
# continuity check but shows up immediately at the month's first and last page
print('=== month endpoint anchors')
for mo,(lo,hi) in ranges.items():
    first = pages.get(lo); last = pages.get(hi)
    if not first or not last: continue
    fd = [d['day_number'] for d in first.get('days',[])]
    ld = [d['day_number'] for d in last.get('days',[])]
    bad=[]
    if fd and g2i(fd[0]) != 1:  bad.append(f'first page (scan {lo}) opens at {fd[0]} not ፩')
    if ld and g2i(ld[-1]) not in (30,6): bad.append(f'last page (scan {hi}) ends at {ld[-1]} not ፴')
    status = '  '.join(bad) if bad else 'ok'
    print(f'  {mo:7} scan {lo}->{fd[0] if fd else "?"}   scan {hi}->{ld[-1] if ld else "?"}   {status}')

# coverage + day continuity per month
print('\n=== coverage')
for mo, (lo, hi) in ranges.items():
    have = sorted(n for n in pages if pages[n].get('month') == mo)
    if not have:
        continue
    missing = [n for n in range(lo, hi + 1) if n not in have]
    print(f'  {mo:7} pages {len(have):>2}/{hi-lo+1:<2} '
          f'({have[0]}-{have[-1]})' + (f'  MISSING {missing}' if missing else ''))

print('\n=== merged master')
master = json.load(open(f'{D}/gitsawe-master.json', encoding='utf-8'))
tot = ext = 0
for part in master['parts']:
    for s in part.get('seasons', []):
        for m in s['months']:
            tot += m['day_count']; ext += m['days_extracted']
            if m['days_extracted']:
                nums = [g2i(d['day_number']) for d in m['days']]
                gaps = [i for i in range(1, max(nums) + 1) if i not in nums]
                dups = sorted({n for n in nums if nums.count(n) > 1})
                flag = ''
                if gaps: flag += f'  GAPS {gaps}'
                if dups: flag += f'  DUPS {dups}'
                print(f'  {m["month"]:7} {m["days_extracted"]:>2}/{m["day_count"]:<2} {m["status"]:8}{flag}')
print(f'  total {ext}/{tot} ({ext*100//tot}%)')

print(f'\n=== structural problems: {len(problems)}')
for x in problems: print('  ' + x)
print(f'\n=== review notes: {len(notes)}')
for x in notes: print(x)
sys.exit(1 if problems else 0)
