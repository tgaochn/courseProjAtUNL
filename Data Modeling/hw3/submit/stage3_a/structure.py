# !/usr/bin/env python
# coding: utf-8
"""
structure.py
Author:
    Tian Gao (tgaochn@gmail.com)
CreationDate:
    10/26/2018, 12:37:04 PM
Link:
    
Description:
    
"""
import math
import os


class LeafNode():
    def __init__(self, tableFileInfoLis, leafNodeFn):
        # tableFileInfoLis: [(key, tableFilename)]
        self.maxKey = max(tableFileInfoLis, key=lambda x: x[0])[0]
        self.nodeFn = leafNodeFn

        with open(leafNodeFn, 'w') as leafNodeFile:
            leafNodeFlag = 1
            leafNodeFile.write('%s\n' % leafNodeFlag)
            for key, tableFn in tableFileInfoLis:
                leafNodeFile.write('%s,%s\n' % (key, tableFn))
    # end_func
# end_class


class NonLeafNode():
    def __init__(self, nodeLis, nonLeafNodeFn):
        keyLis = []
        for node in nodeLis:
            keyLis.append(node.maxKey)
        self.maxKey = max(keyLis)
        self.nodeFn = nonLeafNodeFn

        with open(nonLeafNodeFn, 'w') as nonLeafNodeFile:
            leafNodeFlag = 0
            nonLeafNodeFile.write('%s\n' % leafNodeFlag)
            nonLeafNodeFile.write('%s\n' % keyLis[:-1])
            for node in nodeLis:
                nonLeafNodeFile.write('%s\n' % node.nodeFn)
    # end_func
# end_class


class BplusTree():
    def __init__(self, treeFilePath, fanout):
        self.treeFilePath = treeFilePath
        self.fanout = fanout
    # end_init

    def allocateNode(self, childrenNodeCnt, curNodeCnt):
        # figure out how the children node are allocated in current layer

        minChildrenCnt = int(childrenNodeCnt / curNodeCnt)
        allocateRlt = [minChildrenCnt] * curNodeCnt
        restChildren = childrenNodeCnt - minChildrenCnt * curNodeCnt
        for i in xrange(restChildren):
            allocateRlt[i] += 1
        return allocateRlt
    # end_func

    def buildTree(self, tableInfoLis):
        """
        tableInfoLis:
            [(key, fn)]
        """
        # build the leaf nodes
        tableFileCnt = len(tableInfoLis)
        leafNodeCnt = max(int(math.ceil(tableFileCnt / (self.fanout - 1))), 1)
        # print tableFileCnt
        layerCnt = int(math.ceil(math.log(leafNodeCnt, self.fanout)))
        allocateRlt = self.allocateNode(tableFileCnt, leafNodeCnt)
        tableFnId = 0
        leafFnId = 0
        childrenNodeLis = []
        for i in allocateRlt:
            tableFileInfoLis = []
            for j in xrange(i):
                key, fn = tableInfoLis[tableFnId]
                tableFnId += 1
                tableFileInfoLis.append((key, fn))
            leafFn = os.path.join(self.treeFilePath, 'leaf_%s.dat' % leafFnId)
            leafFnId += 1
            leaf = LeafNode(tableFileInfoLis, leafFn)
            childrenNodeLis.append(leaf)
        # end_for

        # build the non-leaf nodes for each upper layer
        nodeFnId = 0
        layerLis = sorted(range(layerCnt), reverse=True)
        for layerId in layerLis:
            curLayerNodeLis = []
            childrenNodeCnt = len(childrenNodeLis)
            curLayerNodeCnt = int(math.ceil(childrenNodeCnt * 1.0 / self.fanout))
            allocateRlt = self.allocateNode(childrenNodeCnt, curLayerNodeCnt)
            childrenId = 0
            for i in allocateRlt:
                nodeLis = []
                for j in xrange(i):
                    nodeLis.append(childrenNodeLis[childrenId])
                    childrenId += 1
                curNodeFn = os.path.join(self.treeFilePath, 'nonleaf_%s-%s.dat' % (layerId, nodeFnId))
                nodeFnId += 1
                if layerId == 0:
                    curNodeFn = os.path.join(self.treeFilePath, 'root.dat')
                nonLeafNode = NonLeafNode(nodeLis, curNodeFn)
                curLayerNodeLis.append(nonLeafNode)
            childrenNodeLis = curLayerNodeLis
        # end_for
    # end_func

    def isLeaf(self, fn):
        with open(fn) as f:
            return bool(int(f.readline().strip()))
    # end_func

    def getSlotId(self, key, valueLis):
        # get the slot id in the non-leaf node 
        if key > valueLis[-1]:
            return len(valueLis)
        else:
            for slotId, value in enumerate(valueLis):
                if key <= value:
                    return slotId
    # end_func

    def search(self, key):
        rootFn = os.path.join(self.treeFilePath, 'root.dat')
        curFn = rootFn

        # looking for leaf node
        while not self.isLeaf(curFn):
            # print curFn
            with open(curFn) as curFileobj:
                lines = curFileobj.readlines()
                thresholdLis = eval(lines[1].strip())
                if thresholdLis[0].isdigit():
                    thresholdLis = map(lambda x: int(x), thresholdLis)
                slotId = self.getSlotId(key, thresholdLis)
                # print key, thresholdLis, slotId
                curFn = lines[2 + slotId].strip()

        # looking for table file in the leaf node
        with open(curFn) as curFileobj:
            lines = curFileobj.readlines()
            keyLis = map(lambda x: x.strip().split(',')[0], lines[1:])
            # print keyLis
            if keyLis[0].isdigit(): 
                keyLis = map(lambda x: int(x), keyLis)
            if key in keyLis:
                keyIdx = keyLis.index(key)
                tableFn = lines[1 + keyIdx].strip().split(',')[1]
                return tableFn
            return ''
    # end_func
