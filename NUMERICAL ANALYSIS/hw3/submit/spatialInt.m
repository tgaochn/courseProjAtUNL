function F = spatialInt(V, T)
    syms x y;
    F = {};
    triCnt = size(T, 1);
    for i = 1: triCnt
        v1 = V(T(i, 1), :);
        v2 = V(T(i, 2), :);
        v3 = V(T(i, 3), :);

        x1 = v1(1);
        y1 = v1(2);
        w1 = v1(3);
        x2 = v2(1);
        y2 = v2(2);
        w2 = v2(3);
        x3 = v3(1);
        y3 = v3(2);
        w3 = v3(3);

        A=[1,x1,y1;1,x2,y2;1,x3,y3];
        a=det(A) / 2;

        N1 = [x * (y2-y3) - y * (x2-x3) + (x2*y3-x3*y2)]/(2 * a);
        N2 = [x * (y3-y1) - y * (x3-x1) + (x3*y1-x1*y3)]/(2 * a);
        N3 = [x * (y1-y2) - y * (x1-x2) + (x1*y2-x2*y1)]/(2 * a);
        w = N1 * w1 + N2 * w2 + N3 * w3;
        F = {F{:}, {x1, y1, x2, y2, x3, y3, w}};
    end
end
