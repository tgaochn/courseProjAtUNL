# !/usr/bin/env python
# coding: utf-8
"""
tableSort.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/24/2018, 9:34:57 PM
Link:
    
Description:
    
"""
import os
import time
import sys

DEBUG_MODE = False

def sortTable(dataPath, tableNm, order, colId):
    topRowLis = []
    tablePath = '%s/%s' % (dataPath, tableNm)
    tableFnLis = os.listdir(tablePath)
    isReverse = False if order == 'ascending' else True

    # sort in file
    for tableFn in tableFnLis:
        fn = '%s/%s' % (tablePath, tableFn)
        lines = []
        with open(fn) as f:
            lines = f.readlines()
            topRowLis.append((tableFn, lines[0]))
            if lines[0].split(',')[colId].isdigit():
                lines.sort(key=lambda x: int(x.split(',')[colId]), reverse=isReverse)
            else:
                lines.sort(key=lambda x: x.split(',')[colId], reverse=isReverse)

        with open(fn, 'w') as f:
            for line in lines:
                f.write(line)

        # rename the file with a tmp name
        tmpFn = '%s/_%s' % (tablePath, tableFn)
        os.rename(fn, tmpFn)

    # sort between files
    if topRowLis[0][1].split(',')[colId].isdigit():
        topRowLis.sort(key=lambda x: int(x[1].split(',')[colId]), reverse=isReverse)
    else:
        topRowLis.sort(key=lambda x: x[1].split(',')[colId], reverse=isReverse)
    for newIdx, (tableFn, _) in enumerate(topRowLis):
        newFn = '%s/%s_%s.dat' % (tablePath, tableNm, str(newIdx).zfill(6))
        tmpFn = '%s/_%s' % (tablePath, tableFn)
        os.rename(tmpFn, newFn)
# end_func


def func():
    if DEBUG_MODE:
        dataPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_b\data'
    else:
        dataPath = sys.argv[1]

    sortParaLis = [  # format: [tableName, order(ascending/decending), columnId]
        # ['test', 'ascending', 3],
        ['user', 'ascending', 3],
        ['city', 'ascending', 0],
        ['state', 'ascending', 1],
        ['message', 'ascending', 3],
    ]

    start = time.clock()
    for tableName, order, columnId in sortParaLis:
        sortTable(dataPath, tableName, order, columnId)
    elapsed = time.clock() - start
    print("Time used:", elapsed)
# end_func

def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
