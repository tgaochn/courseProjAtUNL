#!/bin/bash

score=0
numofcases=10

echo "Current directory:" $PWD


# compile the program
javafiles=(*.java)
cfiles=(*.c)
cppfiles=(*.cpp)
if [ -e "${javafiles[0]}" ] 
then
    echo "Java files"
    javac *.java
    if [ $? == 0 ]
    then
        echo "Successfully compiles: 20 points"
        let "score=$score+20"
    else
        echo "Could not compile the code"
        echo "Total score = $score points"
        exit
    fi
    if [ -e Project2.class ] 
    then
        echo "Successfully finds the executable file: 10 points"
        let "score=$score+10"
        cmd="java Project2"
    elif [ -e project2.class ] 
    then
        echo "Successfully finds the executable file: 10 points"
        let "score=$score+10"
        cmd="java project2"
    else
        echo "Could not find class Project2.class"
        echo "Total score = $score points"
        exit
    fi        
    grep package *.java
    if [ $? == 0 ]
    then
        echo "Please remove your own Java package; otherwise \"java Project2\" does not run"
        echo "Total score = $score points"
        exit
    fi
elif [ -e "${cfiles[0]}" ] || [ -e "${cppfiles[0]}" ]
then
    echo "C/C++ files"
    if [ -e makefile ] 
    then
        mv makefile Makefile
    fi
    if [ ! -e Makefile ] 
    then
        echo "Could not find Makefile"
        echo "Total score = $score points"
        exit
    fi
    make
    if [ $? == 0 ]
    then
        echo "Successfully compiles: 20 points"
        let "score=$score+20"
    else
        echo "Could not compile the code"
        echo "Total score = $score points"
        exit
    fi
    if [ -e project2 ] 
    then
        echo "Successfully finds the executable file: 10 points"
        let "score=$score+10"
        cmd="./project2"
    elif [ -e Project2 ] 
    then
        echo "Successfully finds the executable file: 10 points"
        let "score=$score+10"
        cmd="./Project2"
    else
        echo "Could not find executable file project2"
        echo "Total score = $score points"
        exit
    fi        
else
   echo "Could not find Java, C, C++ files in the submitted files:"
   ls
   exit
fi

# download testcase input and output files
for i in $(seq 1 $numofcases)
do
    inputfile="q$i.txt"
    outputfile="a$i.txt"
    wget -q http://cse.unl.edu/~xu/courses/automata/proj2/$inputfile -O $inputfile
    if [ $? != 0 ]
    then
        echo "Could not download $inputfile from cse, please contact the instructor"
        exit
    fi
    wget -q http://cse.unl.edu/~xu/courses/automata/proj2/$outputfile -O $outputfile
    if [ $? != 0 ]
    then
        echo "Could not download $outputfile from cse, please contact the instructor"
        exit
    fi
done

# run the program
for i in $(seq 1 $numofcases)
do
    inputfile="q$i.txt"
    outputfile="a$i.txt"
    timeout 15s $cmd < $inputfile > projectoutput.txt
    if [ $? != 124 ]
    then
        # check the first four lines
        # remove possible empty lines
        cat projectoutput.txt | grep '\S' | head -n 4 > projectoutput_tr1.txt
        cat $outputfile | grep '\S' | head -n 4 > correctoutput_tr1.txt
        # do not care about white spaces, do not care about cases
        wrong1=$(diff -i -w -y --suppress-common-lines projectoutput_tr1.txt correctoutput_tr1.txt | wc -l)
        
        if [ $wrong1 == 0 ]
        then
            # check the fifth line
            # remove possible punctuation and empty lines
            tr -d '[:punct:]' < projectoutput.txt | grep '\S' | tail -n 1 > projectoutput_tr2.txt
            tr -d '[:punct:]' < $outputfile | grep '\S' | tail -n 1 > correctoutput_tr2.txt
            # do not care about white spaces, do not care about cases
            wrong2=$(diff -i -w -y --suppress-common-lines projectoutput_tr2.txt correctoutput_tr2.txt | wc -l)
        else
            wrong2=1
        fi
        
        if [ $wrong1 != 0 ] || [ $wrong2 != 0 ]
        then
            echo "*************** testcase $i ******************"
            echo "----- The correct output -----"
            cat $outputfile
            echo "----- Your output -----"
            cat projectoutput.txt
        fi

        correct=$(echo "(7-$wrong1-3*$wrong2)" | bc)
        
        echo "Testcase $i:  " $correct " points"
        let "score=$score+$correct"
    else
        echo "Testcase $i:  Runing longer than 15 seconds. Terminated."
    fi
done



echo "Total score = $score points"
