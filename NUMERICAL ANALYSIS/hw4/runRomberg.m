clear all,
close all,
clc,
format long,
syms x,

fx = 3^x;
a = 0;
b = 8;
m = 4;

% Calculate the first column of R(:,0)using the Recursive Trapezoid Rule
h = b - a;
R = zeros(m); % Note that Matlab index starts with 1 instead of 0
R(1,1) = 0.5 * h * (subs(fx, x, a) + subs(fx, x, b));
i = 1;
fprintf(1, 'R(%d, 0) = %1.10f\n', i-1, R(i,1));
for i = 2:1:size(R,1)
    h = h/2;
    R(i,1) = 0.5 * R(i-1,1);
    for j = 0:1: (2^(i-2)-1)
        R(i,1) = R(i,1) + h * (subs(fx, x, ((2 * j + 1) * h)));
    end
    fprintf(1, 'R(%d, 0) = %1.10f\n', i-1, R(i,1));
end

for j = 2:1:size(R,1)
    for i = j:1:size(R,1)
        R(i,j) = R(i, j-1) + (R(i, j-1) - R(i-1, j-1))/(4^(j-1) - 1);
        % 4^(j-1) is different from the equation due to the matlab index issue
        fprintf(1, 'R(%d, %d) = %1.12f\n', i-1, j-1, R(i,j));
        end
end
