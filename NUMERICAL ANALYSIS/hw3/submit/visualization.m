clear; clc;
x = [0;0;0;3;5;5;10;12;16;20;20];
y = [20;10;0;6;0;13;6;20;12;0;20];
v=[11550;10500;9915;9870;12915;13650;12600;11592;12240;13680;11640];
F = scatteredInterpolant(x,y,v, 'linear');

x=[0; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20];
y=[0; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20];
[X,Y] =  ndgrid(x,y);
Vq = F(X,Y);
mesh(X,Y,Vq);