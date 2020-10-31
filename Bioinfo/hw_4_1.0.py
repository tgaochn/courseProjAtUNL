#!/usr/bin/env python
#coding:utf8

"""
Author          :   Administrator
CreationDate    :   2016-9-20 20:57:55
Description     :
"""

import pdb
import math

def CalSingleInfoContent(string):
    """
    calculate information content of a string
    """
    cntDic = {}
    stringLen = len(string)
    IC = 0
    for letter in string:
        cntDic.setdefault(letter, 0)
        cntDic[letter] += 1
    for letter, cnt in cntDic.iteritems():
        prob = cnt * 1.0 / stringLen
        IC += prob * math.log(prob / 0.25, 10)
    return IC
#end_func

def CalLisInfoContent(seqLis):
    """
    calculate information content of several sequences
    """
    ICLis = []
#    pdb.set_trace()
    for idxY in range(len(seqLis[0])):
        stringInPos = ''
        for idxX in range(len(seqLis)):
            letter = seqLis[idxX][idxY]
            stringInPos += letter
        ICInPos = CalSingleInfoContent(stringInPos)
        ICLis.append(ICInPos)
    return ICLis
#end_func

def hw_4():
    seq = "TGATCGTTTTGACAAAAATG \n AGCACGGCGTCACACTTTGC \n CAAGGTACGTCAGATGACCG \n TATTTCCTCTCACTCTCTTT \n \
    GAACAAAGATCACACAAAGC \n TGGCGGTGTTGACACTGGTA"
    seqLis = seq.split()
    ICLis = CalLisInfoContent(seqLis)
    for idx, IC in enumerate(ICLis):
        print idx + 1, IC
#end_func

def main():
    hw_4()
#end_main

if __name__ == "__main__":
   main()
#end_if


