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
import sys


def mapper(fn=''):
    inputSource = open(fn) if fn else sys.stdin
    for line in inputSource:
        items = line.strip().split('\t')
        wheatId = items[0]
        vol = items[2]
        print '%s\t%s' % (wheatId, vol)
#end_func


def main():
    fn = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\1'
    # mapper(fn)
    mapper()
#end_main


if __name__ == "__main__":
    main()
#end_if
