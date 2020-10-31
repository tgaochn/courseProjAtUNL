#!/usr/bin/python
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
    lastPointLis = []
    lastWheatId = None
    lastLayerId = None
    lastHeight = None

    inputSource = open(fn) if fn else sys.stdin
    for line in inputSource:
        idInfo, _, pointInfo = line.strip().partition('\t')
        wheatID, _, layerID = idInfo.partition(',')
        height, x, y = pointInfo.split(',')
        wheatID = int(wheatID)
        layerID = int(layerID)
        height = float(height)
        x = float(x)
        y = float(y)

        if wheatID != lastWheatId or layerID != lastLayerId:
            if lastPointLis and len(lastPointLis) >= 3:
                hull = ConvexHull(lastPointLis)
                area = hull.volume
                vol = area * lastHeight
                print '%s\t%s\t%s' % (wheatID, layerID, vol)
            lastWheatId = wheatID
            lastLayerId = layerID
            lastHeight = height
            lastPointLis = [(x, y)]
        else:
            lastPointLis.append((x, y))

    hull = ConvexHull(lastPointLis)
    area = hull.volume
    vol = area * lastHeight
    print '%s\t%s\t%s' % (lastWheatId, lastLayerId, vol)
#end_func


def main():
    fn = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\2'
    # reducer(fn)
    reducer()
#end_main


if __name__ == "__main__":
    main()
#end_if
