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


def sortTable(dataPath, tableNm, order, colId):
    tablePath = '%s/%s' % (dataPath, tableNm)
    tableFnLis = os.listdir(tablePath)
    isReverse = False if order == 'ascending' else True
    recordLis = []
    fileCnt = len(tableFnLis)
    tableRecordCnt = 0
    curDataIdx = 0

    # read all the records
    for tableId, tableFn in enumerate(tableFnLis):
        fn = '%s/%s' % (tablePath, tableFn)
        lines = []
        with open(fn) as f:
            for line in f:
                recordLis.append(line.strip().split(','))
                if tableId == 0:tableRecordCnt += 1

    # sort                 
    if recordLis[0][colId].isdigit():
        recordLis.sort(key=lambda x: eval(x[colId]), reverse=isReverse)
    else:
        recordLis.sort(key=lambda x: x[colId], reverse=isReverse) 
    
    # write files
    for i in xrange(fileCnt):
        tableId = str(i).zfill(6)
        tableFn = '%s/%s_%s.dat' % (tablePath, tableNm, tableId)
        with open(tableFn, 'w') as tableFileobj:
            tableData = recordLis[curDataIdx: curDataIdx + tableRecordCnt]
            curDataIdx = curDataIdx + tableRecordCnt
            # print tableFn
            # print tableData
            for record in tableData:
                outputStr = ','.join(record)
                tableFileobj.write('%s\n' % outputStr)
# end_func


def func():
    dataPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_b\data'
    sortParaLis = [  # format: [tableName, order(ascending/decending), columnId]
        # ['test', 'decending', 0],
        ['state', 'ascending', 1],
        ['city', 'ascending', 0],
        ['user', 'ascending', 0],
        ['message', 'ascending', 3],
    ]

    for tableName, order, columnId in sortParaLis:
        sortTable(dataPath, tableName, order, columnId)
# end_func

def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
