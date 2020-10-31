# -*- coding: utf-8 -*-
"""
ProjectName     :
Author          : Tian Gao
Email           : tgaochn@gmail.com
CreationDate    : 2018/1/16
Description     :
# move the following line to line 0 if running on Linux
#!/usr/bin/env python

"""
import bitarray


def bin2int(x):
    return bitarray2int(bitarray.bitarray(x))
#end_func


def bitarray2int(x):
    """
    convert from bitarray to int
    """
    return int(bitarray.bitarray.to01(x), 2)
#end_func

def int2bitarray(x):
    """
    convert from int to bitarray
    """
    return bitarray.bitarray(bin(x)[2:])
#end_func


def pureFrac2bitarray(x):
    """
    convert from pure fraction to bitarray
    """
    fracBase = 0
    while int(x) != x:
        x *= 2
        fracBase += 1
    fracBin = bitarray.bitarray('0' * (fracBase - 1)) + int2bitarray(int(x))
    return fracBin
#end_func


def expend2len(oriBitarray, targetLen):
    return oriBitarray + bitarray.bitarray('0' * (targetLen - len(oriBitarray)))
#end_func


def formatPrint(x):
    print '%s %s %s' % (x[0], x[2:9], x[9:])
#end_func


def func():
    # print pureFrac2bitarray(0.015625)
    print bin2int('10000010')
#end_func

def main():
    func()
#end_main

if __name__ == "__main__":
    main()
#end_if
