clear;
clc;
%
% a = [
% 10 9 6
%     0.001 6 12
%     5 3 30
%     ];
% b = [
% 20
% 30
% 60
% ];


a = [
5.999 11.999
-1.5 27
    ];
b = [
29.998
50
];




s1 = max(a(1, :))
s2 = max(a(2, :))
% s3 = max(a(3, :))

abs(a(1, 1)) / s1
abs(a(2, 1)) / s2
% abs(a(3, 1)) / s3

[x, paraMat, b] = GaussByOrder(a,b);
paraMat, b, x
