# !/usr/bin/env python
# coding: utf-8
"""
loadBplusTree.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/28/2018, 4:46:25 PM
Link:
    
Description:
    
"""


def searchInTableFile(tableFn, key, keyColId, targetColId):
    lines = []
    targetValFreqDic = {}

    # locate file
    with open(tableFn) as tableFileobj:
        lines = tableFileobj.readlines()
        for line in lines:
            items = line.strip().split(',')
            targetVal = items[targetColId]
            targetValFreqDic.setdefault(targetVal, 0)
            targetValFreqDic[targetVal] += 1

    return targetValFreqDic
# end_test


def test():
    fn = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_a\data\state\state_000028.dat'
    key = 'Nebraska'
    keyColId = 1
    targetColId = 0

    fn = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_a\data\message\message_000001.dat'
    key = '02'
    keyColId = 3
    targetColId = 1

    print searchInTableFile(fn, key, keyColId, targetColId)
# end_test


def main():
    test()
# end_main


if __name__ == "__main__":
    main()
# end_if


