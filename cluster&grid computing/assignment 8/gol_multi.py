# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
ProjectName     :
Author          : Tian Gao
Email           : tgaochn@gmail.com
CreationDate    : 2017/11/7
Description     :
# move the following line to line 0 if running on Linux
"""

from copy import deepcopy

import sys
from mpi4py import MPI


def getInitBoard(boardSize):
    initBoard = []
    for _ in xrange(boardSize):
        # initBoard.append([False] * boardSize)
        initBoard.append([0] * boardSize)
    return initBoard
#end_func


def setInitAliveCell(board, initAlivePosLis):
    for (x, y) in initAlivePosLis:
        # board[x][y] = True
        board[x][y] = 1
    return board
#end_func


def displayCombBoard(combBoard):
    for (oriLineIdx, board3line) in combBoard:
        print oriLineIdx
        displayBoard(board3line)
#end_func


def displayBoard(board):
    for tmpLis in board:
        print ' '.join(map(lambda x:str(x), tmpLis))
#end_func

def encode(board, boardSize, commSize):
    """
    1 line structure to 3 line
    """
    encodedBoard = []
    for _ in xrange(commSize):
        encodedBoard.append([])

    cpBoard = deepcopy(board)
    for i in xrange(boardSize):
        idx = i % commSize
        if i == 0:
            encodedBoard[idx].append((i, [[-1] * boardSize, cpBoard[0], cpBoard[1]]))
        elif i == boardSize - 1:
            encodedBoard[idx].append((i, [cpBoard[boardSize - 2], cpBoard[boardSize - 1], [-1] * boardSize]))
        else:
            encodedBoard[idx].append((i, cpBoard[i - 1: i + 2]))
    return encodedBoard
#end_func


def decode(encodedBoard, boardSize):
    """
    3 line structure to 1 line
    """
    board = []
    for _ in xrange(boardSize):
        board.append([])

    for tmpLis1 in encodedBoard:
        for oriLineIdx, tmpLis2 in tmpLis1:
            board[oriLineIdx] = tmpLis2[1]

    return board
#end_func


def getNeighAliveCellCnt(line3Board, cellIdx):
    if cellIdx == 0:
        tmpLis = [line3Board[0][cellIdx], line3Board[0][cellIdx + 1], line3Board[1][cellIdx + 1], line3Board[2][cellIdx], line3Board[2][cellIdx + 1]]
    elif len(line3Board[0]) == cellIdx + 1:
        tmpLis = [line3Board[0][cellIdx - 1], line3Board[0][cellIdx], line3Board[1][cellIdx - 1], line3Board[2][cellIdx - 1], line3Board[2][cellIdx]]
    else:
        tmpLis = [line3Board[0][cellIdx - 1], line3Board[0][cellIdx], line3Board[0][cellIdx + 1], line3Board[1][cellIdx - 1], line3Board[1][cellIdx + 1], line3Board[2][cellIdx - 1], line3Board[2][cellIdx], line3Board[2][cellIdx + 1]]

    neighAliveCellCnt = len(filter(lambda x: x == 1, tmpLis))
    return neighAliveCellCnt
#end_func


def updateLocalBoard(localEncodedBoard):
    for boardIdx, (oriLine, line3Board) in enumerate(localEncodedBoard):
        oriLine3Board = deepcopy(line3Board)
        for cellIdx, targetCell in enumerate(line3Board[1]):
            neighAliveCellCnt = getNeighAliveCellCnt(oriLine3Board, cellIdx)
            if neighAliveCellCnt == 3:
                localEncodedBoard[boardIdx][1][1][cellIdx] = 1
            elif neighAliveCellCnt != 2:
                localEncodedBoard[boardIdx][1][1][cellIdx] = 0
    return localEncodedBoard
#end_func


def outputAliveCellPos(finalBoard, outputFn):
    with open(outputFn, 'w') as outputFileobj:
        for rowId, row in enumerate(finalBoard):
            for colId, item in enumerate(row):
                if item:
                    ouputLine = '%s,%s' % (rowId, colId)
                    outputFileobj.write('%s\n' % ouputLine)
#end_func


def multiNodeRun():
    inputFn = sys.argv[1] if len(sys.argv) >= 2 else None
    # inputFn = r'D:\Dropbox\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\assignment 8\gol_boards\test'
    inputFn = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\assignment 8\test\bricks'
    # inputFn = r'D:\Dropbox\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\assignment 8\gol_boards\input1'
    outputFn = '%s.out' % inputFn


    comm = MPI.COMM_WORLD
    commRank = comm.Get_rank()
    commSize = comm.Get_size()
    with open(inputFn) as fileobj:
        genCnt = int(fileobj.readline())
        boardSize = int(fileobj.readline())

    # init
    if commRank == 0:
        initAlivePosLis = []
        with open(inputFn) as fileobj:
            genCnt = int(fileobj.readline())
            boardSize = int(fileobj.readline())
            for line in fileobj:
                px, _, py = line.strip().partition(',')
                initAlivePosLis.append((int(px), int(py)))
        initBoard = getInitBoard(boardSize)
        initBoard = setInitAliveCell(initBoard, initAlivePosLis)
        displayBoard(initBoard)
        encodedBoard = encode(initBoard, boardSize, commSize)
    else:
        encodedBoard = None

    # update
    for i in range(genCnt):
        localEncodedBoard = comm.scatter(encodedBoard, root=0)
        localEncodedBoard = updateLocalBoard(localEncodedBoard)
        combineEncodedBoard = comm.gather(localEncodedBoard, root=0)
        if commRank == 0:
            combineBoard = decode(combineEncodedBoard, boardSize)
            print '==' * 20
            displayBoard(combineBoard)
            encodedBoard = encode(combineBoard, boardSize, commSize)

            # output
            finalBoard = decode(encodedBoard, boardSize)
            outputAliveCellPos(finalBoard, outputFn)
#end_func


def main():
    multiNodeRun()
#end_main


if __name__ == "__main__":
    main()
#end_if
