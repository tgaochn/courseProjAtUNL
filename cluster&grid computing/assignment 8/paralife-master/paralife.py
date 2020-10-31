import sys
from sys import exit

sys.path.extend(r'C:\ProgramData\Anaconda2\pkgs\mpi4py-2.0.0-py27_1\Lib\site-packages')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpi4py import MPI


class Life:
    def __init__(self, comm, mpiSize, rank, genNum, boardSize, initPointLis):
        self.boardSize = boardSize
        self.comm = comm
        self.mpiSize = mpiSize
        self.rank = rank
        self.genNum = genNum
        self.grid = np.asfortranarray(np.zeros([boardSize, boardSize]))
        self.aug_grid = self.form_aug_grid(self.grid)

        for (px, py) in initPointLis:
            self.grid[px][py] = 1

        if mpiSize > 1:
            self.cols_per_proc = int(np.ceil(boardSize * 1.0 / self.mpiSize))
            self.proc_grid = np.random.choice(2, (boardSize + 2, self.cols_per_proc + 2))
            self.proc_grid[0, :] = self.proc_grid[boardSize, :]
            self.proc_grid[boardSize + 1, :] = self.proc_grid[1, :]
            self.proc_grid = np.asfortranarray(self.proc_grid)
            self.comm_ghosts()

        self.fig = plt.figure()
    # end_func

    def comm_ghosts(self):
        if (self.mpiSize > 1):
            recv_buf_ary = np.arange(self.boardSize + 2)
            [left_tag, right_tag, corner_tl_tag, corner_bl_tag, corner_tr_tag, corner_br_tag] = range(6)
            self.comm.Isend(np.array(self.proc_grid[:, 1]), dest=(self.rank - 1) % self.mpiSize, tag=left_tag)
            self.comm.Isend(np.array(self.proc_grid[:, self.cols_per_proc]), dest=(self.rank + 1) % self.mpiSize,
                            tag=right_tag)
            self.comm.Recv(recv_buf_ary, source=(self.rank - 1) % self.mpiSize, tag=right_tag)
            self.proc_grid[:, 0] = recv_buf_ary
            self.comm.Recv(recv_buf_ary, source=(self.rank + 1) % self.mpiSize, tag=left_tag)
            self.proc_grid[:, self.cols_per_proc + 1] = recv_buf_ary
    # end_func

    def form_aug_grid(self, a):
        return np.lib.pad(a, ((1, 1), (1, 1)), 'wrap')
    # end_func

    def neighbor_sum(self, row, col):
        return self.aug_grid[row + 2][col + 2] + self.aug_grid[row + 2][col + 1] + self.aug_grid[row + 2][col] + \
               self.aug_grid[row + 1][col + 2] + self.aug_grid[row + 1][col] + self.aug_grid[row][col + 2] + \
               self.aug_grid[row][col + 1] + self.aug_grid[row][col]
    # end_func

    def neighbor_sum_local(self, row, col):
        return self.proc_grid[row + 1][col + 1] + self.proc_grid[row + 1][col] + self.proc_grid[row + 1][col - 1] + \
               self.proc_grid[row][col + 1] + self.proc_grid[row][col - 1] + self.proc_grid[row - 1][col + 1] + \
               self.proc_grid[row - 1][col] + self.proc_grid[row - 1][col - 1]
    # end_func

    def update(self, i):
        for row, col in np.ndindex(self.grid.shape):
            if self.neighbor_sum(row, col) == 3:
                self.grid[row][col] = 1
            elif self.neighbor_sum(row, col) != 2:
                self.grid[row][col] = 0
        self.aug_grid = self.form_aug_grid(self.grid)
        plt.cla()
        return plt.imshow(self.grid, interpolation='nearest')
    # end_func

    def update_para_1d_dec_point_to_point(self, i):
        temp_grid = np.copy(self.proc_grid)
        for row in range(1, self.boardSize + 1):
            for col in range(1, self.cols_per_proc + 1):
                if self.neighbor_sum_local(row, col) == 3:
                    temp_grid[row][col] = 1
                elif self.neighbor_sum_local(row, col) != 2:
                    temp_grid[row][col] = 0
        self.proc_grid = temp_grid
        self.proc_grid[0, :] = self.proc_grid[self.boardSize, :]
        self.proc_grid[self.boardSize + 1, :] = self.proc_grid[1, :]
        self.comm.barrier()
        self.comm_ghosts()
        self.reconstruct_full_sim()
        plt.cla()
        return plt.imshow(self.grid, interpolation='nearest')
    # end_func

    def reconstruct_full_sim(self):
        send_buf_ary = np.asfortranarray(self.proc_grid[1:self.boardSize + 1, 1:(self.cols_per_proc + 2) - 1])
        recv_buf_ary = self.comm.gather(send_buf_ary, root=0)
        if (self.rank == 0):
            for proc in range(len(recv_buf_ary)):
                self.grid[:, proc * self.cols_per_proc:(proc + 1) * self.cols_per_proc] = recv_buf_ary[proc]
        self.grid = self.comm.bcast(self.grid, root=0)
    # end_func

    def update_para_1d_dec(self, i):
        for row in range(self.boardSize):
            if (row % self.mpiSize == self.rank):
                for col in range(self.boardSize):
                    if self.neighbor_sum(row, col) == 3:
                        self.grid[row][col] = 1
                    elif self.neighbor_sum(row, col) != 2:
                        self.grid[row][col] = 0

        for row in range(self.boardSize):
            self.grid[row] = self.comm.bcast(self.grid[row], root=row % self.mpiSize)

        if (self.rank == 0):
            self.aug_grid = self.form_aug_grid(self.grid)
        self.aug_grid = self.comm.bcast(self.aug_grid, root=0)

        plt.cla()
        return plt.imshow(self.grid, interpolation='nearest')
    # end_func

    def update_para_2d_dec(self, i):
        for row in range(self.boardSize):
            if (row % self.mpiSize == self.rank):
                for col in range(self.boardSize):
                    if self.neighbor_sum(row, col) == 3:
                        self.grid[row][col] = 1
                    elif self.neighbor_sum(row, col) != 2:
                        self.grid[row][col] = 0

        for row in range(self.boardSize):
            self.grid[row] = self.comm.bcast(self.grid[row], root=row % self.mpiSize)
        if (self.rank == 0):
            self.aug_grid = self.form_aug_grid(self.grid)
        self.aug_grid = self.comm.bcast(self.aug_grid, root=0)
        plt.cla()
        return plt.imshow(self.grid, interpolation='nearest')
    # end_func

    def show(self):
        plt.imshow(self.grid, interpolation='nearest')
        plt.show()
    # end_func

    def movie(self):
        anim = animation.FuncAnimation(self.fig, self.update, interval=10)
        plt.show()
    # end_func

    def movie_para(self):
        anim = animation.FuncAnimation(self.fig, self.update_para_1d_dec_point_to_point, interval=10)
        plt.show()
        # end_func
