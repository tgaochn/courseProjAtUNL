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
def func():
    a = "cityArad = City('Arad', 366)	cityBucharest = City('Bucharest', 0)	cityCraiova = City('Craiova', 160)	cityDobreta = City('Dobreta', 242)	cityEforie = City('Eforie', 161)	cityFagaras = City('Fagaras', 176)	cityGiurgiu = City('Giurgiu', 77)	cityHirsova = City('Hirsova', 151)	cityIasi = City('Iasi', 226)	cityLugoj = City('Lugoj', 244)	cityMehadia = City('Mehadia', 241)	cityNeamt = City('Neamt', 234)	cityOradea = City('Oradea', 380)	cityPitesti = City('Pitesti', 100)	cityRimnicuVilcea = City('RimnicuVilcea', 193)	citySibiu = City('Sibiu', 253)	cityTimisoara = City('Timisoara', 329)	cityUrziceni = City('Urziceni', 80)	cityVaslui = City('Vaslui', 199)	cityZerind = City('Zerind', 374)"
    aLis = a.split('\t')
    cityLis = []
    cityDic = {}
    for item in aLis:
        city, _, _ = item.partition(' = ')
        name = city[4:]
        cityLis.append(city)
        cityDic[name] = '_%s_' % city
        # print '%s.initNeig([])' % city
    # print cityLis
    print cityDic
#end_func

def main():
    func()
#end_main

if __name__ == "__main__":
    main()
#end_if
