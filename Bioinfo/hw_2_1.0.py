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
    #create a zero-filled matrix
    simiMatrix = MakeMatrix(len(x) + 1, len(y) + 1, isLocal=False)
    traceMatrix = MakeMatrix(len(x) + 1, len(y) + 1)
    traceLis = []

    #fill in simiMatrix in the right order
    for i in xrange(1, len(y) + 1):
        for j in xrange(1, len(x) + 1):
            #the global alignment recurrance rule and get the trace:
            compareLis = [
                    (simiMatrix[i][j - 1] + score.gap, (i, j - 1)),
                    (simiMatrix[i - 1][j] + score.gap, (i - 1, j)),
                    (simiMatrix[i - 1][j - 1] + (score.match if x[i - 1] == y[j - 1] else score.mismatch), (i - 1, j - 1)),
                    ]

            simiMatrix[i][j], traceMatrix[i][j] = max(compareLis, key=lambda x:x[0])
    #end_for
    i = len(x)
    j = len(y)
    while((i, j) != (0, 0)):
        lastPos = traceMatrix[i][j]
        traceLis.append((simiMatrix[i][j], lastPos))
        (i, j) = lastPos
    return traceLis
#end_func

def MakeMatrix(x, y, isLocal=False):
    """
    construct a empty matrix with col = y and row = x
    """
    A = []
    for i in xrange(x):
        A.append([0] * (y))

    if not isLocal:
        for i in xrange(1, x):
            A[0][i] = -i
            A[i][0] = -i
    return A
#end_func

def DisplayAlignment(x, y, traceLis):
    """
    display a global alignment between x and y
    """
    traceLis.reverse()
    traceLis.append((0, (len(x), len(y))))
    comStrX = ''
    comStrY = ''
    for idx, (simi, (i, j)) in enumerate(traceLis[:-1]):
        _, (next_i, next_j) = traceLis[idx + 1]
        comStrX += '-' if next_i == i else x[i]
        comStrY += '-' if next_j == j else y[j]
    print comStrX
    print comStrY
#end_func

def hw_2():
    x = 'AACGGTA'
    y = 'ATCGGGT'
    isLocal = False
    xLen = len(x)
    yLen = len(y)
    traceLis = GlobalAlign(x, y)
    DisplayAlignment(x, y, traceLis)
#end_func

def main():
    hw_2()
#end_main

if __name__ == "__main__":
   main()
#end_if

