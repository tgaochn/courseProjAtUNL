# !/usr/bin/env python
# coding: utf-8
"""
utils.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/23/2018, 11:12:35 PM
Link:

Description:

"""
import struct


def readBinRecord(fn):
    with open(fn, 'rb') as f:
        uid = struct.unpack('i', f.read(4))[0]
        userNm = struct.unpack('64s', f.read(64))
        userLoc = struct.unpack('64s', f.read(64))
        msgNum = struct.unpack('i', f.read(4))[0]
        userNm = removeStrSuffix(userNm[0], '\x00')
        userLoc = removeStrSuffix(userLoc[0], ',', 2)

        givenNm, familyNm = userNm.split(' ')

        if userLoc[0] == '\x00':
            city, state = 'null', 'null'
        else:
            city, state = userLoc.split(',')

        userInfoDic = {
            'uid': uid,
            'givenNm': givenNm,
            'familyNm': familyNm,
            'city': city,
            'state': state,
            'msgNum': msgNum,
        }
        msgLis = []

        for i in xrange(msgNum):
            text = struct.unpack('1024p', f.read(1024))[0]
            text = removeStrSuffix(text, '\x00')
            year = struct.unpack('i', f.read(4))[0]
            month = struct.unpack('i', f.read(4))[0]
            day = struct.unpack('i', f.read(4))[0]
            hour = struct.unpack('i', f.read(4))[0]
            minute = struct.unpack('i', f.read(4))[0]

            msgDic = {
                'text': text,
                'year': year,
                'month': month,
                'day': day,
                'hour': hour,
                'minute': minute,
            }
            msgLis.append(msgDic)

        return userInfoDic, msgLis
# end_func


def removeStrSuffix(rawStr, endChar, charIdx=1):
    endIdx = -1
    for i in xrange(charIdx):
        endIdx = rawStr.find(endChar, endIdx + 1)
    return rawStr[:endIdx]
# end_func
