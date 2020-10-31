clear;
clc;
close all;

intergFunc = intergration;

syms x;
syms f;

% f = sin(x) / x;
% f = sin(x) / x;
% f = 1 / (x + 1);
% f = 1 / (2 * x + 1);
% f = x ^ 2;
% f = (x^4 + 5) ^ (-1);
% f = x^(-4);
f = x^(-4);
% partition = [0.00001, 0.2, 0.4, 0.6, 0.8, 1];
% partition = [0, 1/2, 1];
% partition = [1, 3/2, 2];
% partition = [0, 1/4, 1/2, 3/4, 1];
partition = [1, 3/2, 2, 5/2, 3];

inputMat = [
        1 12
        1.5 10
        2 8
        2.5 5
        3 4
];

% inputMat = [
%         0 1
%         0.2 0.99335
%         0.4 0.97355
%         0.6 0.94107
%         0.8 0.89670
%         1 0.84147
% ];

% [upper, lower] = intergFunc.LowerUpperSum(f, partition)
% rlt = intergFunc.trapezoid(f, partition, 1)
% rlt = intergFunc.trapezoid(inputMat(:, 2)', inputMat(:, 1)', 2)
rlt = intergFunc.simpson(f, partition)
