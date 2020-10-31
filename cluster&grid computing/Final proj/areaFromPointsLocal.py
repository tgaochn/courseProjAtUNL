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
import sys
from scipy.spatial import ConvexHull
import os

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
    sliceCnt = 20
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


def calcVol():
    # fnLis = [
    #     r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original\1.ply',
    #     r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original\2.ply',
    # ]
    # for fn in fnLis:
    #     calcVolSingleFile(fn)

    path = r'D:\Dropbox\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\tmp'
    file_list = os.listdir(path)

    for file_name in file_list:
        fn = os.path.join(path, file_name)
        calcVolSingleFile(fn)
#end_func


def volTest():
    # points = np.random.rand(30, 2)
    points = [
        [0, 0],
        [0, 1],
        [1, 0],
        # [2, 2],
    ]
    hull = ConvexHull(points)
    print hull.volume
#end_func


def calcVolFromFormattedFile():
    # inputFolder = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\layerID'
    # inputFolder = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\tmp'
    inputFolder = sys.argv[1]
    basefiles = os.listdir(inputFolder)

    for baseFn in basefiles:
        inputFn = '%s\\%s' % (inputFolder, baseFn)
        pointDic = {}
        wheatId = None
        zstep = None
        vol = 0
        for line in open(inputFn):
            items = line.strip().split('\t')
            wheatId = items[0]
            layerId = items[1]
            zstep = float(items[2])
            x = float(items[3])
            y = float(items[4])
            pointDic.setdefault(layerId, [])
            pointDic[layerId].append((x, y))

        for layerId, tmpLis in pointDic.iteritems():
            hull = ConvexHull(tmpLis)
            area = hull.volume
            curVol = area * zstep
            vol += curVol

        print '%s\t%s' % (wheatId, vol)
#end_func


def main():
    # volTest()
    calcVol()
    # calcVolFromFormattedFile()
#end_main


if __name__ == "__main__":
    main()
#end_if
