#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName     : 
Author          : Tian Gao
CreationDate    : 2017/9/20
Description     :

"""

import random

STATUS_MAP = {
    ('A', 'dirty', 'dirty', 'left'): ('A', 'dirty', 'dirty'),
    ('A', 'dirty', 'dirty', 'suck'): ('A', 'clean', 'dirty'),
    ('A', 'dirty', 'dirty', 'right'): ('B', 'dirty', 'dirty'),
    ('B', 'dirty', 'dirty', 'right'): ('B', 'dirty', 'dirty'),
    ('B', 'dirty', 'dirty', 'left'): ('A', 'dirty', 'dirty'),
    ('B', 'dirty', 'dirty', 'suck'): ('B', 'dirty', 'clean'),
    ('A', 'clean', 'dirty', 'left'): ('A', 'clean', 'dirty'),
    ('A', 'clean', 'dirty', 'right'): ('B', 'clean', 'dirty'),
    ('A', 'clean', 'dirty', 'suck'): ('A', 'clean', 'dirty'),
    ('B', 'clean', 'dirty', 'right'): ('B', 'clean', 'dirty'),
    ('B', 'clean', 'dirty', 'left'): ('A', 'clean', 'dirty'),
    ('B', 'clean', 'dirty', 'suck'): ('B', 'clean', 'clean'),
    ('A', 'dirty', 'clean', 'left'): ('A', 'dirty', 'clean'),
    ('A', 'dirty', 'clean', 'right'): ('B', 'dirty', 'clean'),
    ('A', 'dirty', 'clean', 'suck'): ('A', 'clean', 'clean'),
    ('B', 'dirty', 'clean', 'left'): ('A', 'dirty', 'clean'),
    ('B', 'dirty', 'clean', 'right'): ('B', 'dirty', 'clean'),
    ('B', 'dirty', 'clean', 'suck'): ('B', 'dirty', 'clean'),
    ('A', 'clean', 'clean', 'left'): ('A', 'clean', 'clean'),
    ('A', 'clean', 'clean', 'right'): ('B', 'clean', 'clean'),
    ('A', 'clean', 'clean', 'suck'): ('A', 'clean', 'clean'),
    ('B', 'clean', 'clean', 'left'): ('A', 'clean', 'clean'),
    ('B', 'clean', 'clean', 'right'): ('B', 'clean', 'clean'),
    ('B', 'clean', 'clean', 'suck'): ('B', 'clean', 'clean'),
}

STATUS_LIST = [
    ('A', 'clean', 'clean'),
    ('A', 'clean', 'dirty'),
    ('A', 'dirty', 'clean'),
    ('A', 'dirty', 'dirty'),
    ('B', 'clean', 'clean'),
    ('B', 'clean', 'dirty'),
    ('B', 'dirty', 'clean'),
    ('B', 'dirty', 'dirty'),
]

ACTION2PENALTY = {
    'left': 1,
    'right': 1,
    'suck': 2,
}

ROOM_IDX_MAP = {
    'A': 1,
    'B': 2,
}

def SimpleReflexAgent(location, roomStatus):
    action = 'NoOp'
    if roomStatus == 'dirty':
        action = 'suck'
    elif location == 'A':
        action = 'right'
    elif location == 'B':
        action = 'left'
    return action
#end_test

def RunOnOneStatus():
    print 'sub-question 2'

    curStat = random.choice(STATUS_LIST)
    curLocation = curStat[0]
    roomStatA = curStat[1]
    roomStatB = curStat[2]

    print 'randomly choose an initial status'
    print 'location: %s, room A status:%s, room B status:%s' % (curLocation, roomStatA, roomStatB)

    while roomStatA != 'clean' or roomStatB != 'clean':
        curRoomIdx = ROOM_IDX_MAP[curLocation]
        curRoomStatus = curStat[curRoomIdx]
        nextAction = SimpleReflexAgent(curLocation, curRoomStatus)
        print 'current location: %s, room A status: %s, room B status: %s, next action: %s' % (curLocation, roomStatA, roomStatB, nextAction)
        nextStatus = STATUS_MAP[(curLocation, roomStatA, roomStatB, nextAction)]
        curStat = nextStatus
        curLocation = curStat[0]
        roomStatA = curStat[1]
        roomStatB = curStat[2]
    print 'final status:'
    print 'location: %s, room A status: %s, room B status: %s' % (curLocation, roomStatA, roomStatB)
    print '**' * 30
#end_func

def RunEachStatusAndShowPerfermance():
    print 'sub-question 4'

    for curStat in STATUS_LIST:
        curLocation = curStat[0]
        roomStatA = curStat[1]
        roomStatB = curStat[2]
        totalPenalty = 0

        print 'initial status: location: %s, room A status:%s, room B status:%s' % (curLocation, roomStatA, roomStatB)

        while roomStatA != 'clean' or roomStatB != 'clean':
            curRoomIdx = ROOM_IDX_MAP[curLocation]
            curRoomStatus = curStat[curRoomIdx]
            nextAction = SimpleReflexAgent(curLocation, curRoomStatus)
            curPenalty = ACTION2PENALTY[nextAction]
            totalPenalty += curPenalty
            print 'current location: %s, room A status: %s, room B status: %s, next action: %s, penalty of next action: %s, total penalty: %s' % (curLocation, roomStatA, roomStatB, nextAction, curPenalty, totalPenalty)
            nextStatus = STATUS_MAP[(curLocation, roomStatA, roomStatB, nextAction)]
            curStat = nextStatus
            curLocation = curStat[0]
            roomStatA = curStat[1]
            roomStatB = curStat[2]
        print 'final status:'
        print 'location: %s, room A status: %s, room B status: %s, total penalty: %s' % (curLocation, roomStatA, roomStatB, totalPenalty)
        print '==' * 10
#end_func

def main():
    RunOnOneStatus()
    RunEachStatusAndShowPerfermance()
#end_main

if __name__ == "__main__":
    main()
#end_if
