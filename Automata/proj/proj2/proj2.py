#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName     : ''
Author          : 'Tian Gao'
CreationDate    : '2016/11/23'
Description     :

"""
import copy
import sys

ACCEPTSTRING = 'M stops and accepts w'
REJECTSTRING = 'M stops and rejects w'
LOOPSTRING = 'M is still running'

class Tape():
    def __init__(self, inputStr):
        inputStr = '' if inputStr == 'e' else inputStr
        self.tapeLis = list(inputStr) + ['_']
        self.curChar = self.tapeLis[0]
        self.curPointer = 0
    #end_init

    def updateTape(self, newChar, direction):
        self.tapeLis[self.curPointer] = newChar
        if direction == 'R': self.curPointer += 1
        if direction == 'L' and self.curPointer > 0: self.curPointer -= 1
        if len(self.tapeLis) == self.curPointer: self.tapeLis.append('_')
        self.curChar = self.tapeLis[self.curPointer]
    #end_func
#end_class

def test():
    for i in range(1, 11):
        questionFileNm = 'data/q%s.txt' % i
        answerFileNm = 'data/a%s.txt' % i
        print questionFileNm
        with open(questionFileNm) as curFile:
            transLis, inputStr = LoadData(curFile)
            # print transLis, inputStr
            transDict, stateSet = ParseTrans(transLis)
            curTape = Tape(inputStr)
            rlt = SimilateTM('q0', curTape, transDict)
            encodingStr = "#%s#" % '#'.join(transLis)
            transNum = len(transLis)
            stateNum = len(stateSet)
            checkRlt = CheckRlt(answerFileNm, encodingStr, inputStr, transNum, stateNum, rlt)
            print checkRlt
            print '=' * 40
#end_test

def ConstructAndSimilateTM():
    transLis, inputStr = LoadData(sys.stdin)
    transDict, stateSet = ParseTrans(transLis)
    curTape = Tape(inputStr)
    rlt = SimilateTM('q0', curTape, transDict)
    encodingStr = "#%s#" % '#'.join(transLis)
    transNum = len(transLis)
    stateNum = len(stateSet)
    PrintRlt(encodingStr, inputStr, transNum, stateNum, rlt)
#end_func

def PrintRlt(encodingStr, inputStr, transNum, stateNum, rlt):
    print encodingStr
    print inputStr
    print transNum
    print stateNum
    print rlt
#end_func

def CheckRlt(answerFileNm, encodingStr, inputStr, transNum, stateNum, rlt):
    items = (encodingStr, inputStr, transNum, stateNum, rlt)
    with open(answerFileNm) as answerFile:
        for lineIdx, line in enumerate(answerFile):
            line = line.strip()
            if not line: continue
            item = items[lineIdx]
            print line
            print item
            if str(item) != line:return 'Wrong!!'
    return 'Correct!!'
#end_func

def LoadData(input):
    line = input.readline().strip().strip('#')
    transStr, _, inputStr = line.partition('##')
    transLis = transStr.split('#')
    return transLis, inputStr
#end_func

def ParseTrans(TransLis):
    transDict = {}
    stateSet = set()
    for curTrans in TransLis:
        transStart, transEnd = curTrans.split('->')
        transStartState, transStartChar = transStart.split(',')
        transEndState, transEndChar, tapeDirection = transEnd.split(',')
        transDict.setdefault((transStartState, transStartChar), [])
        transDict[(transStartState, transStartChar)].append((transEndState, transEndChar, tapeDirection))
        stateSet.add(transStartState)
        stateSet.add(transEndState)
    return transDict, stateSet
#end_func

def SimilateTM(curState, curTape, transDict, callCnt=0):
    # print curState, curTape.curChar, curTape.tapeLis
    if curState == 'qa': return ACCEPTSTRING
    if curState == 'qr': return REJECTSTRING
    if callCnt >= 20: return LOOPSTRING
    curChar = curTape.curChar
    if (curState, curChar) not in transDict: return False
    nextItemLis = transDict[(curState, curChar)]
    rltLis = []
    for (nextState, newChar, tapeDirection) in nextItemLis:
        newTape = copy.deepcopy(curTape)
        newTape.updateTape(newChar, tapeDirection)
        rlt = SimilateTM(nextState, newTape, transDict, callCnt + 1)
        if rlt == ACCEPTSTRING: return ACCEPTSTRING
        rltLis.append(rlt)
    if LOOPSTRING in rltLis:return LOOPSTRING
    return REJECTSTRING
#end_func

def main():
    # test()
    ConstructAndSimilateTM()
#end_main

if __name__ == "__main__":
    main()
#end_if
