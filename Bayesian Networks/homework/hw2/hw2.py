#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ProjectName     : ''
Author          : 'Tian Gao'
CreationDate    : '2017/2/27'
Description     :

"""

from graphviz import Digraph
import itertools


def equalA():
    nodeLis = ['W', 'X', 'Y', 'Z', 'R', 'S']
    e1 = ['WX', 'XW']
    e2 = ['XZ']
    e3 = ['YZ']
    e4 = ['RZ', 'ZR']
    e5 = ['SZ', 'ZS']
    e6 = ['SR', 'RS']
    for idx, edgeLis in enumerate(itertools.product(e1, e2, e3, e4, e5, e6)):
        dot = Digraph(format='png')
        for node in nodeLis:
            dot.node(node)
        dot.edges(edgeLis)
        dot.render(r'C:\Users\Administrator\Desktop\q2\equalA\%s.gv' % idx, view=True)
#end_func

def equalC():
    idx = 1
    nodeLis = ['W', 'X', 'Y', 'Z', 'R', 'S']
    e0 = ['WX']
    e1 = ['WY']
    e2 = ['XZ']
    e3 = ['YZ']
    e4 = ['RZ', 'ZR']
    e5 = ['SZ', 'ZS']
    e6 = ['SR', 'RS']
    for edgeLis in itertools.product(e0, e1, e2, e3, e4, e5, e6):
        dot = Digraph(format='png')
        for node in nodeLis:
            dot.node(node)
        dot.edges(edgeLis)
        dot.render(r'C:\Users\Administrator\Desktop\q2\equalC\%s.gv' % idx, view=True)
        idx += 1

    e0 = ['WX']
    e1 = ['YW']
    e2 = ['XZ']
    e3 = ['YZ']
    e4 = ['RZ', 'ZR']
    e5 = ['SZ', 'ZS']
    e6 = ['SR', 'RS']
    for edgeLis in itertools.product(e0, e1, e2, e3, e4, e5, e6):
        dot = Digraph(format='png')
        for node in nodeLis:
            dot.node(node)
        dot.edges(edgeLis)
        dot.render(r'C:\Users\Administrator\Desktop\q2\equalC\%s.gv' % idx, view=True)
        idx += 1

    e0 = ['XW']
    e1 = ['WY']
    e2 = ['XZ']
    e3 = ['YZ']
    e4 = ['RZ', 'ZR']
    e5 = ['SZ', 'ZS']
    e6 = ['SR', 'RS']
    for edgeLis in itertools.product(e0, e1, e2, e3, e4, e5, e6):
        dot = Digraph(format='png')
        for node in nodeLis:
            dot.node(node)
        dot.edges(edgeLis)
        dot.render(r'C:\Users\Administrator\Desktop\q2\equalC\%s.gv' % idx, view=True)
        idx += 1

#end_func

def equalD():
    idx = 1
    nodeLis = ['W', 'X', 'Y', 'Z', 'R', 'S']
    e1 = ['WX', 'XW']
    e2 = ['XZ']
    e3 = ['ZY']
    e4 = ['RZ', 'ZR']
    e5 = ['SZ', 'ZS']
    e6 = ['SR', 'RS']
    for edgeLis in itertools.product(e1, e2, e3, e4, e5, e6):
        dot = Digraph(format='png')
        for node in nodeLis:
            dot.node(node)
        dot.edges(edgeLis)
        dot.render(r'C:\Users\Administrator\Desktop\q2\equalD\%s.gv' % idx, view=True)
        idx += 1

    e1 = ['XW']
    e2 = ['ZX']
    e3 = ['YZ']
    e4 = ['RZ', 'ZR']
    e5 = ['SZ', 'ZS']
    e6 = ['SR', 'RS']
    for edgeLis in itertools.product(e1, e2, e3, e4, e5, e6):
        dot = Digraph(format='png')
        for node in nodeLis:
            dot.node(node)
        dot.edges(edgeLis)
        dot.render(r'C:\Users\Administrator\Desktop\q2\equalD\%s.gv' % idx, view=True)
        idx += 1

#end_func

def Q2():
    # equalA()
    # equalC()
    equalD()
#end_func


def main():
    Q2()
#end_main

if __name__ == "__main__":
    main()
#end_if
