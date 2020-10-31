# -*- coding: utf-8 -*-
"""
ProjectName     :
Author          : Tian Gao
Email           : tgaochn@gmail.com
CreationDate    : 2017/11/5
Description     :
# move the following line to line 0 if running on Linux
#!/usr/bin/env python
"""
from mpi4py import MPI
import sys
import os
# import numpy as np

def fun1():
    """
    mpiexec -np 4 python mpiTest.py

    Hello, World! I am process 2 of 4 on USER-QV4U343P39.
    Hello, World! I am process 1 of 4 on USER-QV4U343P39.
    Hello, World! I am process 0 of 4 on USER-QV4U343P39.
    Hello, World! I am process 3 of 4 on USER-QV4U343P39.
    """
    size = MPI.COMM_WORLD.Get_size()
    rank = MPI.COMM_WORLD.Get_rank()
    name = MPI.Get_processor_name()

    print "Hello, World! I am process %d of %d on %s.\n" % (rank, size, name)
#end_func

def fun2():
    """
    node2node: sender and receiver must be identified
    !!cannot run on a single node!!

    mpiexec - np 4 python mpiTest.py

    my rank is 1, and Ireceived:
    [0, 0, 0, 0, 0]
    my rank is 2, and Ireceived:
    [1, 1, 1, 1, 1]
    my rank is 0, and Ireceived:
    [3, 3, 3, 3, 3]
    my rank is 3, and Ireceived:
    [2, 2, 2, 2, 2]
    """
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()

    # point to point communication
    data_send = [comm_rank] * 5
    comm.send(data_send, dest=(comm_rank + 1) % comm_size)
    data_recv = comm.recv(source=(comm_rank - 1) % comm_size)
    print("my rank is %d, and Ireceived: %s" % (comm_rank, data_recv))
#end_func


def mpiNode2nodeComm():
    """
    node2node: sender and receiver must be identified and send/recv order is set to avoid being stuck
    !!cannot run on a single node!!

    mpiexec - np 4 python mpiTest.py

    my rank is 1, and Ireceived:
    [0, 0, 0, 0, 0]
    my rank is 2, and Ireceived:
    [1, 1, 1, 1, 1]
    my rank is 0, and Ireceived:
    [3, 3, 3, 3, 3]
    my rank is 3, and Ireceived:
    [2, 2, 2, 2, 2]
    """
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()

    data_send = [comm_rank] * 500

    # set an order:
    # leader send and recv, worker recv and send
    # so that the process will not be stuck and wait forever
    if comm_rank == 0:
        comm.send(data_send, dest=(comm_rank + 1) % comm_size)
        data_recv = comm.recv(source=(comm_rank - 1) % comm_size)
    if comm_rank > 0:
        data_recv = comm.recv(source=(comm_rank - 1) % comm_size)
        comm.send(data_send, dest=(comm_rank + 1) % comm_size)
    print("my rank is %d, and Ireceived: %s" % (comm_rank, data_recv))
#end_func


def mpiBcast():
    """
    bcast: copy data and send out

    mpiexec -np 4 python mpiTest.py
    rank 0, got:[0, 1, 2, 3]
    rank 1, got:[0, 1, 2, 3]
    rank 3, got:[0, 1, 2, 3]
    rank 2, got:[0, 1, 2, 3]
    """
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()
    data = None

    if comm_rank == 0:
        data = range(comm_size)
    data = comm.bcast(data if comm_rank == 0 else None, root=0)
    print 'rank %d, got:%s' % (comm_rank, data)
#end_func


def mpiScatter():
    """
    scatter: split data and send out

    mpiexec -np 4 python mpiTest.py
    rank 2, got:2
    rank 1, got:1
    [0, 1, 2, 3]
    rank 0, got:0
    rank 3, got:3
    """
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()

    if comm_rank == 0:
        data = range(comm_size)
        print data
    else:
        data = None
    local_data = comm.scatter(data, root=0)


    print 'rank %d, got:%s' % (comm_rank, local_data)
#end_func


