import sys

recs = []
rec = dict(user=None, ts=None, diff=[])

for line in sys.stdin:
    if line.startswith('user:'):
        rec['user'] = line
    elif line.startswith(':'):
        rec['diff'].append(line)
    elif line.strip():
        rec['ts'] = line
    else:
        recs.append(rec)
        rec = dict(user=None, ts=None, diff=[])

if rec['user']:
    recs.append(rec)

for r in sorted(recs, key=lambda x: x['ts']):
    print(r['user'], end='')
    print(r['ts'], end='')
    for d in r['diff']:
        print(d, end='')
    print('')
