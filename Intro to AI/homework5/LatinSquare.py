#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName     : 
Author          : Tian Gao
CreationDate    : 2017/10/20
Description     :

"""
ALL_ASSIGN = ['r', 'g', 'b', 'y']
ASSIGNMENT = [(0, 0, 'r'), (1, 0, 'g'), (2, 0, 'b'), (3, 0, 'y'), (0, 1, 'g'), (1, 1, 'y'), (0, 2, 'b')]
ASSIGN_DIC = {}

def init():
    initMat = []
    for i in xrange(4):
        initMat.append([['r', 'g', 'b', 'y'], ['r', 'g', 'b', 'y'], ['r', 'g', 'b', 'y'], ['r', 'g', 'b', 'y']])
    return initMat
#end_func


def assignVal(x, y, val):
    ASSIGN_DIC[(x, y)] = val
#end_func


def partialConsistCheck(availMat, x, y, val, type='partial'):
    if type == 'partial':
        assignVal(x, y, val)
        for i in xrange(4):
            if val in availMat[i][x] and len(availMat[i][x]) > 1:
                availMat[i][x].remove(val)
            if val in availMat[y][i] and len(availMat[y][i]) > 1:
                availMat[y][i].remove(val)
        return availMat
    elif type == 'full':
        assignVal(x, y, val)
        for i in xrange(4):
            if val in availMat[i][x] and len(availMat[i][x]) > 1:
                availMat[i][x].remove(val)
            if val in availMat[y][i] and len(availMat[y][i]) > 1:
                availMat[y][i].remove(val)

        for x in xrange(4):
            for y in xrange(4):
                if (x, y) not in ASSIGN_DIC and len(availMat[y][x]) == 1:
                    availMat = partialConsistCheck(availMat, x, y, availMat[y][x][0], 'full')

        return availMat
#end_func


def getOnlyValPos(availMat):
    for x in xrange(4):
        for y in xrange(4):
            if len(availMat[x][y]) == 1 and (y, x) not in ASSIGN_DIC:
                return y, x, availMat[x][y][0]
#end_func


def showCell(availMat, x, y):
    if (x, y) in ASSIGN_DIC:
        return ASSIGN_DIC[(x, y)]
    else:
        cellLis = availMat[y][x]
        cellLis = [curVal if curVal in cellLis else '\_' for curVal in ALL_ASSIGN]
        rtn = '$\\begin{matrix}   %s & %s \\\\   %s & %s  \\end{matrix}$' % (cellLis[0], cellLis[1], cellLis[2], cellLis[3])
        return rtn
#end_func


def displayAvailMat(availMat):
    print '\\begin{tabular}{|l|l|l|l|}'
    print '\\hline'
    print '%s & %s & %s & %s \\\\ \\hline' % (showCell(availMat, 0, 0), showCell(availMat, 1, 0), showCell(availMat, 2, 0), showCell(availMat, 3, 0))
    print '%s & %s & %s & %s \\\\ \\hline' % (showCell(availMat, 0, 1), showCell(availMat, 1, 1), showCell(availMat, 2, 1), showCell(availMat, 3, 1))
    print '%s & %s & %s & %s \\\\ \\hline' % (showCell(availMat, 0, 2), showCell(availMat, 1, 2), showCell(availMat, 2, 2), showCell(availMat, 3, 2))
    print '%s & %s & %s & %s \\\\ \\hline' % (showCell(availMat, 0, 3), showCell(availMat, 1, 3), showCell(availMat, 2, 3), showCell(availMat, 3, 3))
    print '\\end{tabular}\\\\\\\\'
#end_func


def latinSequare():
    checkType = 'full'
    availMat = init()
    for x, y, val in ASSIGNMENT:
        availMat = partialConsistCheck(availMat, x, y, val, checkType)
        displayAvailMat(availMat)
    while len(ASSIGN_DIC) < 16:
        x, y, val = getOnlyValPos(availMat)
        availMat = partialConsistCheck(availMat, x, y, val, checkType)
        displayAvailMat(availMat)
#end_test

def main(): 
    latinSequare()
#end_main

if __name__ == "__main__":
    main()
#end_if
