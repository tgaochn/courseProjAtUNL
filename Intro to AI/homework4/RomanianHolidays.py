#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName:

Author:
    Tian Gao
Email:
    tgaochn@gmail.com
CreationDate:
    10/7/2017
Description:

"""
import heapq
import time


allCitiesList = []
allCitiesHash = {}
allNodes = []
nnv = 0

class City:
    def __init__(self, name, h):
        self.name = name
        self.neighborsLis = []
        self.h = h
        self.visited = False
    #end_func

    def initNeig(self, neighborsLis):
        self.neighborsLis = neighborsLis
    #end_func
#end_class


class Node:
    def __init__(self, parentNode, city):
        self.parentNode = parentNode
        self.childrenNodeLis = []
        self.city = city
        self.pathValue = 0 if not parentNode else parentNode.pathValue + neighborsP(parentNode.city.name, city.name)
    #end_func
#end_class


def initCities():
    global allCitiesList, allCitiesHash

    # init all cities
    cityArad = City('Arad', 366)
    cityBucharest = City('Bucharest', 0)
    cityCraiova = City('Craiova', 160)
    cityDobreta = City('Dobreta', 242)
    cityEforie = City('Eforie', 161)
    cityFagaras = City('Fagaras', 176)
    cityGiurgiu = City('Giurgiu', 77)
    cityHirsova = City('Hirsova', 151)
    cityIasi = City('Iasi', 226)
    cityLugoj = City('Lugoj', 244)
    cityMehadia = City('Mehadia', 241)
    cityNeamt = City('Neamt', 234)
    cityOradea = City('Oradea', 380)
    cityPitesti = City('Pitesti', 100)
    cityRimnicuVilcea = City('RimnicuVilcea', 193)
    citySibiu = City('Sibiu', 253)
    cityTimisoara = City('Timisoara', 329)
    cityUrziceni = City('Urziceni', 80)
    cityVaslui = City('Vaslui', 199)
    cityZerind = City('Zerind', 374)

    # init neighbors
    cityArad.initNeig([(cityZerind, 75), (citySibiu, 140), (cityTimisoara, 118)])
    cityBucharest.initNeig([(cityPitesti, 101), (cityFagaras, 211), (cityGiurgiu, 90), (cityUrziceni, 85)])
    cityCraiova.initNeig([(cityDobreta, 120), (cityRimnicuVilcea, 146), (cityPitesti, 138)])
    cityDobreta.initNeig([(cityMehadia, 75), (cityCraiova, 120)])
    cityEforie.initNeig([(cityHirsova, 86)])
    cityFagaras.initNeig([(citySibiu, 99), (cityBucharest, 211)])
    cityGiurgiu.initNeig([(cityBucharest, 90)])
    cityHirsova.initNeig([(cityEforie, 86), (cityUrziceni, 98)])
    cityIasi.initNeig([(cityNeamt, 87), (cityVaslui, 92)])
    cityLugoj.initNeig([(cityTimisoara, 111), (cityMehadia, 70)])
    cityMehadia.initNeig([(cityLugoj, 70), (cityDobreta, 75)])
    cityNeamt.initNeig([(cityIasi, 87)])
    cityOradea.initNeig([(cityZerind, 71), (citySibiu, 151)])
    cityPitesti.initNeig([(cityRimnicuVilcea, 97), (cityCraiova, 138), (cityBucharest, 101)])
    cityRimnicuVilcea.initNeig([(citySibiu, 80), (cityCraiova, 146), (cityPitesti, 97)])
    citySibiu.initNeig([(cityOradea, 151), (cityArad, 140), (cityFagaras, 99), (cityRimnicuVilcea, 80)])
    cityTimisoara.initNeig([(cityArad, 118), (cityLugoj, 111)])
    cityUrziceni.initNeig([(cityBucharest, 85), (cityVaslui, 142), (cityHirsova, 98)])
    cityVaslui.initNeig([(cityIasi, 92), (cityUrziceni, 142)])
    cityZerind.initNeig([(cityOradea, 71), (cityArad, 75)])

    # build list and hash
    allCitiesList = [cityArad, cityBucharest, cityCraiova, cityDobreta, cityEforie, cityFagaras, cityGiurgiu, cityHirsova, cityIasi, cityLugoj, cityMehadia, cityNeamt, cityOradea, cityPitesti, cityRimnicuVilcea, citySibiu, cityTimisoara, cityUrziceni, cityVaslui, cityZerind]
    allCitiesHash = {'Bucharest': cityBucharest, 'Pitesti': cityPitesti, 'Urziceni': cityUrziceni, 'Lugoj': cityLugoj, 'Dobreta': cityDobreta, 'Hirsova': cityHirsova, 'Craiova': cityCraiova, 'Sibiu': citySibiu, 'Eforie': cityEforie, 'Fagaras': cityFagaras, 'Giurgiu': cityGiurgiu, 'Vaslui': cityVaslui, 'RimnicuVilcea': cityRimnicuVilcea, 'Zerind': cityZerind, 'Timisoara': cityTimisoara, 'Mehadia': cityMehadia, 'Arad': cityArad, 'Oradea': cityOradea, 'Iasi': cityIasi, 'Neamt': cityNeamt}
#end_func


def allCitiesFromList():
    global allCitiesList
    cityNmLis = []
    for city in allCitiesList:
        cityNmLis.append(city.name)
    return cityNmLis
#end_func


def allCitiesFromHtable():
    global allCitiesHash
    cityLis = []
    for cityNm, city in allCitiesHash.iteritems():
        cityLis.append(cityNm)
    return cityLis
#end_func


def getCityFromList(cityNm):
    global allCitiesList
    for city in allCitiesList:
        if city.name == cityNm: return city
    return None
#end_func


def getCityFromHtable(cityNm2):
    global allCitiesHash
    city = allCitiesHash.get(cityNm2, None)
    return city
#end_func


def neighborsUsingList(cityNm1):
    city = getCityFromList(cityNm1)
    return city.neighborsLis
#end_func


def neighborsUsingHtable(cityNm2):
    city = getCityFromHtable(cityNm2)
    return city.neighborsLis
#end_func


def neighborsWithinD(cityNm, dist):
    global allCitiesHash
    curNeighborsLis = []
    city = allCitiesHash.get(cityNm, None)
    if not city: return curNeighborsLis
    for (curCity, curDist) in city.neighborsLis:
        if curDist <= dist:
            curNeighborsLis.append(curCity)
    return curNeighborsLis
#end_func


def neighborsP(cityNm1, cityNm2):
    global allCitiesHash
    city1 = allCitiesHash.get(cityNm1, None)
    if not city1: return None
    for curCity, curDist in city1.neighborsLis:
        if curCity.name == cityNm2: return curDist
    return None
#end_func


def evaluateNode(node, costFunc='uniformCost'):
    f = None
    if costFunc == 'uniformCost':
        f = node.pathValue
    elif costFunc == 'greed':
        f = node.city.h
    elif costFunc == 'A*':
        f = node.city.h + node.pathValue
    return f
# end_func


def fetchNodeToExpand(nodeLis, costFunc='uniformCost'):
    nodeToExpand = None
    if costFunc == 'uniformCost':
        nodeToExpand = min(nodeLis, key=lambda node:node.pathValue)
    elif costFunc == 'greed':
        nodeToExpand = min(nodeLis, key=lambda node:node.city.h)
    elif costFunc == 'A*':
        nodeToExpand = min(nodeLis, key=lambda node:node.city.h + node.pathValue)
    return nodeToExpand
#end_func


def expandNode(curNode, searchType):
    global nnv
    nnv += 1
    if searchType == 'graphSearch':
        curNode.city.visited = True
    for (neighborCity, dist) in curNode.city.neighborsLis:
        childNode = Node(curNode, neighborCity)
        allNodes.append(childNode)
        curNode.childrenNodeLis.append(childNode)
    return curNode.childrenNodeLis
#end_func


def isGoal(curNode):
    rlt = False
    if curNode.city.name == 'Bucharest': rlt = True
    return rlt
#end_func


def search(startCityNm, costFunc, searchType, printMidRlt=False):
    """
    use heap to store frontiers so that the node with minimized cost(which is also the node to be expanded) is on the top
    :param costFunc:
        uniformCost, greed or A*
    :param searchType:
        graphSearch or treeSearch
    """
    frontierHeap = []
    heapq.heapify(frontierHeap)
    startCity = allCitiesHash.get(startCityNm, None)
    if not startCity: return None
    startNode = Node(None, startCity)
    allNodes.append(startNode)
    startNodeF = evaluateNode(startNode, costFunc)
    heapq.heappush(frontierHeap, (startNodeF, startNode))

    # iteratively update the heap and fetch the top node
    while frontierHeap:
        expandNodeCost, nodeToExpand = heapq.heappop(frontierHeap)
        if isGoal(nodeToExpand):
            if printMidRlt: print 'goal:', nodeToExpand.city.name, expandNodeCost
            return nodeToExpand
        if nodeToExpand.city.visited:continue
        if printMidRlt: print nodeToExpand.city.name, expandNodeCost
        newFronterNodeLis = expandNode(nodeToExpand, searchType)
        for newFronterNode in newFronterNodeLis:
            newNodeF = evaluateNode(newFronterNode, costFunc)
            heapq.heappush(frontierHeap, (newNodeF, newFronterNode))
#end_func


def fetchPath(goalNode):
    cityNmLis = [goalNode.city.name]
    curNode = goalNode
    while curNode.parentNode:
        cityNmLis.append(curNode.parentNode.city.name)
        curNode = curNode.parentNode
    cityNmLis.reverse()

    return ' - '.join(cityNmLis)
#end_func


def initNodes():
    for nodeId, node in enumerate(allNodes):
        del allNodes[nodeId]
#end_func


def romanianHolidays():
    # 4.1.1
    # Q1
    initCities()

    # Q2
    cityNmLis = allCitiesFromList()

    # Q3
    cityLis = allCitiesFromHtable()

    # Q4
    cityNm1 = 'Arad'
    cityNm2 = 'Craiova'
    city1 = getCityFromList(cityNm1)
    city2 = getCityFromHtable(cityNm2)

    # Q5
    neighLis1 = neighborsUsingList(cityNm1)
    neighLis2 = neighborsUsingHtable(cityNm2)

    # Q6
    dist = 200
    neigLis = neighborsWithinD(cityNm1, dist)

    # Q7
    cityDist = neighborsP(cityNm1, cityNm2)

    ########################################
    #4.2
    # You may want to use different parameters here
    # :param costFunc:
    #     uniformCost, greed or A*
    # :param searchType:
    #     graphSearch or treeSearch

    startTime = time.clock()


    citiesNmLis = sorted(allCitiesHash.keys())
    global nnv

    # costFunc = 'uniformCost'
    # costFunc = 'greed'
    # costFunc = 'A*'
    costFuncLis = ['uniformCost', 'greed', 'A*']

    # searchType = 'treeSearch'
    # searchType = 'graphSearch'
    searchTypeLis = ['treeSearch', 'graphSearch']

    for searchType in searchTypeLis:
        for costFunc in costFuncLis:
            print "current structure type: %s" % searchType
            print "current search strategy: %s" % costFunc
            print "-" * 10
            for startCityNm in citiesNmLis:
                nnv = 0
                initCities()
                initNodes()
                goalNode = search(startCityNm, costFunc, searchType)
                elapsed = (time.clock() - startTime)

                # output results
                pathStr = fetchPath(goalNode)
                print 'start city: %s, cost function: %s, search type: %s' % (startCityNm, costFunc, searchType)
                print 'Path to Bucharest: %s' % pathStr
                print '#nodes visited: %s' % nnv
                print 'Total cost of path: %s' % goalNode.pathValue
                print 'time cost: %s sec' % elapsed
                print '==' * 20

                # output formatted table for latex
                # print '%s & %s & %s & %s & %.2f ms \\\\ \\hline' % (startCityNm, nnv, pathStr, goalNode.pathValue, elapsed * 1000)
            print '***' * 20
            # print '%s - %s' % (costFunc, searchType)
#end_func


def main():
    romanianHolidays()
#end_main

if __name__ == "__main__":
    main()
#end_if
