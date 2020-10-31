#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName     : ''
Author          : 'Tian Gao'
CreationDate    : '2017/2/3'
Description     :

"""

def test():
    func()
#end_test

def func():
    inputFilenm = r'D:\Dropbox\PatternRecognitionSharing\hw1\NN_sigmoid_withDropout.txt'
    outputFilenm = r'D:\Dropbox\PatternRecognitionSharing\hw1\NN_sigmoid_withDropout_formatted.csv'
    with open(inputFilenm) as fIn, open(outputFilenm, 'w') as fOut:
        for line in fIn:
            if line[:4] != 'Step':continue
            line = line.strip().strip('.')
            stepStr, _, tail = line.partition(':')
            stepCnt = stepStr.strip('Step ')
            lossItems = tail.split('=')
            testLoss = lossItems[2]
            outputLine ='%s,%s\n' % (stepCnt, testLoss)
            fOut.write(outputLine)
#end_func

def main():
    test()
#end_main

if __name__ == "__main__":
    main()
#end_if
