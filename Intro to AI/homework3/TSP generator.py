#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName     :
Author          : Tian Gao
Email           : tgaochn@gmail.com
CreationDate    : 2017-09-26T01:35:01.266Z
Description     :

"""

import random
import math

class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    #end_func
#end_class


class Map:
    def __init__(self, pointLis):
        self.pointLis = pointLis
        self.distMap = self.getDistMap(pointLis)
    #end_func

    @staticmethod
    def getPointDist(point1, point2):
        dist = math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
        return dist
    #end_func

    def getDistMap(self, pointLis):
        distMap = {}
        for point1 in pointLis:
            for point2 in pointLis:
                dist = self.getPointDist(point1, point2)
                distMap[(point1.name, point2.name)] = dist
                distMap[(point2.name, point1.name)] = dist
        return distMap
    #end_func
#end_class


def generateTSP(pointCnt, hasRtn=False):
    pointLis = []
    for i in xrange(pointCnt):
        i = str(i)
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        point = Point(i, x, y)
        pointLis.append(point)
    cityMap = Map(pointLis)

    for point in pointLis:
        print 'city name: %s, location: (%s, %s)' % (point.name, point.x, point.y)
    for (pointNm1, pointNm2), dist in cityMap.distMap.iteritems():
        print 'distance between %s and %s is %s' % (pointNm1, pointNm2, dist)

    if hasRtn: return cityMap
#end_func


def main():
    pointCnt = 5
    generateTSP(pointCnt)
#end_main

if __name__ == "__main__":
    main()
#end_if
