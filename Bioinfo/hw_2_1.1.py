#!/usr/bin/env python
#coding:utf8

"""
Author          :   Administrator
CreationDate    :   2016-09-01 17:20
Description     :
"""

import pdb

class ScoreParam:
    def __init__(self, match=2, mismatch=-1, gap=-1):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
    #end_init
#end_class

def GlobalAlign(x, y, score=ScoreParam(2, -1, -1)):
    """
    Do a global alignment between x and y
    """
    #create a zero-filled matrix to store simi score
    simiMatrix = MakeMatrix(len(x) + 1, len(y) + 1, isLocal=False, isTrace=False)

    #crease a matrix to store trace in every step, which can be more than one.
    traceMatrix = MakeMatrix(len(x) + 1, len(y) + 1, isLocal=False, isTrace=True)

    #fill in simiMatrix in the right order
    for i in xrange(1, len(y) + 1):
        for j in xrange(1, len(x) + 1):
            #the global alignment recurrance rule and get the trace:
            compareLis = [
                    (simiMatrix[i][j - 1] + score.gap, i, j - 1),
                    (simiMatrix[i - 1][j] + score.gap, i - 1, j),
                    (simiMatrix[i - 1][j - 1] + (score.match if x[i - 1] == y[j - 1] else score.mismatch), i - 1, j - 1)
                    ]
            maxSimi = max(compareLis, key=lambda x:x[0])[0]
            simiMatrix[i][j] = maxSimi
            tmpTrace = [(traceX, traceY) for simi, traceX, traceY in compareLis if simi == maxSimi]
            traceMatrix[i][j] = tmpTrace

    #display the whole trace
    displayTrace(traceMatrix, len(x), len(y), x, y)
#end_func

def displayTrace(traceMatrix, curX, curY, seqX, seqY, traceLis=[]):
    """
    turn trace matrix into a list which include the whole trace.(using recursion)
    """
    if curX == 0 and curY == 0:
        displayTraceLis(traceLis)
        return
    curLastPosLis = traceMatrix[curX][curY]
    for lastX, lastY in curLastPosLis:
        curStrX = '-' if lastX == curX else seqX[curX - 1]
        curStrY = '-' if lastY == curY else seqY[curY - 1]
        traceLis.append((curStrX, curStrY))
        displayTrace(traceMatrix, lastX, lastY, seqX, seqY, traceLis)
        traceLis.pop()
#end_func

def displayTraceLis(traceLis):
    for strX, strY in reversed(traceLis):
        print "%s <--------> %s" % (strX, strY)
    print "=" * 20
#end_func

def MakeMatrix(x, y, isLocal=False, isTrace=False):
    """
    construct a empty matrix with col = y and row = x
    """
    tmpMatrix = []
    for i in xrange(x):
        if isTrace:
            tmpMatrix.append([[]] * (y))
        else:
            tmpMatrix.append([0] * (y))

    if not isLocal:
        for i in xrange(1, x):
            tmpMatrix[0][i] = -i if not isTrace else [(i - 1, 0)]
            tmpMatrix[i][0] = -i if not isTrace else [(0, i - 1)]

    return tmpMatrix
#end_func

def hw_2():
    x = 'AACGGTA'
    y = 'ATCGGGT'
    isLocal = False
    xLen = len(x)
    yLen = len(y)
    GlobalAlign(x, y)
#end_func

def main():
    hw_2()
#end_main

if __name__ == "__main__":
   main()
#end_if

