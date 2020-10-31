#!/usr/bin/env python
#coding:utf8

"""
Author          :   Administrator
CreationDate    :   2016-09-05 17:02
Description     :
    This program is for hw #3.2-1.
    It can be used to calculate the coding potential of DNA sequence using di-codon preference model, given di-codon frequencies.
    It can also prodict if the region is a coding region or not.
"""

import pdb
import copy
import math

def InitDic():
    """
    initialize dictory of sequences frequencies.
    Key : 2 triplet
    value : (freq of coding, freq of non-coding)
    """
    tmpDic = {}
    tmpDic[('ACT', 'GGG')] = (0.01, 0.0001)
    tmpDic[('ATC', 'CGT')] = (0.001, 0.0001)
    tmpDic[('CTG', 'GGA')] = (0.002, 0.001)
    tmpDic[('GAT', 'CCG')] = (0.008, 0.001)
    tmpDic[('GGA', 'TCC')] = (0.01, 0.0001)
    tmpDic[('GGG', 'ATC')] = (0.001, 0.001)
    tmpDic[('TGG', 'GAT')] = (0.0005, 0.0001)

    return tmpDic
#end_func

def SpliceSeq(seq):
    """
    cut sequence into triplet list of each open reading frame.
    input : DNA sequence
    output : list of ORF
    """
    tmpSeq = copy.deepcopy(seq) # nomal copy does not work!
    ORFLis = [[], [], []]
    for i in range(3):
        tmpSeq = tmpSeq[i:]
        while len(tmpSeq) >= 6:
            curTriPair = tmpSeq[:6]
            tri1, tri2 = curTriPair[:3], curTriPair[3:]
            ORFLis[i].append((tri1, tri2))
            tmpSeq = tmpSeq[1:]
        tmpSeq = copy.deepcopy(seq) # nomal copy does not work!
    return ORFLis
#end_func

def CalcScore(ORFLis, freqDic):
    """
    calculate the probility of coding and non-coding region.
    input : Triplet list; probility dict of each triplet pair
    output : score of each open reading frame
    """
    ORFScoreLis = []
    for curORF in ORFLis:
        sumScore = 0
        for tri1, tri2 in curORF:
            curFC, curFN = freqDic[(tri1, tri2)] #coding prob and non-coding prob
            score = math.log(curFC / curFN, 2)
            sumScore += score
        ORFScoreLis.append((curORF, sumScore))
    return ORFScoreLis
#end_func

def DisplayRlt(seq, ORFScoreLis, onlyDispFirst=True):
    """
    make a prediction and display whether the DNA sequence is coding region or not.
    input : DNA sequence; a list include ORF and its score; only display the first ORF or not
    output : None
    """
    if onlyDispFirst: ORFScoreLis = ORFScoreLis[:1] # whether use the first ORF only!
    for curORFScore in ORFScoreLis:
        curORF, curScore = curORFScore
        rlt = 'Non-coding' if curScore < 0 else 'coding'
        print 'The DNA sequence : %s' % seq
        print 'ORF : %s' % curORF
        print 'score : %s' % curScore
        print 'prediction result: %s region' % rlt
#end_func

def hw_3():
    initSeq = 'ACTGGGATCCGT'
    freqDic = InitDic()
    ORFLis = SpliceSeq(initSeq)
    ORFScoreLis = CalcScore(ORFLis, freqDic)
    DisplayRlt(initSeq, ORFScoreLis)
#end_func

def main():
    hw_3()
#end_main

if __name__ == "__main__":
   main()
#end_if

