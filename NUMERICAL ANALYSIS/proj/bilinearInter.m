clc;
clear;
close all;

fn = 'baby.jpg'
I = imread(fn);
zmf = 2;
ZI = imblizoom(fn, zmf);

subplot(121)
imshow(I)
axis on
subplot(122)
imshow(ZI)
axis on
