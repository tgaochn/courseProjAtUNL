clear;
clc;
close all;

% inputData = [
        % 2 3
        % 4 7
        % 6 5
% ];
% inputData = [
%         1.1 9.025013
%         1.2 11.023180
%         1.3 13.463740
%         1.4 16.444650
% ];
inputData = [
        2.2 1.58725
        2.4 1.63068
        2.6 1.74256
        2.8 1.91432
];
% inputData = [
%         1.1 1.52918
%         1.2 1.64024
%         1.3 1.70470
%         1.4 1.71277
% ];

diffRlt = differentiation(inputData)
