#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName:

Author:
    Tian Gao
Email:
    tgaochn@gmail.com
CreationDate:
    12/2/2017
Description:

"""
from scipy.spatial import ConvexHull
import sys


def reducer(fn=''):
    lastWheatVolLis = []
    lastWheatId = None

    inputSource = open(fn) if fn else sys.stdin
    for line in inputSource:
        wheatID, _, vol = line.strip().partition('\t')
        wheatID = int(wheatID)
        vol = float(vol)

        if wheatID != lastWheatId:
            if lastWheatVolLis:
                volTotal = sum(lastWheatVolLis)
                print '%s\t%s' % (wheatID, volTotal)
            lastWheatId = wheatID
            lastWheatVolLis = [vol]
        else:
            lastWheatVolLis.append(vol)

    volTotal = sum(lastWheatVolLis)
    print '%s\t%s' % (lastWheatId, volTotal)
#end_func


def main():
    fn = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\2'
    # reducer(fn)
    reducer()
#end_main


if __name__ == "__main__":
    main()
#end_if
