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

from utils import readBinRecord


def func1():
    recordCnt = 2000
    dataPath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\assignment\hw3\stage1'
    userFn = 'user.csv'
    cityFn = 'city.csv'
    stateFn = 'state.csv'
    msgFn = 'message.csv'
    cityDic1 = {}
    cityDic2 = {}
    stateDic1 = {}
    stateDic2 = {}
    msgIdx = 0

    with open(userFn, 'w') as userFileobj, open(cityFn, 'w') as cityFileobj, open(stateFn, 'w') as stateFileobj, open(msgFn, 'w') as msgFileobj:
        for rid in xrange(recordCnt):
            fn = '%s/record_%s.dat' % (dataPath, str(rid).zfill(6))
            userInfoDic, msgLis = readBinRecord(fn)

            uid = str(userInfoDic['uid'])
            givenNm = userInfoDic['givenNm']
            familyNm = userInfoDic['familyNm']
            city = userInfoDic['city']
            state = userInfoDic['state']
            msgNum = userInfoDic['msgNum']
            cityDic1.setdefault(city, len(cityDic1))
            cityId = cityDic1[city]
            cityDic2[cityId] = city
            stateDic1.setdefault(state, len(stateDic1))
            stateId = stateDic1[state]
            stateDic2[stateId] = state

            outputStr = ','.join([uid, givenNm, familyNm, str(cityId), str(stateId)])
            userFileobj.write('%s\n' % outputStr)

            for msgDic in msgLis:
                text = msgDic['text']
                year = str(msgDic['year'])
                month = str(msgDic['month'])
                day = str(msgDic['day'])
                hour = str(msgDic['hour'])
                minute = str(msgDic['minute'])
                outputStr = ','.join([str(msgIdx), uid, '%s/%s/%s %s:%s' % (year, month.zfill(2), day.zfill(2), hour.zfill(2), minute.zfill(2)), hour.zfill(2), text])
                msgFileobj.write('%s\n' % outputStr)
                msgIdx += 1

        cityCnt = len(cityDic2)
        for i in xrange(cityCnt):
            city = cityDic2[i]
            outputStr = ','.join([str(i), city])
            cityFileobj.write('%s\n' % outputStr)

        stateCnt = len(stateDic2)
        for i in xrange(stateCnt):
            state = stateDic2[i]
            outputStr = ','.join([str(i), state])
            stateFileobj.write('%s\n' % outputStr)            
# end_func


def main():
    func1()
# end_main


if __name__ == "__main__":
    main()
# end_if
