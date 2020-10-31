// utils.h
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Fri, 07/31/2020, 02:10

#ifndef _utils_h_
#define _utils_h_

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <semaphore.h>
#include <stdlib.h>

using namespace std;

#define MAXRANDOMINT 50

void printSemLis(sem_t *sem, int semCnt);
int **loadMat(char *fn, int row, int col);
void sortMatAllRow(int **mat, int rowCnt);
void sortMatAllCol(int **mat, int colCnt);
void sortMatRow(int **mat, int targetRow, int rowCnt, bool inv = false);
void sortMatCol(int **mat, int targetCol, int colCnt, bool inv = false);
void invMat(int **mat, int matSize);
void printMat(int **mat, int row, int col);
int **genMat(int row, int col);
void insertionSort(int *arr, int n, bool inv = false);

#endif