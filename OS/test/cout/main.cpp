// main.cpp
// @Author : Tian Gao (tgaochn@gmail.com)
// @Link   : 
// @Date   : Tue, 08/04/2020, 21:55

#include "utils.h"
#include <iostream>
#include "math.h"
using namespace std;

#define N 4
#define totalPhase int(floor((2 * log(N) / log(2)) + 0.5) + 1)

int main(int argc, char **argv)
{
    // int i = 5;
    // cout << i / 4 << endl;
    cout << totalPhase << endl;
    return 0;
}
