// main.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Sun, 08/02/2020, 00:56

#include <iostream>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define N 5
using namespace std;

pthread_mutex_t mutex;
pthread_cond_t cond1, cond2, cond3, cond4;
bool ready = false;

void *Func_p1(void *arg)
{
    for (int i = 0; i < N; i++)
    {
        pthread_mutex_lock(&mutex);
        while (!ready)
            pthread_cond_wait(&cond1, &mutex);
        printf("---thread id: %lu , p1 num: %d \n", pthread_self(), i);
        pthread_cond_signal(&cond2);
        pthread_cond_broadcast(&cond2);
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

void *Func_p2(void *arg)
{
    for (int i = 0; i < N; i++)
    {
        pthread_mutex_lock(&mutex);
        while (!ready)
            pthread_cond_wait(&cond2, &mutex);
        printf("---thread id: %lu , p2 num: %d \n", pthread_self(), i);
        pthread_cond_signal(&cond3);
        pthread_cond_broadcast(&cond3);
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

void *Func_p3(void *arg)
{
    for (int i = 0; i < N; i++)
    {
        pthread_mutex_lock(&mutex);
        while (!ready)
            pthread_cond_wait(&cond3, &mutex);
        printf("---thread id: %lu , p3 num: %d \n", pthread_self(), i);
        pthread_cond_signal(&cond1);
        pthread_cond_broadcast(&cond1);
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main()
{
    pthread_t p1, p2, p3, p4;

    pthread_mutex_init(&mutex, NULL);
    pthread_cond_init(&cond1, NULL);
    pthread_cond_init(&cond2, NULL);
    pthread_cond_init(&cond3, NULL);

    pthread_create(&p1, NULL, Func_p1, NULL);
    pthread_create(&p2, NULL, Func_p2, NULL);
    pthread_create(&p3, NULL, Func_p3, NULL);

    pthread_cond_signal(&cond1);
    ready = true;

    pthread_join(p1, NULL);
    pthread_join(p2, NULL);
    pthread_join(p3, NULL);

    pthread_mutex_destroy(&mutex);
    pthread_cond_destroy(&cond1);
    pthread_cond_destroy(&cond2);
    pthread_cond_destroy(&cond3);

    return 0;
}
