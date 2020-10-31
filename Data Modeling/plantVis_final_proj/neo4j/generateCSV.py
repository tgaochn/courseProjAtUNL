# !/usr/bin/env python
# coding: utf-8
"""
generateCSV.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    11/28/2018, 9:53:56 PM
Link:
    
Description:
    
"""
import os


def func():
    dataDic = {}
    dataPath = r'Z:\result\3_rotatingCamera\3_panicleExperiment'
    outputFn = 'rlt/init.csv'
    for curDate in os.listdir(dataPath):
        datePath = os.path.join(dataPath, curDate)
        for plantId in os.listdir(datePath):
            dataDic.setdefault(plantId, [])
            plyPath = os.path.join(datePath, plantId, 'original', 'merge', 'surface-L2-clean.ply')
            if not os.path.isfile(plyPath): continue
            dataDic[plantId].append((curDate, plyPath))

    with open(outputFn, 'w') as outputFile:
        outputFile.write('plantId,curDate,nextDate,plyPath\n')
        for plantId, dateInfo in dataDic.iteritems():
            dateInfo.sort(key=lambda x: x[1])
            for idx, (curDate, plyPath) in enumerate(dateInfo):
                nextDate = dateInfo[idx + 1][0] if idx < len(dateInfo) - 1 else ''
                outputItems = [plantId, curDate, nextDate, plyPath]
                outputLine = ','.join(outputItems)
                outputFile.write('%s\n' % outputLine)
# end_func


def main():
    func()
# end_main


if __name__ == "__main__":
    main()
# end_if
