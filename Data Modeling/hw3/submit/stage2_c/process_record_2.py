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

from utils import linearSearch
import time
import sys

DEBUG_MODE = False

def func():
    if DEBUG_MODE:
        dataPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_b\data'
    else:
        dataPath = sys.argv[1]

    start = time.clock()

    tableName = 'message'
    tablePath = '%s/%s' % (dataPath, tableName)
    userIdDic = linearSearch(tablePath, '08', 3, 1)

    elapsed = time.clock() - start
    print("Time used:", elapsed)
    print userIdDic.keys()
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
