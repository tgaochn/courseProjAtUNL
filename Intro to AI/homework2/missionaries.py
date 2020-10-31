#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName     : 
Author          : Tian Gao
CreationDate    : 2017/9/9
Description     :

"""

import itertools

class PeopleStat:
    """
    a class shows how many Missionaries and Cannibals are in each bank
    """
    def __init__(self, oriBankPeopCnt, goalBankPeopCnt):
        self.peopCntLis = [oriBankPeopCnt, goalBankPeopCnt]
        self.totalCnt = oriBankPeopCnt + goalBankPeopCnt
    #end_func
#end_class

def BoatMove(curMisStat, curCanStat, fromBank, misOnBoard, canOnBoard):
    """
    return how many Missionaries and Cannibals are in each bank after the boat move
    :param curMisStat: how many Missionaries are in each bank before move
    :param curCanStat: how many Cannibals are in each bank before move
    :param fromBank: which bank the boat moves from
    :param misOnBoard: how many Missionaries on board
    :param canOnBoard: how many Cannibals on board
    """
    newMisStat = PeopleStat(curMisStat.peopCntLis[0] + (-1) ** (fromBank + 1) * misOnBoard, curMisStat.peopCntLis[1] + (-1) ** fromBank * misOnBoard)
    newCanStat = PeopleStat(curCanStat.peopCntLis[0] + (-1) ** (fromBank + 1) * canOnBoard, curCanStat.peopCntLis[1] + (-1) ** fromBank * canOnBoard)
    return newMisStat, newCanStat
#end_func

def IsStatSafe(misStat, canStat):
    """
    whether or not the current status is safe
    """
    misCnt0 = misStat.peopCntLis[0]
    canCnt0 = canStat.peopCntLis[0]
    misCnt1 = misStat.peopCntLis[1]
    canCnt1 = canStat.peopCntLis[1]
    isSafe = (canCnt0 >= misCnt0 or canCnt0 == 0) and (canCnt1 >= misCnt1 or canCnt1 == 0)
    return isSafe
#end_func

def IsEnd(misStat, canStat):
    """
    whether or not all the people have been moved to the goal bank
    """
    rlt = misStat.peopCntLis[1] == misStat.totalCnt and canStat.peopCntLis[1] == canStat.totalCnt
    return rlt
#end_func

def ShowRlt(statHist):
    for id, (boatPos, misStat, canStat) in enumerate(statHist):
        print id + 1, misStat, canStat
    print "==" * 10
#end_func

def SolvePuzzle(curMisStat, curCanStat, boatPos, statHist):
    if IsEnd(curMisStat, curCanStat): ShowRlt(statHist)
    possiblePeopOnBoard = (0, 1, 2)

    for misOnBoard, canOnBoard in itertools.product(possiblePeopOnBoard, repeat=2):
        isValidPeopOnBoard = 0 < misOnBoard + canOnBoard <= 2
        if not isValidPeopOnBoard: continue

        isValidPeopOnBank = curMisStat.peopCntLis[boatPos] - misOnBoard >= 0 and curCanStat.peopCntLis[boatPos] - canOnBoard >= 0
        if not isValidPeopOnBank: continue

        newMisStat, newCanStat = BoatMove(curMisStat, curCanStat, boatPos, misOnBoard, canOnBoard)
        newBoatPos = 1 - boatPos
        isDuplicateStep = statHist and (newBoatPos, newMisStat.peopCntLis, newCanStat.peopCntLis) in statHist # repeated steps are not allowed
        if not isDuplicateStep and IsStatSafe(newMisStat, newCanStat):
            SolvePuzzle(newMisStat, newCanStat, newBoatPos, statHist + [(newBoatPos, newMisStat.peopCntLis, newCanStat.peopCntLis)])
#end_func

def missionaries():
    totalMisCnt = 3
    totalCanCnt = 3

    misStat = PeopleStat(totalMisCnt, 0)
    canStat = PeopleStat(totalCanCnt, 0)
    boatPos = 0
    statHis = [(boatPos, misStat.peopCntLis, canStat.peopCntLis)]
    SolvePuzzle(misStat, canStat, boatPos, statHis)
#end_test

def main():
    missionaries()
#end_main

if __name__ == "__main__":
    main()
#end_if
