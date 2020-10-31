# !/usr/bin/env python
# coding: utf-8
"""
tmp.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/23/2018, 11:44:07 PM
Link:
    
Description:
    
"""
from utils import readBinRecord

def func():
    fn = 'ref/record_000728.dat'
    userInfoDic, msgLis = readBinRecord(fn)
    print userInfoDic
    print msgLis[0]

# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
