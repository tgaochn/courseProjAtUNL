#!/usr/bin/env python
# coding:utf8

import sys

class NFA:
    stateSet = set()
    startState = 0
    finalStateSet = set()
    transFunc = dict()

    def __init__(self, stateSet=set([0]), startState=0, finalStateSet=set([0]), transFunc=dict()):
        self.stateSet = stateSet
        self.startState = startState
        self.finalStateSet = finalStateSet
        self.transFunc = transFunc #{(inputState, inputChar):set(outputStateSet)}
    #end_init

    def AdjustNFA(self, delta):
        '''
        adjust states, startstate, finalstates and transfunction by adding delta to every state
        '''
        self.stateSet = self.GetAdjustedStateSet(delta)
        self.startState = self.GetAdjustedStartState(delta)
        self.finalStateSet = self.GetAdjustedFinalStateSet(delta)
        self.transFunc = self.GetAdjustedTransFunc(delta)
    #end_func
        

    def GetAdjustedStartState(self, delta):
        '''
        Give start state a new index by adding delta
        :param delta:
        :return: adjusted start state with a new index
        '''
        return self.startState + delta
    #end_func

    def GetAdjustedStateSet(self, delta):
        '''
        Give every state a new index by adding delta
        :param delta:
        :return: adjusted state with a new index
        '''
        adjustedStateSet= set([ele + delta for ele in self.stateSet])
        return adjustedStateSet
    #end_func

    def GetAdjustedFinalStateSet(self, delta):
        '''
        Give every final state a new index by adding delta
        :param delta:
        :return: adjusted final state with a new index
        '''
        adjustedFinalStateSet = set([ele + delta for ele in self.finalStateSet])
        return adjustedFinalStateSet
    #end_func

    def GetAdjustedTransFunc(self, delta):
        '''
        Give every state in transFunc a new index by adding delta
        :param delta:
        :return: adjusted transFunc with a new index
        '''
        adjustedTransFunc = dict()
        for (inputState, curInputChar),outputStateSet in self.transFunc.iteritems():
            newOutputStateSet = set([ele + delta for ele in outputStateSet])
            adjustedTransFunc.setdefault((inputState + delta, curInputChar),newOutputStateSet)
        return adjustedTransFunc
    #end_func

    def Conc(self, NFA2):
        '''
        Concatenate two NFA.
        :param NFA2:
        :return: new NFA after concatenation
        '''
        NFA1 = self
        NFA1StateCnt = len(NFA1.stateSet)
        newNFAStateSet = NFA1.stateSet | NFA2.GetAdjustedStateSet(NFA1StateCnt)
        newNFAStartState = NFA1.startState
        newNFAFinalStateSet = NFA2.GetAdjustedFinalStateSet(NFA1StateCnt)
        newNFATransFunc = dict()
        for (inputState, curInputChar),outputStateSet in self.transFunc.iteritems():
            newNFATransFunc.setdefault((inputState, curInputChar), outputStateSet)
        adjustedNFA2TransFunc = NFA2.GetAdjustedTransFunc(NFA1StateCnt)
        for (inputState, curInputChar),outputStateSet in adjustedNFA2TransFunc.iteritems():
            newNFATransFunc.setdefault((inputState, curInputChar), outputStateSet)
        for inputState in self.finalStateSet:
            newNFATransFunc.setdefault((inputState, 'e'), set())
            newNFATransFunc[(inputState, 'e')].add(NFA2.startState + NFA1StateCnt)

        newNFA = NFA(newNFAStateSet, newNFAStartState, newNFAFinalStateSet, newNFATransFunc)
        return newNFA
    #end_func

    def Union(self, NFA2):
        '''
        Unionize two NFAs.
        :param NFA2:
        :return: new NFA after union
        '''
        NFA1 = self
        NFA1StateCnt = len(NFA1.stateSet)
        totalStateCnt = NFA1StateCnt + len(NFA2.stateSet)
        newNFAStateSet = NFA1.stateSet | NFA2.GetAdjustedStateSet(NFA1StateCnt)
        newNFAStateSet.add(totalStateCnt)
        newNFAStartState = totalStateCnt
        newNFAFinalStateSet = NFA1.finalStateSet | NFA2.GetAdjustedFinalStateSet(NFA1StateCnt)
        newNFATransFunc = dict()
        for (inputState, curInputChar),outputStateSet in self.transFunc.iteritems():
            newNFATransFunc.setdefault((inputState, curInputChar), outputStateSet)
        adjustedNFA2TransFunc = NFA2.GetAdjustedTransFunc(NFA1StateCnt)
        for (inputState, curInputChar),outputStateSet in adjustedNFA2TransFunc.iteritems():
            newNFATransFunc.setdefault((inputState, curInputChar), outputStateSet)
        newNFATransFunc.setdefault((newNFAStartState, 'e'), set())
        newNFATransFunc[(newNFAStartState, 'e')].add(NFA1.startState)
        newNFATransFunc[(newNFAStartState, 'e')].add(NFA2.GetAdjustedStartState(NFA1StateCnt))

        newNFA = NFA(newNFAStateSet, newNFAStartState, newNFAFinalStateSet, newNFATransFunc)
        return newNFA
    #end_func

    def Star(self):
        '''
        Get star of a NFA.
        :return: new NFA after star operation
        '''
        stateCnt = len(self.stateSet)
        newNFATransFunc = self.transFunc
        newNFATransFunc.setdefault((stateCnt, 'e'), set([self.startState]))
        for finalState in self.finalStateSet:
            newNFATransFunc.setdefault((finalState, 'e'), set())
            newNFATransFunc[(finalState, 'e')].add(self.startState)
        newNFAStateSet = self.stateSet
        newNFAStateSet.add(stateCnt)
        newNFAStartState = stateCnt
        newNFAFinalStateSet = self.finalStateSet
        newNFAFinalStateSet.add(stateCnt)

        newNFA = NFA(newNFAStateSet, newNFAStartState, newNFAFinalStateSet, newNFATransFunc)
        return newNFA
    #end_func

    def ShowNFA(self):
        '''
        Print the structure of NFA
        '''
        print '=' * 40
        print "stateSet is %s " % self.stateSet
        print "startState is %s " % self.startState
        print "finalStateSet is %s " % self.finalStateSet
        print "transFunc is "
        transFuncKeys = sorted(self.transFunc.keys())
        for inputState, inputChar in transFuncKeys:
            print "%s with %s ---> %s" % (inputState, inputChar, self.transFunc[(inputState, inputChar)])
        print '=' * 40
    #end_func

    def ShowNFAFromStartState(self):
        '''
        Print the structure of NFA
        '''
        print '=' * 40
        print "stateSet is %s " % self.stateSet
        print "startState is %s " % self.startState
        print "finalStateSet is %s " % self.finalStateSet
        print "transFunc is "
        exploredStateSet = set()
        stateQueue = []
        stateQueue.append(self.startState)
        while stateQueue:
            inputState = stateQueue[0]
            stateQueue = stateQueue[1:]
            if inputState in exploredStateSet: continue
            exploredStateSet.add(inputState)
            for inputChar in ['e', 'a', 'b']:
                if (inputState, inputChar) not in self.transFunc:continue
                outputStateSet = self.transFunc[(inputState, inputChar)]
                print "%s with %s ---> %s" % (inputState, inputChar, outputStateSet)
                for outputState in outputStateSet:
                    stateQueue.append(outputState)
        print '=' * 40
    #end_func
