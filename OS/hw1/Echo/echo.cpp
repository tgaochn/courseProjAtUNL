// echo.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   : 
// @Date   : Fri, 07/17/2020, 00:05

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    for (int i = 1; i < argc; i++)
    {
        cout << argv[i] << " ";
    }
    cout << endl;
    return 0;
}
