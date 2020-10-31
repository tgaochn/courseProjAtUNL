#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#define MSGSIZE 16

int main()
{
    char *msg1 = "How are you?";
    char inbuff[MSGSIZE];
    int p1[2], p2[2], child1, child2;

    pipe(p1);
    pipe(p2);
    child1 = fork();

    if (child1 > 0)
    {
        // parent

        // !! new added
        // int status = 0;
        // wait(&status); //wait the end of child process
    }
    else
    {
        child2 = fork();
        if (child2 > 0)
        {
            // child1
            write(p1[1], msg1, MSGSIZE);
            close(p1[1]);

            read(p2[0], inbuff, MSGSIZE);
            close(p2[0]);
            printf("%s\n", inbuff);
        }
        else
        {
            // child2
            read(p1[0], inbuff, MSGSIZE);
            close(p1[0]);

            myStrupr(inbuff);
            write(p2[1], inbuff, MSGSIZE);
            close(p2[1]);
        }
    }
    close(p1[0]);
    close(p1[1]);
    close(p2[0]);
    close(p2[1]);

    exit(0);
}

void myStrupr(char *s)
{
    char *p = s;
    while (*p != (char *)NULL)
    {
        *p = _toupper(*p);
        ++p;
    }
}