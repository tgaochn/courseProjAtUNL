clc;
clear;
findingZero = findingZero;

syms x
% f = 3 * x^3 - 2 * x^2 + 5 * x - 2 * exp(x) + 1;
f = x^3 - 5 * x;
p0 = 1;
TOL = 0.0001;
maxIter = 50;
% p_biSec = findingZero.bisection(f, -1, 1, TOL)
p_nt = findingZero.newton(f, p0, TOL, maxIter)
% p_sec = findingZero.secant(f, 1, 0.99, TOL, maxIter)

% display('Using Bisection method, the root of f(x) is');
% display(p_biSec);
display('Using Newton method, the root of f(x) is');
display(p_nt);
% display('Using Secant method, the root of f(x) is');
% display(p_sec);
