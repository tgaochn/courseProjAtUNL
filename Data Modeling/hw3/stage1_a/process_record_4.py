# !/usr/bin/env python
# coding: utf-8
"""
process_record_1.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/23/2018, 10:01:00 PM
Link:
    
Description:
    
"""

from utils import readBinRecord


def func1():
    recordCnt = 2000
    dataPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\assignment\hw3\stage1'
    maxMsgCnt = -1
    maxMsgUserInfo = {}
    for rid in xrange(recordCnt):
        fn = '%s/record_%s.dat' % (dataPath, str(rid).zfill(6))
        userInfoDic, msgLis = readBinRecord(fn)
        if userInfoDic['state'] == 'Nebraska':
            filteredMsg = filter(lambda x: x['hour'] == 8, msgLis)
            if len(filteredMsg) > maxMsgCnt:
                maxMsgCnt = len(filteredMsg)
                maxMsgUserInfo = userInfoDic
    
    print maxMsgUserInfo
# end_func


def main():
    func1()
# end_main


if __name__ == "__main__":
    main()
# end_if
