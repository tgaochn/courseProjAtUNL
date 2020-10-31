#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName:

Author:
    Tian Gao
Email:
    tgaochn@gmail.com
CreationDate:
    10/8/2017
Description:

"""
import heapq
import random
import copy

import time

allStateLis = []
allNodeLis = []
nnv = 0

class State:
    def __init__(self, digitLis):
        """
        :param digitLis:
            a 1D-array to store all the digit
        :param distType:
            Displaced or Manhattan
        """
        self.digit2pos = {}
        self.pos2digit = {}

        for digitIdx, digit in enumerate(digitLis):
            x, y = listIdx2pos(digitIdx)
            self.digit2pos[digit] = (x, y)
            self.pos2digit[(x, y)] = digit

        self.neighborsLis = []
        self.h = None
        self.visited = False
    #end_func
#end_class


class Node:
    def __init__(self, parentNode, state, dirction):
        self.state = state
        self.parentNode = parentNode
        self.childrenNodeLis = []
        self.pathValue = 0 if not parentNode else parentNode.pathValue + 1
        self.dirctionFromParent = dirction
    #end_func
#end_class


def listIdx2pos(listIdx):
    x = listIdx % 3
    y = listIdx / 3
    return x, y
#end_func


def digit2goalPos(digit):
    """
    get the pos of inputted digit in goal state
    """
    x = 0
    y = 0
    if digit == ' ': return x, y
    x = digit % 3
    y = digit / 3
    return x, y
#end_func


def getSingleTileManhDist(digit, x, y):
    """
    get Manhattan distance for a single tile
    """
    goalX, goalY = digit2goalPos(digit)
    dist = abs(x - goalX) + abs(y - goalY)
    return dist
#end_func


def getGoalDist(state, distType='Displaced'):
    dist = None
    if distType == 'Displaced':
        dist = 0
        for digit, (x, y) in state.digit2pos.iteritems():
            if digit == ' ':
                if x != 0 or y != 0: dist = 1 if not dist else dist + 1
            else:
                if y * 3 + x != int(digit): dist = 1 if not dist else dist + 1
    elif distType == 'Manhattan':
        for digit, (x, y) in state.digit2pos.iteritems():
            if digit == ' ':continue
            dist = getSingleTileManhDist(digit, x, y) if not dist else dist + getSingleTileManhDist(digit, x, y)
    return dist
#end_func


def updateStateNeigAndHeur(state, distType):
    dirctionLis = ['north', 'south', 'east', 'west']
    for dirction in dirctionLis:
        newState = getStateAfterMove(state, dirction, distType)
        if newState: state.neighborsLis.append((newState, dirction))

    state.h = getGoalDist(state, distType)
# end_func


def stateGen(mode='rand', digitLis=None, distType='Manhattan'):
    state = None
    if mode == 'given' and digitLis:
        state = State(digitLis)
    else:
        if mode == 'rand':
            digitLis = range(9)
            digitLis[0] = ' '
            state = State(digitLis)
            moveCnt = int(random.random() * 25)
            for i in xrange(moveCnt):
                moveDirection = random.sample(['north', 'south', 'east', 'west'], 1)[0]
                newState = getStateAfterMove(state, moveDirection, distType, updateH=False)
                if newState: state = newState
        elif mode == 'goal':
            digitLis = range(9)
            digitLis[0] = ' '
            state = State(digitLis)
    if state:
        updateStateNeigAndHeur(state, distType)
        allStateLis.append(state)
    return state
#end_func


def getStateAfterMove(state, moveDirection, distType, updateH=True):
    """
    move the empty tile to 4 direction
    :param moveDirection:
        north, south, east and west
    """
    x, y = state.digit2pos[' ']
    if not isMoveValid(x, y, moveDirection): return None
    newX, newY = getNewPos(x, y, moveDirection)
    digitToExchange = state.pos2digit[(newX, newY)]

    newState = copy.deepcopy(state)
    newState.visited = False
    newState.pos2digit[(x, y)] = digitToExchange
    newState.pos2digit[(newX, newY)] = ' '
    newState.digit2pos[digitToExchange] = (x, y)
    newState.digit2pos[' '] = (newX, newY)
    newState.neighborsLis = []
    if updateH: newState.h = getGoalDist(newState, distType)

    # print '=' * 10
    # print moveDirection
    # dispState(newState)

    return newState
#end_func


def getNewPos(x, y, moveDirection):
    if moveDirection == 'north':
        y -= 1
    elif moveDirection == 'south':
        y += 1
    elif moveDirection == 'west':
        x -= 1
    elif moveDirection == 'east':
        x += 1
    return x, y
#end_func


def isMoveValid(x, y, moveDirection):
    rtn = True
    if y == 0 and moveDirection == 'north':
        rtn = False
    elif y == 2 and moveDirection == 'south':
        rtn = False
    elif x == 0 and moveDirection == 'west':
        rtn = False
    elif x == 2 and moveDirection == 'east':
        rtn = False
    return rtn
#end_func


def expandNode(curNode, distType):
    global nnv
    nnv += 1
    curNode.state.visited = True
    if not curNode.state.neighborsLis:
        updateStateNeigAndHeur(curNode.state, distType)
    for (state, dirction) in curNode.state.neighborsLis:
        childNode = Node(curNode, state, dirction)
        allNodeLis.append(childNode)
        curNode.childrenNodeLis.append(childNode)
    return curNode.childrenNodeLis
#end_func


def evaluateNode(node, distType='Displaced'):
    f = node.pathValue + getGoalDist(node.state, distType)
    return f
#end_func


def isGoal(curNode, goalState):
    rlt = False
    if curNode.state.pos2digit == goalState.pos2digit: rlt = True
    return rlt
#end_func


def search(initState, goalState, distType):
    """
    use heap to store frontiers so that the node with minimized cost(which is also the node to be expanded) is on the top
    :param distType:
        Displaced or Manhattan
    """
    frontierHeap = []
    heapq.heapify(frontierHeap)
    startNode = Node(None, initState, None)
    allNodeLis.append(startNode)
    startNodeF = evaluateNode(startNode, distType)
    heapq.heappush(frontierHeap, (startNodeF, startNode))

    # iteratively update the heap and fetch the top node
    while frontierHeap:
        expandNodeCost, nodeToExpand = heapq.heappop(frontierHeap)
        if isGoal(nodeToExpand, goalState):
            return nodeToExpand
        if nodeToExpand.state.visited:continue
        newFronterNodeLis = expandNode(nodeToExpand, distType)
        for newFronterNode in newFronterNodeLis:
            newNodeCost = evaluateNode(newFronterNode, distType)
            heapq.heappush(frontierHeap, (newNodeCost, newFronterNode))
#end_func


def fetchPath(goalNode, dispMidStates=False):
    directionLis = []
    stateLis = []
    curNode = goalNode
    while curNode.parentNode:
        directionLis.append(curNode.dirctionFromParent)
        stateLis.append(curNode.state)
        curNode = curNode.parentNode
    directionLis.reverse()
    stateLis.reverse()

    if dispMidStates:
        print 'all the middle states:'
        for state in stateLis:
            print '==' * 10
            dispState(state)

    return ' - '.join(directionLis)
#end_func


def dispState(state):
    # print '=' * 10
    for y in xrange(3):
        print '%s %s %s' % (state.pos2digit[(0, y)], state.pos2digit[(1, y)], state.pos2digit[(2, y)])
    # print '=' * 10
#end_func


def clearStateAndNode():
    for idx, state in enumerate(allStateLis):
        del allStateLis[idx]

    for idx, node in enumerate(allNodeLis):
        del allNodeLis[idx]
#end_func


def eight_PiecesLidingPuzzle():
    global nnv
    testLis = [1, 2, 5, 3, 4, 8, ' ', 6, 7]

    combinationsCnt = 10
    for i in xrange(combinationsCnt):
        startTime = time.clock()

        # initState = stateGen('given', testLis, distType)
        initState = stateGen(mode='rand')
        goalState = stateGen(mode='goal')
        initStateCopy = copy.deepcopy(initState)
        goalStateCopy = copy.deepcopy(goalState)

        print 'initial state'
        dispState(initState)
        print 'goal state'
        dispState(goalState)

        # use Manhattan distance
        nnv = 0
        distType = 'Manhattan'
        goalNode = search(initState, goalState, distType)
        pathStr = fetchPath(goalNode)
        print 'distance type: %s' % distType
        print 'movement list: %s' % pathStr

        print '#nodes visited: %s' % nnv
        print 'Total cost of path: %s' % goalNode.pathValue

        elapsed = (time.clock() - startTime)
        print 'time cost: %s sec' % elapsed

        nnv1 = copy.deepcopy(nnv)
        pathCost1 = copy.deepcopy(goalNode.pathValue)
        cpuTime1 = copy.deepcopy(elapsed)

        # use Displaced tile
        clearStateAndNode()
        nnv = 0
        distType = 'Displaced'
        goalNode = search(initStateCopy, goalStateCopy, distType)
        pathStr = fetchPath(goalNode)
        print 'distance type: %s' % distType
        print 'movement list: %s' % pathStr

        print '#nodes visited: %s' % nnv
        print 'Total cost of path: %s' % goalNode.pathValue

        elapsed = (time.clock() - startTime)
        print 'time cost: %s sec' % elapsed

        nnv2 = copy.deepcopy(nnv)
        pathCost2 = copy.deepcopy(goalNode.pathValue)
        cpuTime2 = copy.deepcopy(elapsed)

        # output formatted table for latex
        matrixLatexStr = '$\\begin{matrix} %s & %s & %s \\\\ %s & %s & %s \\\\ %s & %s & %s \\end{matrix}$' \
                         % (initStateCopy.pos2digit[(0, 0)], initStateCopy.pos2digit[(1, 0)], initStateCopy.pos2digit[(2, 0)],
                            initStateCopy.pos2digit[(0, 1)], initStateCopy.pos2digit[(1, 1)], initStateCopy.pos2digit[(2, 1)],
                            initStateCopy.pos2digit[(0, 2)], initStateCopy.pos2digit[(1, 2)], initStateCopy.pos2digit[(2, 2)],)
        print 'latex table code:'
        print '%s & %s & %s & %.2f sec & %s & %s & %.2f sec \\\\ \\hline' % (matrixLatexStr, nnv1, pathCost1, cpuTime1, nnv2, pathCost2, cpuTime2)


#end_func

def main():
    eight_PiecesLidingPuzzle()
#end_main

if __name__ == "__main__":
    main()
#end_if
