function R=RodRot(a,b)
% Reference
aNorm = a / norm(a);
bNorm = b / norm(b);
c = cross(aNorm, bNorm);
axis = c/norm(c);
cos_A=dot(aNorm, bNorm);
sin_A=sqrt(1-cos_A^2);

R = [axis(1)^2+(1-axis(1)^2)*cos_A  axis(1)*axis(2)*(1-cos_A)-axis(3)*sin_A     axis(1)*axis(3)*(1-cos_A)+axis(2)*sin_A;
    
    axis(1)*axis(2)*(1-cos_A)+axis(3)*sin_A   axis(2)^2+(1-axis(2)^2)*cos_A   axis(2)*axis(3)*(1-cos_A)-axis(1)*sin_A;
    
    axis(1)*axis(3)*(1-cos_A)-axis(2)*sin_A   axis(2)*axis(3)*(1-cos_A)+axis(1)*sin_A   axis(3)^2+(1-axis(3)^2)*cos_A];