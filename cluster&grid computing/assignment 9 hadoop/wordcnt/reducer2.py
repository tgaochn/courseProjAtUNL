#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    cnt, _, word = line.strip().partition('\t')
    print '%s\t%s' % (word, int(cnt))
