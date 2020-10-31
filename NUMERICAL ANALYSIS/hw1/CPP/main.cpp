#include <cmath>
#include <iostream>

using namespace std;

double func(float x){
    double f;
    f = 3 * pow(x, 3) - 2 * pow(x, 2) + 5 * x - 2 * exp(1) + 1;
    return f;
}

float biSec(float a, float b, float e){
    double fa, fb, fc;
    float c;

    fa = func(a);
    fb = func(b);

    if(fa == 0){
        return a;
    }

    if(fb == 0){
        return b;
    }

    if(fa * fb > 0){
        cout << "There is no result" << endl;
        return 0;
    } else{
        c = (a + b) / 2;
        fc = func(c);
        if(abs(fc) < e){
            return c;
        }else{
            if(fa * fc > 0){
                a = c;
            }else{
                b = c;
            }
            return biSec(a, b, e);
        }
    }
}

int main() {
    float a, b, e;
    float c;

    a = -1;
    b = 1;
    e = 0.0001;
    c = biSec(a, b ,e);

    cout << c << endl;
    cout << func(0.823486) << endl;
    return 0;
}