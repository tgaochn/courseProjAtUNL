// utils.h
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Fri, 07/31/2020, 02:10

#ifndef _SemSort_h_
#define _SemSort_h_

#include <cmath>
#include <iostream>
#include <math.h>
#include <pthread.h>
#include <semaphore.h>

using namespace std;

void runTest();
void runHw3();
void *threadCall(void *args);

struct threadPara
{
    int threadId;
};

#endif