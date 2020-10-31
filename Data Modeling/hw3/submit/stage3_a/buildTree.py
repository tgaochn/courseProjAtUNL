# !/usr/bin/env python
# coding: utf-8
"""
buildTree.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/26/2018, 12:22:26 PM
Link:
    
Description:
    
"""
import os
from structure import BplusTree
import sys
import time


DEBUG_MODE = False

def buildBplusTree(dataPath, tableName, columnId, treeFilePath, fanout):
    tablePath = os.path.join(dataPath, tableName)
    tableFnLis = os.listdir(tablePath)
    tableFileInfoLis = []
    for tableFn in tableFnLis:
        tableFn = os.path.join(tablePath, tableFn)
        with open(tableFn) as tableFileobj:
            topLine = tableFileobj.readline()
            key = topLine.strip().split(',')[columnId]
            tableFileInfoLis.append((key, tableFn))
    treeFilePath = os.path.join(treeFilePath, tableName)
    if not os.path.exists(treeFilePath):
        os.makedirs(treeFilePath)
    bpTree = BplusTree(treeFilePath, fanout)
    bpTree.buildTree(tableFileInfoLis)
    return bpTree
# end_test


def run():
    if DEBUG_MODE:
        dataPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_b\data'
        treeFilePath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage3_a\data'
        fanout = 200
    else:
        dataPath = sys.argv[1]
        treeFilePath = sys.argv[2]
        fanout = int(sys.argv[3])

    sortParaLis = [  # format: [tableName, columnId]
        # ['test', 3],
        ['user', 4],
        ['city', 0],
        ['state', 1],
        ['message', 3],
    ]

    start = time.clock()
    for tableName, columnId in sortParaLis:
        bpTree = buildBplusTree(dataPath, tableName, columnId, treeFilePath, fanout)
        print bpTree.search('Nebraska')

    elapsed = time.clock() - start
    print("Time used:", elapsed)
# end_test


def main():
    run()
# end_main


if __name__ == "__main__":
    main()
# end_if
