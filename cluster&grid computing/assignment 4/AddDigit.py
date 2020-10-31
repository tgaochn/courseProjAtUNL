#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def GetLineIdx(processId, totalLineCnt, totalProcessCnt):
    interval = totalLineCnt / totalProcessCnt
    startLineIdx = processId * interval
    endLineIdx = (processId + 1) * interval
    return startLineIdx, endLineIdx
#end_func

def main():

#end_main

if __name__ == "__main__":
   main()
#end_if
