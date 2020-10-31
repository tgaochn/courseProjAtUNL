# !/usr/bin/env python
# coding: utf-8
"""
utils.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/25/2018, 2:39:53 PM
Link:
    
Description:
    
"""


def dataParser(data, method='original'):
    if method == 'original':
        return data
    elif method == 'datetimeHour':
        datetimeFormat = '%Y/%m/%d %H:%M'
        datetimeObject = datetime.strptime(data, datetimeFormat)
        return datetimeObject.hour
# end_func
