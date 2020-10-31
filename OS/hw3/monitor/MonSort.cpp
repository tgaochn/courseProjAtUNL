// MonSort.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Fri, 07/31/2020, 02:10

#include "MonSort.h"
#include "utils.h"

#define N 4
#define TOTALPHASE int(floor((2 * log(N) / log(2)) + 0.5) + 1)

int **Mat;

class monitor
{
public:
    pthread_mutex_t condlock;
    pthread_cond_t cond[N];
    bool ready = false;

    int totalPhase = int(floor((2 * log(N) / log(2)) + 0.5) + 1);
    bool isRowSortPhase = true;
    bool isInv = false;
    int curPhase = 0;
    int i = 0;

    monitor()
    {
        pthread_mutex_init(&condlock, NULL);
        for (int i = 0; i < N; i++)
        {
            pthread_cond_init(&cond[i], NULL);
        }
    }

    void monSort(int threadId)
    {

        while (1)
        {
            if (threadId == i % N)
            {
                pthread_mutex_lock(&condlock);
                while (!ready)
                    pthread_cond_wait(&cond[threadId], &condlock);
                curPhase = i / N;
                isRowSortPhase = curPhase % 2 == 0 ? true : false;
                isInv = isRowSortPhase && threadId % 2;
                if (isRowSortPhase)
                {

                    sortMatRow(Mat, threadId, N, isInv);
                }
                else
                {
                    sortMatCol(Mat, threadId, N, isInv);
                }

                // cout << i << "\tthread: " << threadId << "\tphase: " << curPhase << "\tisRowSortPhase: " << isRowSortPhase << "\tisInv: " << isInv << endl;
                cout << " ";
                i++;

                if (i % N == 0)
                {
                    cout << "matrix in phase:" << curPhase + 1 << endl;
                    printMat(Mat, N, N);
                }

                pthread_cond_signal(&cond[(threadId + 1) % N]);
                pthread_mutex_unlock(&condlock);

                if (i >= TOTALPHASE * N)
                {
                    break;
                }
            }
        }
    }
} M;

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
    Mat = loadMat("input.txt", N, N);
    cout << "original matrix:" << endl;
    printMat(Mat, N, N);

    for (int i = 0; i < N; i++)
    {
        threadInput[i].threadId = i;

        int ret = pthread_create(&thread[i], NULL, threadCall, (void *)&(threadInput[i]));
        if (ret != 0)
        {
            cout << "pthread_create error : error_code = " << ret << endl;
        }
    }

    M.ready = true;
    pthread_cond_signal(&M.cond[0]);

    for (int i = 0; i < N; i++)
    {
        pthread_join(thread[i], NULL);
        pthread_cond_destroy(&M.cond[i]);
    }

    pthread_mutex_destroy(&M.condlock);
    pthread_exit(NULL);
}

void runTest()
{
    pthread_t thread[N];
    struct threadPara threadInput[N];
    Mat = loadMat("input.txt", N, N);
    cout << "original matrix:" << endl;
    printMat(Mat, N, N);

    for (int i = 0; i < N; i++)
    {
        threadInput[i].threadId = i;

        int ret = pthread_create(&thread[i], NULL, threadCall, (void *)&(threadInput[i]));
        if (ret != 0)
        {
            cout << "pthread_create error : error_code = " << ret << endl;
        }
    }

    pthread_cond_signal(&M.cond[0]);
    M.ready = true;

    for (int i = 0; i < N; i++)
    {
        pthread_join(thread[i], NULL);
    }

    for (int i = 0; i < N; i++)
    {
        pthread_cond_destroy(&M.cond[i]);
    }
    pthread_mutex_destroy(&M.condlock);
    pthread_exit(NULL);
}

void *threadCall(void *args)
{
    struct threadPara *input;
    input = (struct threadPara *)args;
    M.monSort(input->threadId);
}
