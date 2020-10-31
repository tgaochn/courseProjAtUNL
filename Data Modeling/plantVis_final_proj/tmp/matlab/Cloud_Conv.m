filename='3.ply';

[Vertex,Color,Face]=plyRead(filename,1,1);
X=Vertex(:, 1);
Y=Vertex(:, 2);
Z=Vertex(:, 3);
Points_V=[X,Y,Z];

coeff=pca(Points_V(Color(:,2)>20&Color(:,2)<140,:));
disp(coeff);

v_pca=coeff(:,1);

% 
% [V,~]=Voxelize(filename);
% 
% Size=size(V);
% 
% Centers=Normal_dist(V);
% 
% Vec_z=Centers(1,:);
% Vec_z=Vec_z/norm(Vec_z);
% disp(Vec_z);

disp(v_pca');
Points_V_rot=Rotation(Points_V,v_pca');

X=Points_V_rot(:,1);
Y=Points_V_rot(:,2);
Z=Points_V_rot(:,3);


Vertex(:,1)=X;
Vertex(:,2)=Y;
Vertex(:,3)=Z;

write_ply(Vertex,Color,Face,['moved_',filename])

