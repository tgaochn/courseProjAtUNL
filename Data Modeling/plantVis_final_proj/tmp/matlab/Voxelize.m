function [V,PtCloud_V]=Voxelize(filename,W,Ratio)

if nargin==1
    Size=100;
    Ratio=1;
elseif nargin==2
    Size=W;
    Ratio=1;
elseif nargin==3
    Size=W;
    if Ratio<=0
        Ratio=1;
    end
end


PtCloud=pcread(filename);

Points=PtCloud.Location;
Colors=PtCloud.Color;

if isempty(Colors)
    Colors=zeros(size(Points));
    Colors(:,1)=255;
end


% Norms=PtCloud.Normal;
Ratio=max(Ratio,0.1);
Points=Points/Ratio;
size(Points)

X_min=min(Points(:,1));
Y_min=min(Points(:,2));
Z_min=min(Points(:,3));

X_max=max(Points(:,1));
Y_max=max(Points(:,2));
Z_max=max(Points(:,3));



X_range=X_max-X_min;
Y_range=Y_max-Y_min;
Z_range=Z_max-Z_min;



% [X_range,Y_range,Z_range]
[~,Index]=sort([X_range,Y_range,Z_range]);
Range_min=min([X_range,Y_range,Z_range]);
Points=[Points(:,Index(1)),Points(:,Index(2)),Points(:,Index(3))];
%%%%%%%%%Range Scaling%%%%%%%%%
Points=Points/Range_min;
%%%%%%%%%Range Scaling%%%%%%%%%

X_min=min(Points(:,1));
Y_min=min(Points(:,2));
Z_min=min(Points(:,3));

X_max=max(Points(:,1));
Y_max=max(Points(:,2));
Z_max=max(Points(:,3));



X_range=X_max-X_min;
Y_range=Y_max-Y_min;
Z_range=Z_max-Z_min;



Sx=round(X_range*Size);
Sy=round(Y_range*Size);
Sz=round(Z_range*Size);

[Sx,Sy,Sz]

V=zeros(Sx,Sy,Sz);
C1=zeros(Sx,Sy,Sz);
C2=zeros(Sx,Sy,Sz);
C3=zeros(Sx,Sy,Sz);


for i=1:length(Points(:,1))
    
    Point=Points(i,:);
    
    X=round((Point(1)-X_min)*Size);
    Y=round((Point(2)-Y_min)*Size);
    Z=round((Point(3)-Z_min)*Size);
    
%     X=round((Point(1)-X_min)/X_range*Size);
%     Y=round((Point(2)-Y_min)/Y_range*Size);
%     Z=round((Point(3)-Z_min)/Z_range*Size);

    X=max(X,1);
    Y=max(Y,1);
    Z=max(Z,1);
    
    X=min(X,Sx);
    Y=min(Y,Sy);
    Z=min(Z,Sz);

    V(X,Y,Z)=V(X,Y,Z)+1;
%      C1(X,Y,Z)=C1(X,Y,Z)+Colors(i,1);
%      C2(X,Y,Z)=C2(X,Y,Z)+Colors(i,2);
%      C3(X,Y,Z)=C3(X,Y,Z)+Colors(i,3);

     C1(X,Y,Z)=Colors(i,1);
     C2(X,Y,Z)=Colors(i,2);
     C3(X,Y,Z)=Colors(i,3);

    
end

% C1=C1./(V+eps);
% C2=C2./(V+eps);
% C3=C3./(V+eps);


V=V./max(V(:));

V(V<0.1)=0;

Points_V=zeros(sum(V(:)>0),3);
Colors_V=zeros(size(Points_V));

Count=0;
for i=1:Sx
    for j=1:Sy
        for k=1:Sz        
            if V(i,j,k)>0
                Count=Count+1;
                Points_V(Count,:)=[i,j,k];
                Colors_V(Count,:)=[C1(i,j,k),C2(i,j,k),C3(i,j,k)];
            end
        end
    end
end


PtCloud_V=pointCloud(Points_V,'Color',uint8(Colors_V));
% figure,pcshow(PtCloud_V);