#end_class

def gol():
    # init
    inputFn = 'bricks'
    initPointLis = []
    comm = MPI.COMM_WORLD
    mpiSize = comm.Get_size()
    rank = comm.Get_rank()
    genNum = 0
    boardSize = 0

    # load input
    with open(inputFn) as inputObj:
        genNum = int(inputObj.readline())
        boardSize = int(inputObj.readline())
        for line in inputObj:
            px, _, py = line.strip().partition(',')
            initPointLis.append((int(px), int(py)))

    rowsPerProc = boardSize / mpiSize
    print mpiSize, rowsPerProc, int(boardSize * 1.0 / mpiSize)

    # running in serial mode or parallelled
    if (rowsPerProc != int(boardSize * 1.0 / mpiSize)):
        if (rank == 0):
            print "Matrix size not evenly divisible by number of processors. Use \
                different values."
            exit()
    elif (mpiSize > 1):
        if (rank == 0):
            print "Parallelizing with ", mpiSize, " processors."
    else:
        print "Running in serial mode."

    # init life class
    do_movie = True
    gol = Life(comm, mpiSize, rank, genNum, boardSize, initPointLis)

    gol.grid = comm.bcast(gol.grid, root=0)
    gol.aug_grid = gol.form_aug_grid(gol.grid)
    if (gol.mpiSize > 1):
        print rank, gol.proc_grid

    if (do_movie):
        if (mpiSize == 1):
            gol.movie()
        else:
            gol.movie_para()
    else:
        num_steps = 10
        for i in range(num_steps):
            gol.update_para_1d_dec_point_to_point(i)
            if (rank == 0):
                print rank, gol.grid


# end_func

if __name__ == "__main__":
    gol()
# end_main
