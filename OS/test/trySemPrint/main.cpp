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

sem_t Sem1, Sem2;

void *Func_p1(void *arg)
{
    for (int i = 0; i < N; i++)
    {
        sem_wait(&Sem1);
        printf("---thread id: %lu , p1 num: %d \n", pthread_self(), i);
        sem_post(&Sem2);
    }
}

void *Func_p2(void *arg)
{
    for (int i = 0; i < N; i++)
    {
        sem_wait(&Sem2);
        printf("---thread id: %lu , p2 num: %d \n", pthread_self(), i);
        sem_post(&Sem1);
    }
}

int main()
{
    pthread_t p1, p2;

    sem_init(&Sem1, 0, 1);
    sem_init(&Sem2, 0, 0);

    pthread_create(&p1, NULL, Func_p1, NULL);
    pthread_create(&p2, NULL, Func_p2, NULL);

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);

    return 0;
}
