#!usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import mpi4py.MPI as MPI
import numpy as np

#
#  Global variables for MPI
#

# instance for invoking MPI relatedfunctions
comm = MPI.COMM_WORLD
# the node rank in the whole community
comm_rank = comm.Get_rank()
# the size of the whole community, i.e.,the total number of working nodes in the MPI cluster
comm_size = comm.Get_size()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python *.py directoty_with_files\n")
        sys.exit(1)
    path = sys.argv[1]
    path = './testData'
    file_list = None
    if comm_rank == 0:
        file_list = os.listdir(path)
        sys.stderr.write("%d files\n" % len(file_list))
    file_list = comm.bcast(file_list if comm_rank == 0 else None, root=0) # broadcast filename
    num_files = len(file_list)
    local_files_offset = np.linspace(0, num_files, comm_size + 1).astype('int')
    print local_files_offset
    local_files = file_list[local_files_offset[comm_rank]:local_files_offset[comm_rank + 1]]
    # sys.stderr.write("%d/%d processor gets %d/%d data \n" % (comm_rank, comm_size, len(local_files), num_files))
    sys.stderr.write("%d/%d processor gets %s \n" % (comm_rank, comm_size, local_files))
    cnt = 0

    for file_name in local_files:
        hd = open(os.path.join(path, file_name))
        for line in hd:
            output = line.strip() + ' process every line here'
            # print output
        cnt += 1
        # sys.stderr.write("processor %d has processed %d/%d files \n" % (comm_rank, cnt, len(local_files)))
        hd.close()