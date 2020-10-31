// main.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Sun, 08/02/2020, 00:56

#include <iostream>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define N 5
using namespace std;

struct threadPara
{
    int threadId;
};

class monitor
{
private:
public:
    pthread_cond_t canPrint1;
    pthread_cond_t canPrint2;
    pthread_cond_t cond[2];

    pthread_mutex_t condlock;
    bool ready = false;
    int count = 0;

    monitor()
    {
        pthread_mutex_init(&condlock, NULL);
        pthread_cond_init(&canPrint1, NULL);
        pthread_cond_init(&canPrint2, NULL);

        pthread_cond_init(&cond[0], NULL);
        pthread_cond_init(&cond[1], NULL);
    }

    void print1()
    {
        static int i = 0;
        while (1)
        {
            if ((i / 2) % 2 == 0)
            {
                if (count % 2 == 0)
                {
                    pthread_mutex_lock(&condlock);
                    while (!ready)
                        pthread_cond_wait(&canPrint2, &condlock);

                    count++;
                    i++;
                    cout << "thread1 \tphase1_" << i << endl;

                    pthread_cond_signal(&canPrint1);
                    pthread_mutex_unlock(&condlock);
                }
            }
            else
            {
                if (count % 2 == 0)
                {
                    pthread_mutex_lock(&condlock);
                    while (!ready)
                        pthread_cond_wait(&canPrint2, &condlock);

                    count++;
                    i++;
                    cout << "thread1 \tphase2_" << i << endl;

                    pthread_cond_signal(&canPrint1);
                    pthread_mutex_unlock(&condlock);
                }
            }
            if (count >= 10)
                break;
        }
    }

    void print2()
    {
        static int i = 0;
        while (1)
        {
            if ((i / 2) % 2 == 1)
            {

                if (count % 2 == 1)
                {
                    pthread_mutex_lock(&condlock);
                    while (!ready)
                        pthread_cond_wait(&canPrint1, &condlock);

                    count++;
                    i++;
                    cout << "thread2 \tphase1_" << i << endl;

                    pthread_cond_signal(&canPrint2);
                    pthread_mutex_unlock(&condlock);
                }
            }
            else
            {

                if (count % 2 == 1)
                {
                    pthread_mutex_lock(&condlock);
                    while (!ready)
                        pthread_cond_wait(&canPrint1, &condlock);

                    count++;
                    i++;
                    cout << "thread2 \tphase2_" << i << endl;

                    pthread_cond_signal(&canPrint2);
                    pthread_mutex_unlock(&condlock);
                }
            }
            if (count >= 10)
                break;
        }
    }

    void print(int pid)
    {
        static int i = 0;

        while (1)
        {
            if (i % 2 == 1)
            {
                pthread_mutex_lock(&condlock);
                while (!ready)
                    pthread_cond_wait(&cond[0], &condlock);

                cout << "thread_1 " << pid << "\t" << i << endl;
                i++;

                pthread_cond_signal(&cond[1]);
                pthread_mutex_unlock(&condlock);
            }
            else
            {
                pthread_mutex_lock(&condlock);
                while (!ready)
                    pthread_cond_wait(&cond[1], &condlock);

                cout << "thread_2 " << pid << "\t" << i << endl;
                i++;

                pthread_cond_signal(&cond[0]);
                pthread_mutex_unlock(&condlock);
            }

            if (i >= 10)
            {
                break;
            }
        }
    }
} M;

void *Func_p1(void *arg)
{
    M.print1();
}

void *Func_p2(void *arg)
{
    M.print2();
}

void *Func_p(void *arg)
{
    struct threadPara *input = (struct threadPara *)arg;
    M.print(input->threadId);
}

int main()
{
    pthread_t p1, p2, p3;
    pthread_t p[2];
    struct threadPara threadInput[2];

    // pthread_create(&p1, NULL, Func_p1, NULL);
    // pthread_create(&p2, NULL, Func_p2, NULL);

    for (int i = 0; i < 2; i++)
    {
        threadInput[i].threadId = i;
        pthread_create(&p1, NULL, Func_p, (void *)&(threadInput[i]));
        pthread_create(&p2, NULL, Func_p, (void *)&(threadInput[i]));
    }

    pthread_cond_signal(&M.canPrint1);
    M.ready = true;

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);

    return 0;
}