# end_class


def test():
    # test leaf
    """
    tableFileInfoLis = [
        (4, r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_b\data\state\state_000003.dat'),
        ]
    leafNodeFn = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage3_a\data\test\leaf1.dat'
    leaf1 = LeafNode(tableFileInfoLis, leafNodeFn)
    tableFileInfoLis = [
        (41, r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage2_b\data\state\state_000002.dat'),
        ]
    leafNodeFn = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage3_a\data\test\leaf2.dat'
    leaf2 = LeafNode(tableFileInfoLis, leafNodeFn)
    """

    # test non-leaf
    """
    nodeLis = [leaf1, leaf2]
    nonLeafNodeFn = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage3_a\data\test\nonLeaf1.dat'
    nonLeaf1 = NonLeafNode(nodeLis, nonLeafNodeFn)
    """

    # test B+ tree
    treeFilePath = r'D:\Dropbox\UNL\class\CSCE811 - Data Modeling\solution\hw3\stage3_a\data\test'
    fanout = 200
    tableFileInfoLis = [
        (1, 'a1'),
        (2, 'a2'),
        (3, 'a3'),
        (4, 'a4'),
        (5, 'a5'),
        (6, 'a6'),
        (7, 'a7'),
        (8, 'a8'),
        (9, 'a9'),
        (10, 'a10'),
        (11, 'a11'),
        (12, 'a12'),
        (13, 'a13'),
        (14, 'a14'),
        (15, 'a15'),
        (16, 'a16'),
        (17, 'a17'),
        (18, 'a18'),
        (19, 'a19'),
        (20, 'a20'),
        (21, 'a21'),
        (22, 'a22'),
        (23, 'a23'),
        (24, 'a24'),
        (25, 'a25'),
        (26, 'a26'),
        (27, 'a27'),
        (28, 'a28'),
        (29, 'a29'),
        (30, 'a30'),
        (31, 'a31'),
        (32, 'a32'),
        (33, 'a33'),
        (34, 'a34'),
        (35, 'a35'),
    ]
    bpTree = BplusTree(treeFilePath, fanout)
    bpTree.buildTree(tableFileInfoLis[:10])
    print bpTree.search(5)

# end_test


def main():
    test()
# end_main


if __name__ == "__main__":
    main()
# end_if