#end_class

def GetInput(input):
    inputStringLis = []
    REString = input.readline().strip()
    for line in input:
        inputString = line.strip()
        inputStringLis.append(inputString)
    return REString, inputStringLis
#end_func

def RE2NFAOnlyWithStar(REString):
    '''
    handle REString which has only a, b, *
    '''
    curNFA = None
    strLen = len(REString)
    for idx, curChar in enumerate(REString):
        if curChar == '*' : continue

        newStateSet = set([0, 1])
        newStartState = 0
        newFinalStateSet = set([1])
        newTransFunc = {(0, curChar):set([1])}
        newNFA = NFA(newStateSet, newStartState, newFinalStateSet, newTransFunc)

        if curNFA is None:
            if idx == strLen - 1 or REString[idx + 1] != '*': #list is over or next char is a or b.
              curNFA = newNFA
            else: #next char is *
                curNFA = newNFA.Star()
        else:
            if idx == strLen - 1 or REString[idx + 1] != '*': #list is over or next char is a or b.
                curNFA = curNFA.Conc(newNFA)
            else: #next char is *
                curNFA = curNFA.Conc(newNFA.Star())
    return curNFA
#end_func

def RE2NFAOnlyWithStarUnion(REString):
    '''
    handle REString which has only a, b, *, |
    '''
    curNFA = None
    substringLis = REString.split('|')
    for substring in substringLis:
        tmpNFA = RE2NFAOnlyWithStar(substring)
        if curNFA is None:
            curNFA = tmpNFA
        else:
            curNFA = curNFA.Union(tmpNFA)
    return curNFA
