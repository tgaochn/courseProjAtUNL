from copy import deepcopy
import sys


class Cell:
    def __init__(self, pos):
        self.point = pos
        self.x, self.y = self.point
        self.isAlive = False
    #end_func

    def setDead(self):
        self.isAlive = False
    #end_func

    def setAlive(self):
        self.isAlive = True
    #end_func
#end_class


class Game:
    def __init__(self, genNum, boardSize, initPointLis):
        self.boardSize = boardSize
        self.genNum = genNum
        self.aliveCellSet = set()
        self.aliveCellPosSet = set()
        self.board = self.initBoard()
        self.initAliveCell(initPointLis)
    #end_func

    def initBoard(self):
        board = []
        for px in xrange(self.boardSize):
            row = []
            for py in xrange(self.boardSize):
                row.append(Cell((px, py)))
            board.append(row)
        return board
    #end_func

    def initAliveCell(self, initPointLis):
        for px, row in enumerate(self.board):
            for py, cell in enumerate(row):
                if (px, py) in initPointLis:
                    self.setCellAlive(cell)
    #end_func

    def setCellAlive(self, cell):
        cell.setAlive()
        if cell.point not in self.aliveCellPosSet:
            self.aliveCellSet.add(cell)
            self.aliveCellPosSet.add(cell.point)
    #end_func

    def setCellDead(self, cell):
        cell.setDead()
        if cell.point in self.aliveCellPosSet:
            self.aliveCellSet.remove(cell)
            self.aliveCellPosSet.remove(cell.point)
    #end_func

    def getNeighbours(self, cell):
        cellAliveCnt = 0
        for offsetX in xrange(-1, 2):
            for offsetY in xrange(-1, 2):
                cellX, cellY = cell.x + offsetX, cell.y + offsetY
                if ((cellX, cellY) == cell.point) or (cellX < 0 or cellX >= self.boardSize) or (cellY < 0 or cellY >= self.boardSize):
                    continue
                if self.board[cellX][cellY].isAlive:
                    cellAliveCnt += 1
        return cellAliveCnt
    #end_func

    def gameStart(self):
        for _ in xrange(self.genNum):
            newBoard = deepcopy(self.board)
            for posX, row in enumerate(self.board):
                for poxY, _ in enumerate(row):
                    curCell = newBoard[posX][poxY]
                    neiCnt = self.getNeighbours(curCell)
                    if neiCnt == 3:
                        self.setCellAlive(curCell)
                    elif neiCnt != 2:
                        self.setCellDead(curCell)
            self.board = newBoard
    #end_func

    def outputCellAlive(self, outputFn):
        with open(outputFn, 'w') as outputObj:
            aliveCellLis = sorted(self.aliveCellSet)
            for cell in aliveCellLis:
                outputLine = '%s,%s' % (cell.x, cell.y)
                outputObj.write('%s\n' % outputLine)
    #end_func
#end_class

def main():
    # mpiSize = sys.argv[1] if len(sys.argv) >= 3 else None
    inputFn = sys.argv[1] if len(sys.argv) >= 2 else None
    outputFn = '%s.out' % inputFn

    # print sys.argv

    # inputFn = 'bricks'
    # inputFn = 'fifty'
    # outputFn = 'bricks.out'
    # outputFn = 'fifty.out'
    initPointLis = []

    # load input
    with open(inputFn) as inputObj:
        genNum = int(inputObj.readline())
        boardSize = int(inputObj.readline())
        for line in inputObj:
            px, _, py = line.strip().partition(',')
            initPointLis.append((int(px), int(py)))

    game = Game(genNum, boardSize, initPointLis)
    game.gameStart()
    game.outputCellAlive(outputFn)
#end_main

if __name__ == '__main__':
    main()
#end_if