#!/usr/bin/env python
import sys

for line in sys.stdin:
    fid, _, uids = line.strip().partition('\t')
    uidLis = uids.split(',')
    for uid1 in uidLis:
        for uid2 in uidLis:
            if uid1 == uid2: continue
            print '%s\t%s,%s' %(uid1, uid2, fid)