#end_func

def ParseBrac(curString):
    '''
    input a string, output 2 indexes with which the string can be divided into 3 part.
    only output the outest brackets
    only output the leftest brackets
    eg.
    aa(b(aaa)b)aa(aa)b -> 2, 10
    '''
    sepIdx1 = -1
    sepIdx2 = -1
    bracStack = []
    for idx, curChar in enumerate(curString): 
        if curChar == '(':
            bracStack.append(curChar)
            sepIdx1 = idx if sepIdx1 == -1 else sepIdx1 # find the first (
        if curChar == ')': # find the ) which associates the first (
            bracStack.pop()
            if not bracStack:
                sepIdx2 = idx
                break
    return sepIdx1, sepIdx2
#end_func

def RE2NFA(REString):
    '''
    L0 : may contain (, ), |, *, a, b, e
    L1 : may contain |, *, a, b, e
    L2 : may contain *, a, b, e
    L3 : only contain a, b, e
    Seperate the string into 3(or 2) parts and recurse.
    '''
    if '(' not in REString: return RE2NFAOnlyWithStarUnion(REString)
    idx1, idx2 = ParseBrac(REString)

    NFA1 = NFA()
    NFA3 = NFA()
    oper1 = 'c' # operator between NFA1 and NFA2
    oper2 = 'c' # operator between NFA2 and NFA3
    headString = REString[:idx1]
    midString = REString[idx1 + 1:idx2]
    tailString = REString[idx2 + 1:]

    if headString: # skip case : (ab)a
        if headString[-1] == '|':
            oper1 = '|'
            headString = headString[:-1]
        NFA1 = RE2NFA(headString)

    NFA2 = RE2NFA(midString)
    if tailString and tailString[0] == '*': # case (ab)*b
        NFA2 = NFA2.Star()
        tailString = tailString[1:]
        if tailString and tailString[0] == '|':# case (ab)*|b
            oper2 = '|'
            tailString = tailString[1:]
    elif tailString and tailString[0] == '|': # case (ab)|(ba)
        oper2 = '|'
        tailString = tailString[1:]

    if tailString: # skip case : a(ab), only 2 parts
        NFA3 = RE2NFA(tailString)

    finalNFA = NFA1 
    if oper1 == '|': finalNFA = finalNFA.Union(NFA2)
    if oper1 == 'c': finalNFA = finalNFA.Conc(NFA2)
    if oper2 == '|': finalNFA = finalNFA.Union(NFA3)
    if oper2 == 'c': finalNFA = finalNFA.Conc(NFA3)

    return finalNFA
#end_func

def GetAllReachedableStateWithE(curNFA, stateSet):
    reachedableStateSet = set()
    exploredStateSet = set()
    stateStack = []
    stateStack.extend(stateSet)
    while stateStack:
        ele = stateStack.pop()
        if ele in exploredStateSet: continue
        exploredStateSet.add(ele)
        reachedableStateSet.add(ele)
        eReachedStateSet = curNFA.transFunc.get((ele, 'e'), set())
        stateStack.extend(eReachedStateSet)
    return exploredStateSet
#end_func


def test():
    REString = "((a|b)*aa(a|b)*aba(a|b)*)|((a|b)*aba(a|b)*aa(a|b)*)|((a|b)*aaba(a|b)*)"
    print REString
    print '=' * 40
    curNFA = RE2NFA(REString)
    #curNFA = NFA2DFA(curNFA)
    curNFA.ShowNFAFromStartState()
    #print SingleStringCheckMatch(curDFA, 'abbabb')
#end_func


def ConstructDFA(stateSet, startState, finalStateSet, transFunc):
    '''
    Reconstruct a DFA by rebuild the state index
    '''
    idxMap = {}
    for newIdx, oldState in enumerate(stateSet):
        idxMap[oldState] = newIdx

    DFAStateSet = set(range(len(stateSet)))
    DFAStartState = idxMap[startState]
    DFAFinalStateSet = set([idxMap[ele] for ele in finalStateSet])
    DFATransFunc = {}
    for (inputState, inputChar), outputStateSet in transFunc.iteritems():
        DFATransFunc[(idxMap[inputState], inputChar)] = set([idxMap[outputStateSet]])
        DFATransFunc[(idxMap[inputState], 'e')] = set([idxMap[inputState]])
        
    curDFA = NFA(DFAStateSet, DFAStartState, DFAFinalStateSet, DFATransFunc)
    return curDFA
#end_func

def Set2Str(curSet):
    return str(sorted(list(curSet)))
