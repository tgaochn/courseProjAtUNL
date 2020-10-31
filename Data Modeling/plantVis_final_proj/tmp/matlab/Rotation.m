function Points_V_rot=Rotation(Points_V,Vec_z)

% Theta=asin(Vec_z(2)/norm(Vec_z(1:2)));
% Alpha=acos(Vec_z(3)/norm(Vec_z));
% 
% Mat_xy=[cos(Theta),-sin(Theta),0;sin(Theta),cos(Theta),0;0,0,1];
% Mat_xz=[cos(Alpha),0,sin(Alpha);0,1,0;-sin(Alpha),0,cos(Alpha)];
% 
% Vec_z_rot=Vec_z*Mat_xy;
% Vec_z_rot=Vec_z_rot*Mat_xz;

R=RodRot(Vec_z,[0,0,1]);

R=transpose(R);

Vec_z_rot=Vec_z*R;
disp(Vec_z_rot);

fprintf("Rotation begins\n");

Points_V_G=gpuArray(Points_V);

R_G=gpuArray(R);

Points_V_rot_G=Points_V_G*R_G;




%%%Centering%%%

X_min=min(Points_V_rot_G(:,1));
X_max=max(Points_V_rot_G(:,1));
Y_min=min(Points_V_rot_G(:,2));
Y_max=max(Points_V_rot_G(:,2));
Z_min=min(Points_V_rot_G(:,3));
Z_max=max(Points_V_rot_G(:,3));

Points_V_rot_G(:,1)=Points_V_rot_G(:,1)-(X_min+X_max)/2; 
Points_V_rot_G(:,2)=Points_V_rot_G(:,2)-(Y_min+Y_max)/2;
Points_V_rot_G(:,3)=Points_V_rot_G(:,3)-Z_min;

Points_V_rot=gather(Points_V_rot_G);
fprintf("Rotation ends\n");

