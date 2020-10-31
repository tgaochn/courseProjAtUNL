#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ProjectName:

Author:
    Tian Gao
Email:
    tgaochn@gmail.com
CreationDate:
    10/23/2017
Description:

"""
def func2():
    dayLis = ['PAm', 'PAtu', 'PAw', 'PAth', 'PAf',
                'PRm', 'PRtu', 'PRw', 'PRth', 'PRf']
    outputLis = []

    for day1 in dayLis:
        for day2 in dayLis:
            if day1[:2] == day2[:2]: continue
            if day1[2:] >= day2[2:]: continue
            # if day1 > day2: continue
            clause = '%s \\wedge %s' % (day1, day2)
            outputLis.append(clause)

    outputStr = ')\\vee ('.join(outputLis)
    outputStr = '$(%s)$' % outputStr
    print len(outputLis)
    print outputStr

#end_func

def func3():
    stateLis = ['NE', 'IA', 'KS', 'MO']
    colorLis = ['r', 'g', 'b']

    outputLis1 = []
    for state in stateLis:
        clause = '(%sr \\wedge \\neg %sg \\wedge \\neg %sb) \\vee (\\neg %sr \\wedge %sg \\wedge \\neg %sb) \\vee (\\neg %sr \\wedge \\neg %sg \\wedge %sb)' % tuple([state] * 9)
        outputLis1.append(clause)

    outputStr1 = ')\\wedge ('.join(outputLis1)
    outputStr1 = '(%s)' % outputStr1

    outputLis2 = []
    for color in colorLis:
        clause = '((NE%s \\rightarrow (\\neg IA%s \\wedge \\neg KS%s))\\wedge (IA%s \\rightarrow (\\neg NE%s \\wedge \\neg MO%s))\\wedge (KS%s \\rightarrow (\\neg NE%s \\wedge \\neg MO%s))\\wedge (MO%s \\rightarrow (\\neg NE%s \\wedge \\neg IA%s \\wedge \\neg KS%s)))' % tuple([color] * 13)
        outputLis2.append(clause)

    outputStr2 = ')\\wedge ('.join(outputLis2)
    outputStr2 = '(%s)' % outputStr2

    print '$%s$' % outputStr1
    print '$%s$' % outputStr2
    print '$%s \\wedge %s$' % (outputStr1, outputStr2)



#end_func


def func4():
    boolLis = [False, True]
    boolMap = {False: 0, True: 1}

    for d in boolLis:
        for c in boolLis:
            for b in boolLis:
                for a in boolLis:
                    var1 = b or c
                    var2 = (not a) or (not b) or (not c) or (not d)
                    var3 = ((not a) or b) and a and (not b) and c and d
                    # print boolMap[a], boolMap[b], boolMap[c], boolMap[d], boolMap[var1]
                    # print boolMap[a], boolMap[b], boolMap[c], boolMap[d], boolMap[var2]
                    print boolMap[a], boolMap[b], boolMap[c], boolMap[d], boolMap[var3]
#end_func


def func6():
    boolLis = [False, True]
    boolMap = {False: 0, True: 1}

    for a in boolLis:
        for b in boolLis:
            var1 = (not a) or b
            var2 = (not ((not a) or b)) or (a or (not b))
            var3 = a or b or (not b)
            # print '%s & %s & %s \\\\ \\hline' % (boolMap[a], boolMap[b], boolMap[var1])
            # print '%s & %s & %s \\\\ \\hline' % (boolMap[a], boolMap[b], boolMap[var2])
            # print '%s & %s & %s \\\\ \\hline' % (boolMap[a], boolMap[b], boolMap[var3])

    for a in boolLis:
        for b in boolLis:
            for c in boolLis:
                # var1 = (not (a or b) or c) == (((not a) or c) or ((not b) or c))
                var2 = a and (b or c)
                # print '%s & %s & %s & %s \\\\ \\hline' % (boolMap[a], boolMap[b], boolMap[c], boolMap[var1])
                print '%s & %s & %s & %s \\\\ \\hline' % (boolMap[a], boolMap[b], boolMap[c], boolMap[var2])
#end_func



def main():
    # func2()
    # func3()
    # func4()
    # func5()
    func6()
#end_main

if __name__ == "__main__":
    main()
#end_if
