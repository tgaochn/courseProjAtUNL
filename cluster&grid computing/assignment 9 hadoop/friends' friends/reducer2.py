#!/usr/bin/env python

import sys

lastRecommLis = []
lastUid1 = None

for line in sys.stdin:
    uid1, _, uid2_fid = line.strip().partition('\t')
    uid2, _, fid = uid2_fid.partition(',')

    if uid1 != lastUid1:
        if lastUid1:
            uid2Set = set()
            uid2_fidSet_Dict = {}
            for uid2, fid in lastRecommLis:
                uid2_fidSet_Dict.setdefault(uid2, set())
                uid2_fidSet_Dict[uid2].add(fid)
                uid2Set.add(uid2)
            recommLis = [(uid2, len(uid2_fidSet_Dict[uid2])) for uid2 in uid2Set]
            recommLis.sort(key=lambda x:x[1], reverse=True)
            for i in range(5):
                if i >= len(recommLis) - 1: continue
                print '%s\t%s\t%s\t%s' % (lastUid1, recommLis[i][0], recommLis[i][1], ','.join(uid2_fidSet_Dict[recommLis[i][0]]))
        lastUid1 = uid1
        lastRecommLis = [(uid2, fid)]
    else:
        lastRecommLis.append((uid2, fid))


uid2Set = set()
uid2_fidSet_Dict = {}
for uid2, fid in lastRecommLis:
    uid2_fidSet_Dict.setdefault(uid2, set())
    uid2_fidSet_Dict[uid2].add(fid)
    uid2Set.add(uid2)
recommLis = [(uid2, len(uid2_fidSet_Dict[uid2])) for uid2 in uid2Set]
recommLis.sort(key=lambda x:x[1], reverse=True)
for i in range(5):
    if i >= len(recommLis) - 1: continue
    print '%s\t%s\t%s\t%s' % (lastUid1, recommLis[i][0], recommLis[i][1], ','.join(uid2_fidSet_Dict[recommLis[i][0]]))

