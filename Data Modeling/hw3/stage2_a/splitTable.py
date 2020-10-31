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
from datetime import datetime
import sys

DEBUG_MODE = False

def func1():

    if DEBUG_MODE:
        inputCsvPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage1_b\data'
        outputTablePath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_a\data'
    else:
        inputCsvPath = sys.argv[1]
        outputTablePath = sys.argv[2]

    splitInfoLis = [  # csvFn, keyColId
        ['user.csv', 4],
        ['city.csv', 0],
        ['state.csv', 1],
        ['message.csv', 3],
    ]

    # for csvFn, keyColId, parser in splitInfoLis:
    for csvFn, keyColId in splitInfoLis:
        tableFileIdMap = {}
        outputDataLis = []
        tableNm = csvFn.partition('.')[0]
        csvFn = '%s/%s' % (inputCsvPath, csvFn)
        tablePath = '%s/%s' % (outputTablePath, tableNm)
        if not os.path.exists(tablePath):
            os.makedirs(tablePath)

        with open(csvFn) as csvFileobj:
            data = csvFileobj.readlines()
            keySet = set(map(lambda x: x.strip().split(',')[keyColId], data))
            keyLis = sorted(list(keySet))
            keyCnt = len(keySet)

            for i in xrange(keyCnt):
                outputDataLis.append([])
                key = keyLis[i]
                tableFileIdMap[key] = i

            # split data into different lists
            for record in data:
                key = record.strip().split(',')[keyColId]
                tableFileId = tableFileIdMap[key]
                outputDataLis[tableFileId].append(record)
            
        # write splitted table files
        for i in xrange(keyCnt):
            key = keyLis[i]
            tableFn = '%s/%s_%s.dat' % (tablePath, tableNm, str(i).zfill(6))
            outputData = outputDataLis[i]
            with open(tableFn, 'w') as tableFile:
                for data in outputData:
                    tableFile.write(data)
# end_func


def main():
    func1()
# end_main


if __name__ == "__main__":
    main()
# end_if
