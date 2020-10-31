// main.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Sun, 08/02/2020, 00:56

#include <iostream>
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define N 5
using namespace std;

class monitor
{
private:
public:
    pthread_cond_t canPrint1;
    pthread_cond_t canPrint2;
    pthread_mutex_t condlock;
    bool ready = false;
    bool sent1 = true;
    bool sent2 = false;

    monitor()
    {
        pthread_mutex_init(&condlock, NULL);
        pthread_cond_init(&canPrint1, NULL);
        pthread_cond_init(&canPrint2, NULL);
    }

    void print1(int i)
    {
        pthread_mutex_lock(&condlock);
        while (!ready)
            pthread_cond_wait(&canPrint1, &condlock);

        cout << "thread: " << pthread_self() << "\tprint1 : " << i << endl;

        pthread_cond_signal(&canPrint2);
        pthread_mutex_unlock(&condlock);
        // sleep(1);
    }

    void print2(int i)
    {
        pthread_mutex_lock(&condlock);
        while (!ready)
            pthread_cond_wait(&canPrint2, &condlock);

        cout << "thread: " << pthread_self() << "\tprint2 : " << i << endl;

        pthread_cond_signal(&canPrint1);
        pthread_mutex_unlock(&condlock);
        // sleep(1);
    }

} M;

void *Func_p1(void *arg)
{
    for (int i = 0; i < N; i++)
    {
        M.print1(i);
    }
}

void *Func_p2(void *arg)
{
    for (int i = 0; i < N; i++)
    {
        M.print2(i);
    }
}

int main()
{
    pthread_t p1, p2, p3;

    pthread_create(&p1, NULL, Func_p1, NULL);
    pthread_create(&p2, NULL, Func_p2, NULL);

    pthread_cond_signal(&M.canPrint1);
    // pthread_cond_broadcast(&M.canPrint1);
    M.ready = true;

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);

    return 0;
}