#end_func

def NFA2DFA(curNFA):
    DFAStartState = set()
    DFAFinalState = set()
    DFAStateSet = set()
    DFATransFunc = dict()
    stateSetStack = [GetAllReachedableStateWithE(curNFA, set([curNFA.startState]))] # states in DFA, indexing form is original NFA
    exploredStateSet = set()
    while stateSetStack:
        curStateSet = stateSetStack.pop()
        if not DFAStartState:DFAStartState = curStateSet
        if curStateSet.intersection(curNFA.finalStateSet): DFAFinalState.add(Set2Str(curStateSet))
        DFAStateSet.add(Set2Str(curStateSet))
        outputStateSet1 = set() # 2 output sets of inputStateSet when current input is a or b
        outputStateSet2 = set()
        inputStateSet = GetAllReachedableStateWithE(curNFA, curStateSet)

        for curState in inputStateSet:
            curOutputStateSet = curNFA.transFunc.get((curState, 'a'), set())
            outputStateSet1 = outputStateSet1 | curOutputStateSet
            curOutputStateSet = curNFA.transFunc.get((curState, 'b'), set())            
            outputStateSet2 = outputStateSet2 | curOutputStateSet

        eReachedStateSet = GetAllReachedableStateWithE(curNFA, outputStateSet1)
        outputStateSet1 = outputStateSet1 | eReachedStateSet
        eReachedStateSet = GetAllReachedableStateWithE(curNFA, outputStateSet2)
        outputStateSet2 = outputStateSet2 | eReachedStateSet
        DFATransFunc[(Set2Str(inputStateSet), 'a')] = Set2Str(outputStateSet1)
        DFATransFunc[(Set2Str(inputStateSet), 'b')] = Set2Str(outputStateSet2)
        
        exploredStateSet.add(Set2Str(curStateSet))
        if Set2Str(outputStateSet1) not in exploredStateSet:
            exploredStateSet.add(Set2Str(outputStateSet1))
            stateSetStack.append(outputStateSet1)
        if Set2Str(outputStateSet2) not in exploredStateSet:
            exploredStateSet.add(Set2Str(outputStateSet2))
            stateSetStack.append(outputStateSet2)
    #end_while
    curDFA = ConstructDFA(DFAStateSet, Set2Str(DFAStartState), DFAFinalState, DFATransFunc)
    return curDFA
#end_func

def CheckMatch(curDFA, inputStringLis):
    rltLis = []
    for inputString in inputStringLis:
        rlt = SingleStringCheckMatch(curDFA, inputString)
        rltLis.append(rlt)
    return rltLis
#end_func

def SingleStringCheckMatch(curDFA, inputString):
    curState = curDFA.startState
    for inputChar in inputString:
        curState = list(curDFA.transFunc[(curState, inputChar)])[0] # the value in this dict(output state) is a set with only ONE element
    rlt = True if curState in curDFA.finalStateSet else False
    return rlt
#end_func

def CheckRlt(rltLis, outputFn):
    rltMap = {'yes' : True, 'no' : False}
    print 'Checking file : %s' % outputFn
    for lineId, line in enumerate(open(outputFn)):
        line = line.strip()
        if not line: continue
        if rltMap[line] == rltLis[lineId]:
            print 'line %s : my result is %s, Correct!' % (lineId + 1, rltLis[lineId])
        else:
            print 'line %s : my result is %s, Wrong!' % (lineId + 1, rltLis[lineId])
#end_def

def REMatch():
    for i in xrange(1):
        inputFn = "q%s.txt" % (i + 1)
        outputFn = "a%s.txt" % (i + 1)
        inputF = open(inputFn)
        REString, inputStringLis = GetInput(inputF)
        print REString
        curNFA = RE2NFA(REString)
        curDFA = NFA2DFA(curNFA)
        rltLis = CheckMatch(curDFA, inputStringLis)
        CheckRlt(rltLis, outputFn)
        print '=' * 40
#end_func

def PrintRlt(rltLis):
    rltMap = {True:'yes', False:'no'}
    for rlt in rltLis:
        rlt = rltMap.get(rlt, 'yes')
        print rlt
#end_func

def REMatchReadingStdin():
    REString, inputStringLis = GetInput(sys.stdin)
    curNFA = RE2NFA(REString)
    curDFA = NFA2DFA(curNFA)
    rltLis = CheckMatch(curDFA, inputStringLis)
    PrintRlt(rltLis)
#end_func

def main():
    REMatch()
    #test()
#end_main

if __name__ == "__main__":
    main()
# end_if
