#!/usr/bin/env python
import sys

for line in sys.stdin:
    
    line = line.strip()
    word, _, cnt = line.partition('\t')

    if int(cnt) <= 10: continue
    print '%s\t%s' %(cnt.zfill(6), word)
