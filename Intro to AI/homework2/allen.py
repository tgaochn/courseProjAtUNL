#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName     : 
Author          : Tian Gao
CreationDate    : 2017/9/9
Description     :

"""
class TimePoint:
    def __init__(self, repSec=0):
        self.repSec = repSec
    #end_func

    def __str__(self):
        return str(self.repSec)
    #end_func

    def __sub__(self, other):
        return self.repSec - other.repSec
    #end_func

    def __eq__(self, other):
        return self.repSec == other.repSec
    #end_func

    def __lt__(self, other):
        return self.repSec < other.repSec
    #end_func

    def __le__(self, other):
        return self.repSec <= other.repSec
    #end_func

    def __gt__(self, other):
        return self.repSec > other.repSec
    #end_func

    def __ge__(self, other):
        return self.repSec >= other.repSec
    #end_func
#end_class

class Interval:
    def __init__(self, beginTime=TimePoint(0), endTime=TimePoint(0)):
        self.beginTime = beginTime
        self.endTime = endTime
    #end_func
#end_class

def Start(interval):
    return interval.beginTime
#end_func

def End(interval):
    return interval.endTime
#end_func

def Meet(interval1, interval2):
    rlt = End(interval1) == Start(interval2)
    return rlt
#end_func

def Before(interval1, interval2):
    rlt = End(interval1) < Start(interval2)
    return rlt
#end_func

def After(interval1, interval2):
    rlt = Before(interval2, interval1)
    return rlt
#end_func

def During(interval1, interval2):
    rlt = Start(interval2) <= Start(interval1) and End(interval1) <= End(interval2)
    return rlt
#end_func

def Overlap(interval1, interval2):
    maxLen = min(End(interval2) - Start(interval1), End(interval1) - Start(interval2))
    minStartTimeSec = max([Start(interval1), Start(interval2)], key=lambda x:x.repSec).repSec
    maxStartTimeSec = max([End(interval1), End(interval2)], key=lambda x:x.repSec).repSec
    for startTimeSec in xrange(minStartTimeSec, maxStartTimeSec):
        for curLen in xrange(1, maxLen + 1):
            startTime = TimePoint(startTimeSec)
            endTime = TimePoint(startTimeSec + curLen)
            curInterval = Interval(startTime, endTime)
            if During(curInterval, interval1) and During(curInterval, interval2): return True
    return False
#end_func

def Equals(interval1, interval2):
    rlt = Start(interval1) == Start(interval2) and End(interval1) == End(interval2)
    return rlt
#end_func

def Finishes(interval1, interval2):
    rlt = End(interval1) == End(interval2)
    return rlt
#end_func

def Contains(interval1, interval2):
    rlt = Start(interval1) < Start(interval2) and End(interval1) > End(interval2)
    return rlt
#end_func

def TestFunc(funNm, interval1, interval2):
    rlt = funNm(interval1, interval2)

    print "=" * 20
    print "now testing: %s" % funNm.__name__
    print "input1: (%s, %s)" % (Start(interval1), End(interval1))
    print "input2: (%s, %s)" % (Start(interval2), End(interval2))
    print "result: %s" % rlt
#end_func

def AllenTest():
    interval1 = Interval(TimePoint(5), TimePoint(10))
    interval2 = Interval(TimePoint(7), TimePoint(13))

    TestFunc(Meet, interval1, interval2)
    TestFunc(Before, interval1, interval2)
    TestFunc(After, interval1, interval2)
    TestFunc(During, interval1, interval2)
    TestFunc(Overlap, interval1, interval2)
    TestFunc(Equals, interval1, interval2)
    TestFunc(Finishes, interval1, interval2)
    TestFunc(Contains, interval1, interval2)
#end_test

def main():
    AllenTest()
#end_main

if __name__ == "__main__":
       main()
#end_if
