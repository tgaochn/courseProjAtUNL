// cat.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   :
// @Date   : Fri, 07/17/2020, 19:36

#include <fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;

int main(int argc, char **argv)
{
    fstream f;
    char buffer[256];

    for (int i = 1; i < argc; i++)
    {
        f.open(argv[i]);
        if (!f.is_open())
        {
            cout << "Cannot open file: " << argv[i] << endl;
            exit(1);
        }

        while (!f.eof())
        {
            f.getline(buffer, 100);
            cout << buffer << endl;
        }

        f.close();
    }

    return 0;
}
