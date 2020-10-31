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
import sys


def mapper(fn=''):
    inputSource = open(fn) if fn else sys.stdin
    for line in inputSource:
        items = line.strip().split('\t')
        wheatId = items[0]
        layerId = items[1]
        zstep = items[2]
        x = float(items[3])
        y = float(items[4])
        print '%s,%s\t%s,%s,%s' % (wheatId, layerId, zstep, x, y)
#end_func


def main():
    fn = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\layerID\1.ply'
    # mapper(fn)
    mapper()
#end_main


if __name__ == "__main__":
    main()
#end_if
