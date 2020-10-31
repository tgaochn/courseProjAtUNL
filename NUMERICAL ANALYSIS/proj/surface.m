clc;
clear;
close all;

% Nearest Neighbor
x1 = linspace(-5, 5, 20);
x2 = linspace(-5, 5, 20);
[X, Y]=meshgrid(x1, x2);
Z = sign(1 - abs(X) ) + sign(1 - abs(Y));
Z1 = Z;
Z1(Z1 ~= 2) = 0;
Z1(Z1 == 2) = 1;
surf(X, Y, Z1)

% Bilinear
deltaX = 2;
deltaY = 2;
x1 = linspace(-5, 5, 20);
x2 = linspace(-5, 5, 20);
[X, Y]=meshgrid(x1, x2);
signX = sign(deltaX - abs(X));
signY = sign(deltaY - abs(Y));
signX(signX < 0.5) = 0;
signY(signY < 0.5) = 0;
Z = (1 - abs(X)/deltaX ) .* (1 - abs(Y)/deltaY) .* signX .* signY;
surf(X, Y, Z)

% Sinc - 2D
deltaX = 2;
x = linspace(-5, 5, 20);
y = (1/deltaX)*sinc(x/deltaX);
plot(x, y)

% Sinc - 3D
x1 = linspace(-5, 5, 20);
x2 = linspace(-5, 5, 20);
[X, Y]=meshgrid(x1, x2);
Z = (1/4) * sinc(X/2) .* sinc(Y/2);
surf(X, Y, Z)
