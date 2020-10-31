# !/usr/bin/env python
# coding: utf-8
"""
utils.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/25/2018, 1:51:08 AM
Link:
    
Description:
    
"""

import os


def linearSearch(tablePath, key, keyColId, targetColId):
    tableFnLis = os.listdir(tablePath)
    lines = []
    targetValFreqDic = {}

    # locate file
    for tableFn in tableFnLis:
        tableFn = '%s/%s' % (tablePath, tableFn)
        with open(tableFn) as tableFileobj:
            lines = tableFileobj.readlines()
            if lines[0].strip().split(',')[keyColId] == key:
                break
    
    # fetch data
    for line in lines:
        items = line.strip().split(',')
        targetVal = items[targetColId]
        targetValFreqDic.setdefault(targetVal, 0)
        targetValFreqDic[targetVal] += 1

    return targetValFreqDic
# end_func

