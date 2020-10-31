// SemSort.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Fri, 07/31/2020, 02:10

#include "SemSort.h"
#include "utils.h"

#define N 4

int **Mat;
sem_t Sem[N];

int main(int argc, char **argv)
{
    // runTest();
    runHw3();

    return 0;
}

void runHw3()
{
    pthread_t thread[N];
    struct threadPara threadInput[N];
    int semInitVal;
    void *status;
    int rc;

    Mat = loadMat("input.txt", N, N);
    cout << "original matrix:" << endl;
    printMat(Mat, N, N);

    for (int i = 0; i < N; i++)
    {
        semInitVal = i == 0 ? 1 : 0;
        sem_init(&Sem[i], 0, semInitVal);
        threadInput[i].threadId = i;

        int ret = pthread_create(&thread[i], NULL, threadCall, (void *)&(threadInput[i]));
        if (ret != 0)
        {
            cout << "pthread_create error : error_code = " << ret << endl;
        }
    }

    for (int i = 0; i < N; i++)
    {
        pthread_join(thread[i], NULL); 
    }

    pthread_exit(NULL);
}

void runTest()
{
    pthread_t thread[N];
    struct threadPara threadInput[N];
    int semInitVal;
    Mat = loadMat("input.txt", N, N);
    cout << "original matrix:" << endl;
    printMat(Mat, N, N);

    // insertionSort(Mat[0], N);
    // printMat(Mat, N, N);
    // insertionSort(Mat[1], N, true);
    // printMat(Mat, N, N);
    // invMat(Mat, N);
    // printMat(Mat, N, N);
    // invMat(Mat, N);
    // insertionSort(Mat[0], N);
    // invMat(Mat, N);
    // sortMatRow(Mat, 0, N);
    // printMat(Mat, N, N);
    // sortMatRow(Mat, 1, N, true);
    // printMat(Mat, N, N);
    // sortMatCol(Mat, 0, N);
    // printMat(Mat, N, N);
    // sortMatCol(Mat, 1, N, true);
    // printMat(Mat, N, N);
    // sortMatAllRow(Mat, N);
    // printMat(Mat, N, N);
    // sortMatAllCol(Mat, N);
    // printMat(Mat, N, N);

    for (int i = 0; i < N; i++)
    {
        semInitVal = i == 0 ? 1 : 0;
        sem_init(&Sem[i], 0, semInitVal);
        threadInput[i].threadId = i;

        int ret = pthread_create(&thread[i], NULL, threadCall, (void *)&(threadInput[i]));
        if (ret != 0)
        {
            cout << "pthread_create error : error_code = " << ret << endl;
        }
    }

    pthread_exit(NULL);
}

void *threadCall(void *args)
{
    struct threadPara *input;
    bool isRowSortPhase, isInv;
    int phaseCnt = int(floor((2 * log(N) / log(2)) + 0.5) + 1);
    int semId;
    input = (struct threadPara *)args;

    for (int curPhase = 0; curPhase < phaseCnt; curPhase++)
    {
        sem_wait(&Sem[input->threadId]);
        isRowSortPhase = curPhase % 2 == 0 ? true : false;
        isInv = isRowSortPhase && input->threadId % 2;

        if (isRowSortPhase)
        {
            sortMatRow(Mat, input->threadId, N, isInv);
        }
        else
        {
            sortMatCol(Mat, input->threadId, N, isInv);
        }

        if (input->threadId == N - 1)
        {
            // printSemLis(Sem, N);
            cout << "matrix in phase:" << curPhase + 1 << endl;
            printMat(Mat, N, N);
        }

        semId = (input->threadId + 1) % N;
        sem_post(&Sem[semId]);
    }
}
