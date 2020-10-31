#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define MSGSIZE 16

int main()
{
    int p1[2], p2[2], child1, child2;
    int randNum = 0;
    int timeInfo = 0;

    pipe(p1);
    pipe(p2);
    child1 = fork();

    if (child1 > 0)
    {
        // parent
        read(p1[0], &randNum, sizeof(randNum));
        close(p1[0]);

        randNum += 1000;
        printf("%d\n", randNum);

        read(p2[0], &timeInfo, sizeof(timeInfo));
        close(p2[0]);

        timeInfo = timeInfo + 100;
        printf("%d\n", timeInfo);
    }
    else
    {
        child2 = fork();
        if (child2 > 0)
        {
            // child1
            randNum = rand();
            write(p1[1], &randNum, sizeof(randNum));
            close(p1[1]);
        }
        else
        {
            // child2
            write(p2[1], &timeInfo, sizeof(timeInfo));
            close(p2[1]);
        }
    }
    close(p1[0]);
    close(p1[1]);
    close(p2[0]);
    close(p2[1]);

    exit(0);
}
