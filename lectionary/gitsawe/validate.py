#!/usr/bin/env python3
"""Validation and QA for lectionary dataset.

Checks structure, coverage, date format, and English key consistency
across months, parts, and gitsawe-master.json.
"""
import json, glob, os, sys, re

D = os.path.dirname(os.path.abspath(__file__))
problems = []

# 1. Validate months
months_dir = f'{D}/months'
month_files = sorted(os.listdir(months_dir))
if len(month_files) != 13:
    problems.append(f"Expected 13 month files, found {len(month_files)}")

total_days = 0
dates_seen = set()

print("=== validating month files")
for mf in month_files:
    p = os.path.join(months_dir, mf)
    data = json.load(open(p, encoding='utf-8'))
    m_name = data.get('month')
    m_idx = data.get('monthIndex')
    day_count = data.get('dayCount')
    days = data.get('days', [])
    
    if len(days) != day_count:
        problems.append(f"{mf}: declared dayCount {day_count} != actual days {len(days)}")
        
    for d in days:
        date_key = d.get('date')
        if not date_key or not re.match(r'^\d{2}-\d{2}$', date_key):
            problems.append(f"{mf}: invalid date format '{date_key}'")
        if date_key in dates_seen:
            problems.append(f"Duplicate date key '{date_key}' in {mf}")
        dates_seen.add(date_key)
        
        if not d.get('title'):
            problems.append(f"{mf} date {date_key}: missing title")
            
        for sname in ('negh', 'kidassie', 'serk'):
            if sname in d:
                svc = d[sname]
                if 'msbak' in svc:
                    if not isinstance(svc['msbak'], list):
                        problems.append(f"{mf} {date_key} {sname}: msbak must be a list")
                    for m in svc['msbak']:
                        if not m.get('text', {}).get('geez'):
                            problems.append(f"{mf} {date_key} {sname} msbak: missing text.geez")
                            
    total_days += len(days)
    print(f"  {m_name:8} (month {m_idx:02d}): {len(days)} days ok")

print(f"\nTotal fixed-cycle days: {total_days}/366")
if total_days != 366:
    problems.append(f"Expected 366 days across year, got {total_days}")

# 2. Validate parts
print("\n=== validating parts")
part_files = {
    '02-movable-feasts.json': 49,
    '03-sunday-hymns.json': 91,
    '04-atnatewos.json': 25,
    '05-bahre-hasab.json': 15,
}

for pf, expected_count in part_files.items():
    ppath = f'{D}/parts/{pf}'
    if not os.path.exists(ppath):
        problems.append(f"Missing part file: {pf}")
        continue
    pdata = json.load(open(ppath, encoding='utf-8'))
    if pf == '05-bahre-hasab.json':
        rows = pdata.get('table', {}).get('rows', [])
        if len(rows) != expected_count:
            problems.append(f"{pf}: expected {expected_count} rows, found {len(rows)}")
        print(f"  {pf:25}: {len(rows)} table rows ok")
    else:
        sections = pdata.get('sections', [])
        if len(sections) != expected_count:
            problems.append(f"{pf}: expected {expected_count} sections, found {len(sections)}")
        print(f"  {pf:25}: {len(sections)} sections ok")

# 3. Validate master
print("\n=== validating gitsawe-master.json")
master_path = f'{D}/gitsawe-master.json'
if not os.path.exists(master_path):
    problems.append("Missing gitsawe-master.json")
else:
    mdata = json.load(open(master_path, encoding='utf-8'))
    parts = mdata.get('parts', [])
    if len(parts) != 5:
        problems.append(f"Master parts count expected 5, found {len(parts)}")
    print(f"  Master has {len(parts)} parts ok")

# 4. Validate daily-gitsawe.json if present
daily_path = f'{D}/daily-gitsawe.json'
if os.path.exists(daily_path):
    ddata = json.load(open(daily_path, encoding='utf-8'))
    if len(ddata) != 366:
        problems.append(f"daily-gitsawe.json has {len(ddata)} days, expected 366")
    print(f"  daily-gitsawe.json: {len(ddata)} days ok")

print(f"\n=== validation summary: {len(problems)} problem(s)")
for p in problems:
    print(f"  ERROR: {p}")

sys.exit(1 if problems else 0)
