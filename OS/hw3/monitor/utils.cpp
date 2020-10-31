// utils.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Fri, 07/31/2020, 02:10

#include "utils.h"

int **loadMat(char *fn, int row, int col)
{
    // load a matrix from a file

    int **mat;
    FILE *file = fopen(fn, "r");
    mat = (int **)malloc(row * sizeof(int *));

    for (int i = 0; i < row; i++)
    {
        mat[i] = (int *)malloc(col * sizeof(int));
    }

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            fscanf(file, "%d", &mat[i][j]);
        }
    }
    fclose(file);

    return mat;
}

void sortMatAllRow(int **mat, int rowCnt)
{
    for (int i = 0; i < rowCnt; i++)
    {
        bool inv = i % 2 == 0 ? false : true;
        sortMatRow(mat, i, rowCnt, inv);
    }
}

void sortMatAllCol(int **mat, int colCnt)
{
    for (int i = 0; i < colCnt; i++)
    {
        sortMatCol(mat, i, colCnt);
    }
}

void sortMatRow(int **mat, int targetRow, int rowCnt, bool inv)
{
    // sort the targetRow of the matrix

    insertionSort(mat[targetRow], rowCnt, inv);
}

void sortMatCol(int **mat, int targetCol, int colCnt, bool inv)
{
    // sort the targetCol of the matrix

    invMat(mat, colCnt);
    insertionSort(mat[targetCol], colCnt, inv);
    invMat(mat, colCnt);
}

void invMat(int **mat, int matSize)
{
    // inverse the matrix

    int tmp;

    for (int i = 0; i < matSize; i++)
    {
        for (int j = 0; j < matSize; j++)
        {
            if (i < j)
            {
                tmp = mat[i][j];
                mat[i][j] = mat[j][i];
                mat[j][i] = tmp;
            }
        }
    }
}

void printMat(int **mat, int row, int col)
{
    // print the matrix

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < row; j++)
        {
            cout << mat[i][j] << "\t";
        }
        cout << endl;
    }
    cout << endl;
}

int **genMat(int row, int col)
{
    // generate a matrix for testing

    int **mat;
    mat = (int **)malloc(row * sizeof(int *));

    for (int i = 0; i < row; i++)
    {
        mat[i] = (int *)malloc(col * sizeof(int));
    }

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            mat[i][j] = rand() % MAXRANDOMINT;
        }
    }

    return mat;
}

void insertionSort(int *arr, int n, bool inv)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;

        if (inv)
        {
            while (j >= 0 && arr[j] < key)
            {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
        }
        else
        {
            while (j >= 0 && arr[j] > key)
            {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
        }
        arr[j + 1] = key;
    }
}