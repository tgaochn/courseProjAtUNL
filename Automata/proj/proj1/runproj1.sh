#!/bin/bash

score=0
numofcases=10
bonus=bonus

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
        echo "Successfully compiles: 30 points"
        let "score=$score+30"
    else
        echo "Could not compile the code"
        echo "Total score = $score points"
        exit
    fi
    if [ -e Project1.class ] 
    then
        echo "Successfully finds the executable file: 10 points"
        let "score=$score+10"
        cmd="java Project1"
    elif [ -e project1.class ] 
    then
        echo "Successfully finds the executable file: 10 points"
        let "score=$score+10"
        cmd="java project1"
    else
        echo "Could not find class Project1.class"
        echo "Total score = $score points"
        exit
    fi        
    grep java.util.regex *.java
    if [ $? == 0 ]
    then
        echo "You may not use java.util.regex"
        echo "Total score = $score points"
        exit
    fi
    grep package *.java
    if [ $? == 0 ]
    then
        echo "Please remove your own Java package; otherwise \"java Project1\" does not run."
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
        echo "Successfully compiles: 30 points"
        let "score=$score+30"
    else
        echo "Could not compile the code"
        echo "Total score = $score points"
        exit
    fi
    if [ -e project1 ] 
    then
        echo "Successfully finds the executable file: 10 points"
        let "score=$score+10"
        cmd="./project1"
    elif [ -e Project1 ] 
    then
        echo "Successfully finds the executable file: 10 points"
        let "score=$score+10"
        cmd="./Project1"
    else
        echo "Could not find executable file project1"
        echo "Total score = $score points"
        exit
    fi        
    grep "<regex>" *.c*
    if [ $? == 0 ]
    then
        echo "You may not use <regex>"
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
    wget -q http://cse.unl.edu/~xu/courses/automata/proj1/$inputfile -O $inputfile
    if [ $? != 0 ]
    then
        echo "Could not download $inputfile from cse, please contact the instructor"
        exit
    fi
    wget -q http://cse.unl.edu/~xu/courses/automata/proj1/$outputfile -O $outputfile
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
        # remove possible punctuation and empty lines, add line numbers
        cat projectoutput.txt | grep '\S' | head -n 6 | nl > projectoutput_nl.txt
        cat $outputfile | grep '\S' | head -n 6 | nl > correctoutput_nl.txt
        # do not care about white spaces, do not care about cases
        wrong=$(diff -i -w -y --suppress-common-lines projectoutput_nl.txt correctoutput_nl.txt | wc -l)
        let "correct=6-$wrong"
        echo "Testcase $i:  Number of correct outputs:" $correct " points"
        let "score=$score+$correct"
    else
        echo "Testcase $i:  Runing longer than 15 seconds. Terminated."
    fi
done

# test the bonus testcase

inputfile="q$bonus.txt"
outputfile="a$bonus.txt"
    wget -q http://cse.unl.edu/~xu/courses/automata/proj1/$inputfile -O $inputfile
    if [ $? != 0 ]
    then
        echo "Could not download $inputfile from cse, please contact the instructor"
        exit
    fi
    wget -q http://cse.unl.edu/~xu/courses/automata/proj1/$outputfile -O $outputfile
    if [ $? != 0 ]
    then
        echo "Could not download $outputfile from cse, please contact the instructor"
        exit
    fi
    timeout 15s $cmd < $inputfile > projectoutput.txt
    if [ $? != 124 ]
    then
        cat projectoutput.txt | grep '\S' | head -n 6 | nl > projectoutput_nl.txt
        cat $outputfile | grep '\S' | head -n 6 | nl > correctoutput_nl.txt
        wrong=$(diff -i -w -y --suppress-common-lines projectoutput_nl.txt correctoutput_nl.txt | wc -l)
        if [ $wrong == 0 ]
        then
            /usr/bin/time -f "%U\n%S\n" -o time.txt $cmd <$inputfile > projectoutput.txt
            timeresult=( $(cat time.txt) )
            totaltime1=$(echo "${timeresult[0]}+${timeresult[1]}" | bc)
            /usr/bin/time -f "%U\n%S\n" -o time.txt $cmd <$inputfile > projectoutput.txt
            timeresult=( $(cat time.txt) )
            totaltime2=$(echo "${timeresult[0]}+${timeresult[1]}" | bc)
            /usr/bin/time -f "%U\n%S\n" -o time.txt $cmd <$inputfile > projectoutput.txt
            timeresult=( $(cat time.txt) )
            totaltime3=$(echo "${timeresult[0]}+${timeresult[1]}" | bc)
            avgtime=$(echo "scale=2; ($totaltime1+$totaltime2+$totaltime3)/3" | bc)
            echo "Bonus  case:  Number of correct outputs: 6"
            echo "Bonus  case:  Running time of three runs: " $totaltime1"," $totaltime2"," $totaltime3" seconds, respectively"
            echo "Bonus  case:  Average running time: " $avgtime "seconds. No bonus point"

        else
            let "correct=6-$wrong"
            echo "Bonus  case:  Number of correct outputs:" $correct". No bonus points"

        fi
    else
        echo "Bonus  case:  Runing longer than 15 seconds. Terminated."
    fi



echo "Total score = $score points"
