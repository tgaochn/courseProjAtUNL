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
import os
SLICE_CNT = 50


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

def addWheatIDSingle():
    """
    add wheat id for a single file
    """
    inputFn = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\2.ply'
    outputFn = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\F2.ply'

    with open(inputFn) as inputFileobj, open(outputFn, 'w') as outputFileobj:
        for lineIdx, line in enumerate(inputFileobj):
            if lineIdx < 13: continue
            outputFileobj.write(line)
#end_func


def addWheatIDMultiple():
    """
    add wheat id for multiple files
    """
    inputFolder = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original'
    outputFolder = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\wheatID'

    files = os.listdir(inputFolder)
    for wheatId, fn in enumerate(files):
        if os.path.isdir(fn): continue
        inputFn = '%s\\%s' % (inputFolder, fn)
        outputFn = '%s\\%s' % (outputFolder, fn)

        with open(inputFn) as inputFileobj, open(outputFn, 'w') as outputFileobj:
            for lineIdx, line in enumerate(inputFileobj):
                if lineIdx < 13: continue
                outputFileobj.write('%s %s' % (wheatId, line))
#end_func


def addLayerIDMultiple():
    """
    add wheat id and layer id for multiple files
    """
    inputFolder = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original'
    outputFolder = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\layerID'

    sliceCnt = SLICE_CNT

    files = os.listdir(inputFolder)
    for wheatId, fn in enumerate(files):
        if os.path.isdir(fn): continue
        inputFn = '%s\\%s' % (inputFolder, fn)
        outputFn = '%s\\%s' % (outputFolder, fn)

        with open(outputFn, 'w') as outputFileobj:
            pc = loadPointCloud(inputFn)
            pc = sorted(pc, key=lambda x: x[2])
            zmax = pc[-1][2]
            zmin = pc[0][2]
            zstep = (zmax - zmin) / sliceCnt
            curLayer = 0
            curUpperBound = zmin + zstep
            for (x, y, z) in pc:
                if z > curUpperBound:
                    curLayer += 1
                    curUpperBound += zstep
                outputItems = [str(wheatId), str(curLayer), str(zstep), str(x), str(y)]
                outputLine = '\t'.join(outputItems)
                outputFileobj.write('%s\n' % outputLine)
#end_func

def addLayerIDMultipleCopy():
    """
    add wheat id and layer id for multiple files
    """
    inputFn = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\original\2.ply'
    outputFolder = r'D:\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\data\layerID'

    sliceCnt = SLICE_CNT
    copyCnt = 2000

    for wheatId in xrange(copyCnt):
        baseFn = os.path.basename(inputFn)
        base, _, ext = baseFn.partition('.')
        outputFn = '%s\\%s.%s' % (outputFolder, wheatId, ext)

        with open(outputFn, 'w') as outputFileobj:
            pc = loadPointCloud(inputFn)
            pc = sorted(pc, key=lambda x: x[2])
            zmax = pc[-1][2]
            zmin = pc[0][2]
            zstep = (zmax - zmin) / sliceCnt
            curLayer = 0
            curUpperBound = zmin + zstep
            for (x, y, z) in pc:
                if z > curUpperBound:
                    curLayer += 1
                    curUpperBound += zstep
                outputItems = [str(wheatId), str(curLayer), str(zstep), str(x), str(y)]
                outputLine = '\t'.join(outputItems)
                outputFileobj.write('%s\n' % outputLine)
#end_func

def prodData():
    """
    add wheat id and layer id for multiple files
    """
    outputFolder = r'D:\Dropbox\project\1. homework\3. Fall 2017\CSCE 835, cluster&grid computing - Fall 2017\Final proj\test1'

    fileCnt = 4
    contCnt = 5

    for wheatId in xrange(fileCnt):
        outputFn = '%s\\%s.%s' % (outputFolder, wheatId, '.txt')

        with open(outputFn, 'w') as outputFileobj:
            for i in range(contCnt):
                outputFileobj.write('%s\n' % wheatId)
#end_func

def main():
    # addWheatIDSingle()
    # addWheatIDMultiple()
    # addLayerIDMultiple()
    # addLayerIDMultipleCopy()
    prodData()
#end_main

if __name__ == "__main__":
    main()
#end_if