def mpiGather():
    """
    scatter and gather: send and collect data.

    mpiexec -np 4 python mpiTest.py
    rank 1, got and do:2
    rank 2, got and do:4
    [0, 1, 2, 3]
    rank 0, got and do:0
    [0, 2, 4, 6]
    rank 3, got and do:6
    """
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()

    if comm_rank == 0:
        data = range(comm_size)
        print data
    else:
        data = None
    local_data = comm.scatter(data, root=0)
    local_data = local_data * 2
    print 'rank %d, got and do:%s' % (comm_rank, local_data)
    combine_data = comm.gather(local_data, root=0)
    if comm_rank == 0:
        print combine_data
#end_func


def mpiMultiGather():
    """
    scatter and gather: send and collect data.

    mpiexec -np 4 python mpiTest.py
    rank 1, got and do:2
    rank 2, got and do:4
    [0, 1, 2, 3]
    rank 0, got and do:0
    [0, 2, 4, 6]
    rank 3, got and do:6
    """
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()

    if comm_rank == 0:
        combine_data = range(comm_size)
        print combine_data
    else:
        combine_data = None

    for i in range(1):
        local_data = comm.scatter(combine_data, root=0)
        local_data = local_data * 2
        print 'rank %d, got and do:%s' % (comm_rank, local_data)
        combine_data = comm.gather(local_data, root=0)

    # combine_data = comm.gather(local_data, root=0)
    # print 2, combine_data

    if comm_rank == 0:
        print combine_data

    # local_data = comm.scatter(combine_data, root=0)
    # local_data = local_data * 2
    # print 'rank %d, got and do:%s' % (comm_rank, local_data)
    # combine_data = comm.gather(local_data, root=0)
    # if comm_rank == 0:
    #     print combine_data

#end_func


def mpiReduce():
    """
    reduce: operation during collection

    mpiexec -np 4 python mpiTest.py
    rank 3, got and do: 6
    rank 2, got and do: 4
    [0, 1, 2, 3]
    rank 0, got and do: 0
    sumis:12
    rank 1, got and do: 2
    """
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()
    if comm_rank == 0:
        data = range(comm_size)
        print data
    else:
        data = None
    local_data = comm.scatter(data, root=0)
    local_data = local_data * 2
    print 'rank %d, got and do: %s' % (comm_rank, local_data)
    all_sum = comm.reduce(local_data, root=0, op=MPI.SUM)
    if comm_rank == 0:
        print 'sum is:%d' % all_sum
#end_func


def readFile():
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()
    all_lines = None
    inputFn = 'input1.txt'

    if comm_rank == 0:
        with open(inputFn) as inputFileobj:
            all_lines = inputFileobj.readlines()
    all_lines = comm.bcast(all_lines if comm_rank == 0 else None, root=0)
    num_lines = len(all_lines)
    local_lines_offset = np.linspace(0, num_lines, comm_size + 1).astype('int')
    local_lines = all_lines[local_lines_offset[comm_rank]:local_lines_offset[comm_rank + 1]]
    sys.stderr.write("%d/%d processor gets %d/%d data \n" % (comm_rank, comm_size, len(local_lines), num_lines))
    cnt = 0
    for line in local_lines:
        fields = line.strip().split('\t')
        cnt += 1
        if cnt % 100 == 0:
            sys.stderr.write("processor %d has processed %d/%d lines \n" % (comm_rank, cnt, len(local_lines)))
        output = line.strip() + ' process every line here'
        print output
#end_func


def listAdd():
    comm = MPI.COMM_WORLD
    comm_rank = comm.Get_rank()
    comm_size = comm.Get_size()

    if comm_rank == 0:
        data = [
            [[1, 2, 3], [4, 5, 6]],
            [[2, 3, 4], [5, 6, 7]],
            [[3, 4, 5], [6, 7, 8]],
        ]
        print data
    else:
        data = None
    local_data = comm.scatter(data, root=0)
    for lis1 in local_data:
        lis1[1] = lis1[0] + lis1[2]
    combine_data = comm.gather(local_data, root=0)
    print 'rank %d, got:%s' % (comm_rank, local_data)
    if comm_rank == 0:
        print combine_data
#end_func


def main():
    # fun1()
    # fun2()
    # mpiNode2nodeComm()
    # mpiBcast()
    # mpiScatter()
    mpiGather()
    # mpiReduce()
    # readFile()
    # listAdd()
#end_main

if __name__ == "__main__":
    main()
#end_if
