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

    tableName = 'state'
    tablePath = '%s/%s' % (dataPath, tableName)
    stateIdDic = linearSearch(tablePath, 'Nebraska', 1, 0)

    tableName = 'user'
    tablePath = '%s/%s' % (dataPath, tableName)
    userIdDic1 = linearSearch(tablePath, stateIdDic.keys()[0], 4, 0)

    tableName = 'message'
    tablePath = '%s/%s' % (dataPath, tableName)
    userIdDic2 = linearSearch(tablePath, '08', 3, 1)
    userMsgLis = [(userId, msgCnt) for userId,
                 msgCnt in userIdDic2.iteritems() if userId in userIdDic1]

    maxMsgUser = max(userMsgLis, key=lambda x: x[1])

    elapsed = time.clock() - start
    print("Time used:", elapsed)
    print maxMsgUser
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
