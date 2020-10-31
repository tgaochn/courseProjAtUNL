clc;
clear;
close all;

syms h;
syms L;
syms fh;
% syms fh2;

fh = L - 4 * h^(1/2) - 8 * h - 2 * h^(3/2) + 3 * h^(4/2) + h^(5/2)

fh2 = subs(fh, h, h/2)
fh3 = sqrt(2) * fh2
