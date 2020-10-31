#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName:

Author:
    Tian Gao
Email:
    tgaochn@gmail.com
CreationDate:
    12/2/2017
Description:

"""
from scipy.spatial import ConvexHull
import sys
import os
import mpi4py.MPI as MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
comm_rank = comm.Get_rank()
comm_size = comm.Get_size()

def loadPointCloud(fn):
    pc = []
    with open(fn) as fileobj:
        for lineIdx, line in enumerate(fileobj):
            if lineIdx < 14: continue
            items = line.strip().split(' ')
            x = float(items[0])
            y = float(items[1])
            z = float(items[2])
            pc.append((x, y, z))
    return pc
#end_func

def calcVolSingleFile(fn):
    sliceCnt = 1000
    epsilon = 0.0001

    pc = loadPointCloud(fn)
    pc = sorted(pc, key=lambda x: x[2])
    zmax = pc[-1][2]
    zmin = pc[0][2]
    zstep = (zmax - zmin) / sliceCnt
    volTotal = 0
    curLowerBound = zmin
    curUpperBound = zmin + zstep
    tmpPointSet = []
    for (x, y, z) in pc:
        if z == zmax:
            z -= epsilon
        if curLowerBound <= z < curUpperBound:
            tmpPointSet.append((x, y))
        else:
            # calculate area of one layer
            if len(tmpPointSet) >= 3:
                hull = ConvexHull(tmpPointSet)
                area = hull.volume
                print area
                curVol = area * zstep
                volTotal += curVol

            # update bound
            curLowerBound = curUpperBound
            curUpperBound = curUpperBound + zstep
            tmpPointSet = [(x, y)]

    print 'file: %s, vol: %s' % (os.path.basename(fn), volTotal)
#end_func


def calcVolLocal():
    # fnLis = [
    #     r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original\1.ply',
    #     r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original\2.ply',
    # ]
    # for fn in fnLis:
    #     calcVolSingleFile(fn)

    # path = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original'
    path = sys.argv[1]
    file_list = os.listdir(path)
    if len(sys.argv) > 2: file_list = file_list[:int(sys.argv[2])]

    for file_name in file_list:
        fn = os.path.join(path, file_name)
        calcVolSingleFile(fn)
#end_func


def calcVolMPIByFile():
    path = sys.argv[1]
    # path = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original'
    file_list = None
    if comm_rank == 0:
        file_list = os.listdir(path)
        if len(sys.argv) > 2: file_list = file_list[:int(sys.argv[2])]
        print "%d files\n" % len(file_list)
    file_list = comm.bcast(file_list if comm_rank == 0 else None, root=0) # broadcast filename
    num_files = len(file_list)
    local_files_offset = np.linspace(0, num_files, comm_size + 1).astype('int')
    print local_files_offset
    local_files = file_list[local_files_offset[comm_rank]:local_files_offset[comm_rank + 1]]
    sys.stderr.write("%d/%d processor gets %s \n" % (comm_rank, comm_size, local_files))

    for file_name in local_files:
        fn = os.path.join(path, file_name)
        # calcVolSingleFile(fn)
#end_func


def calcVolMPIBySlice():
    path = sys.argv[1]
    file_list = None
    data_list = None
    if comm_rank == 0:
        file_list = os.listdir(path)
        if len(sys.argv) > 2: file_list = file_list[:int(sys.argv[2])]
        print "%d files\n" % len(file_list)
    file_list = comm.bcast(file_list if comm_rank == 0 else None, root=0) # broadcast filename
    num_files = len(file_list)
    local_files_offset = np.linspace(0, num_files, comm_size + 1).astype('int')
    print local_files_offset
    local_files = file_list[local_files_offset[comm_rank]:local_files_offset[comm_rank + 1]]
    sys.stderr.write("%d/%d processor gets %s \n" % (comm_rank, comm_size, local_files))

    for file_name in local_files:
        fn = os.path.join(path, file_name)
        with open(fn) as fileobj:
            lines = fileobj.readlines()
            # lines = comm.bcast(lines if comm_rank == 0 else None, root=0)  # broadcast filename
            lines = comm.bcast(lines)  # broadcast filename
            local_lines_offset = np.linspace(0, len(lines), comm_size + 1).astype('int')
            local_lines = lines[local_lines_offset[comm_rank]:local_lines_offset[comm_rank + 1]]
            # print local_lines
            sys.stderr.write("%d/%d processor gets %s \n" % (comm_rank, comm_size, local_lines))


    #end_func


def main():
    start = time.clock()

    # calcVolMPIByFile()
    # calcVolMPIBySlice()
    calcVolLocal()

    print time.clock() - start
#end_main


if __name__ == "__main__":
    main()
#end_if
