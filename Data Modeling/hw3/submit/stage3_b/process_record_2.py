# !/usr/bin/env python
# coding: utf-8
"""
process_record.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/25/2018, 12:10:16 AM
Link:
    
Description:
    
"""
import sys
from utils import searchInTableFile
sys.path.append('stage3_a/')
sys.path.append('../stage3_a/')
from structure import BplusTree
from buildTree import buildBplusTree
import time
DEBUG_MODE = False


def func():
    if DEBUG_MODE:
        dataPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_b\data'
        treeFilePath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage3_b\data'
        fanout = 200
    else:
        dataPath = sys.argv[1]
        treeFilePath = sys.argv[2]
        fanout = int(sys.argv[3])

    bpTreeMsg = buildBplusTree(dataPath, 'message', 3, treeFilePath, fanout)
    start = time.clock()
    tableFn = bpTreeMsg.search(8)
    userRltDic = searchInTableFile(tableFn, 8, 3, 1)
    userIdLis = userRltDic.keys()
    elapsed = time.clock() - start
    print userIdLis
    print("Time used:", elapsed)
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
