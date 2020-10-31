# !/usr/bin/env python
# coding: utf-8
"""
genCSV.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/24/2018, 4:18:01 PM
Link:
    
Description:
    
"""

import math
import os


def func1():
    maxFileNum = 2000
    inputCsvPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage1_b\data'
    outputTablePath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_a\data'
    userFn = 'user.csv'
    cityFn = 'city.csv'
    stateFn = 'state.csv'
    msgFn = 'message.csv'
    csvFnLis = [userFn, cityFn, stateFn, msgFn]
    # csvFnLis = [stateFn]

    for csvFn in csvFnLis:
        tablePrefix = csvFn.partition('.')[0]
        csvFn = '%s/%s' % (inputCsvPath, csvFn)
        with open(csvFn) as csvFileobj:
            data = csvFileobj.readlines()
            curDataIdx = 0
            recordTotalCnt = len(data)
            tableRecordCnt = 1 if recordTotalCnt <= maxFileNum else int(math.ceil(recordTotalCnt / maxFileNum))
            fileCnt = recordTotalCnt if recordTotalCnt <= maxFileNum else maxFileNum
            for i in xrange(fileCnt):
                tableId = str(i).zfill(6)
                tablePath = '%s/%s' % (outputTablePath, tablePrefix)
                if not os.path.exists(tablePath):
                    os.makedirs(tablePath)
                tableFn = '%s/%s_%s.dat' % (tablePath, tablePrefix, tableId)
                with open(tableFn, 'w') as tableFileobj:
                    tableData = data[curDataIdx: curDataIdx + tableRecordCnt]
                    curDataIdx = curDataIdx + tableRecordCnt
                    for record in tableData:
                        tableFileobj.write(record)
# end_func


def main():
    func1()
# end_main


if __name__ == "__main__":
    main()
# end_if
