/* Include Files */
#include <pthread.h>
#include <stdio.h>

/* External References */
extern int world(void);
extern int hello(void);
extern int exclamation(void);
void *threadCall1(void *arg);
void *threadCall2(void *arg);
void *threadCall3(void *arg);

int main(int argc, char *argv[])
{
    pthread_t thread[3];

    pthread_create(&thread[0], NULL, threadCall1, NULL);
    pthread_join(thread[0], NULL);

    pthread_create(&thread[1], NULL, threadCall2, NULL);
    pthread_join(thread[1], NULL);

    pthread_create(&thread[2], NULL, threadCall3, NULL);
    pthread_join(thread[2], NULL);

    printf("\n");
    pthread_exit(NULL);
    return (0);
}

void *threadCall1(void *arg)
{
    hello();
}

void *threadCall2(void *arg)
{
    world();
}

void *threadCall3(void *arg)
{
    exclamation();
}

/* world - print the "world" part. */
int world(void)
{
    printf("world");
    return 0;
}

/* hello - print the "hello" part. */
int hello(void)
{
    printf("hello ");
    return 0;
}

/* exclamation - print "!".*/
int exclamation()
{
    printf("!");
    return 0;
}