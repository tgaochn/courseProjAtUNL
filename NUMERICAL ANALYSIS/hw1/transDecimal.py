#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName:

Author:
    Tian Gao
Email:
    tgaochn@gmail.com
CreationDate:
    1/14/2018
Description:

"""
import bitarray
import supp
import re


def int2bin(decNum):
    intPart = int(decNum)
    fracPart = decNum - intPart
    fracBin = supp.pureFrac2bitarray(fracPart)
    intBin = supp.int2bitarray(intPart)
    offset = len(intBin) - 1

    s = 1 if decNum < 0 else 0
    E = 127 + offset
    binM = intBin[1:] + fracBin

    binS = supp.int2bitarray(s)
    binE = supp.int2bitarray(E)
    binM = supp.expend2len(binM, 23)

    print s, E
    print binS, binE, binM
    print binS + binE + binM
#end_func


def bin2int(binStr):
    binStr = binStr.replace(' ', '')
    binS = binStr[0]
    binE = binStr[1:9]
    binM = binStr[9:]

    s = int(binS, 2)
    E = int(binE, 2)

    print s, E, binM

    offset = E - 127

    expLis = [offset] + [offset - (m.start() + 1) for m in re.finditer('1', binM)]
    decNum = (-1)**s * sum([2**x for x in expLis])
    print decNum
#end_func


def func():
    # int2bin(33.015625)
    # int2bin(32.015725)
    # bin2int('0 10000101 11111100000000000000000')
    # bin2int('0 10000100 00001000001000000000000')

    supp.formatPrint('00110000100010010111000001011111')
#end_func

def main():
    func()
#end_main

if __name__ == "__main__":
    main()
#end_if
