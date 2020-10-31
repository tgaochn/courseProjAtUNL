#!/usr/bin/env python
import sys

lastUidLis = []
lastFuid = None

for line in sys.stdin:
    fuid, _, uid = line.strip().partition('\t')
    if fuid != lastFuid:
        if lastFuid:
            uids = ','.join(lastUidLis)
            print '%s\t%s' % (fuid, uids)
        lastFuid = fuid
        lastUidLis = [uid]
    else:
        lastUidLis.append(uid)

uids = ','.join(lastUidLis)
print '%s\t%s' % (fuid, uids)
