clc;
clear;
spline = spline;

syms x;

% statMat = [
%             1 30;
%             5 33;
%             8 35;
%             12 27;
%             15 29;
%             19 32;
%             22 35;
%             26 37;
%             29 39;
%                     ];

% statMat = [
%             6 75
%             13 78
%             20 72
%             27 68
% ]

% statMat = [
%     1 68
%     5 71
%     8 76
%     12 73
%     15 71
%     19 68
%     22 70
%     26 74
%     29 731
% ]

% statMat = [
%     1 68
%     5 71
%     8 76
%     12 73
%     15 71
%     19 68
%     22 70
%     26 74
%     29 73
% ]

% statMat = [
%     1 42
%     7 54
%     13 60
%     19 72
%     25 90
% ]
% statMat = [
%     5 28
%     10 30
%     15 33
%     20 31
% ]
% %
% statMat = [
%     6 75
%     13 78
%     20 72
%     27 68
% ]
statMat = [
    8 30
    15 37
    22 42
    29 44
]
%

% S = spline.linear(statMat);
% S = spline.quadratic(statMat);
% S = spline.cubic(statMat);
S = spline.cubic_r(statMat);
for i = 1:size(S, 2)
    display(['calculating Q_', int2str(i - 1)])
    display(S{i});
end
