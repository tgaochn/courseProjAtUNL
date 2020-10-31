#!/usr/bin/env python
import sys

for line in sys.stdin:
    uid, _, fuids = line.strip().partition('\t')
    fuidLis = fuids.split(',')
    for fuid in fuidLis:
        print '%s\t%s' %(fuid, uid)
