V=[0,20,11550;
    12,20,11592;
    20,20,11640;
    5,13,13650;
    16,12,12240;
    0,10,10500;
    3,6,9870;
    10,6,12600;
    0,0,9915;
    5,0,12915;
    20,0,13680];

T=[1,4,6;
    1,2,4;
    2,3,5;
    4,6,8;
    2,4,8;
    2,5,8;
    3,5,11;
    6,7,8;
    5,8,11;
    6,7,9;
    7,9,10;
    7,8,10;
    8,10,11];

F = spatialInt(V, T);
for i = 1: size(F, 2)
    display('The 3 vertices are:')
    x1 = F{i}{1};
    y1 = F{i}{2};
    x2 = F{i}{3};
    y2 = F{i}{4};
    x3 = F{i}{5};
    y3 = F{i}{6};
    w = F{i}{7};
    display(['(', num2str(x1), ',', num2str(y1), '), (', num2str(x2), ',', num2str(y2), '), (', num2str(x2), ',', num2str(y2), ')'])
    display('The linear interpolation function of the triangular surface is:')
    display(w)
    display('=============')
end
