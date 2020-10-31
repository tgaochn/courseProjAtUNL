function [Img,Density]=points2Img(points,W)
% size(points)
% points=unique(points,'rows');

X_min=min(points(:,1));
X_max=max(points(:,1));

Y_min=min(points(:,2));
Y_max=max(points(:,2));

Sx=round((X_max-X_min)*W);
Sy=round((Y_max-Y_min)*W);

Img=zeros(Sx,Sy);

    for i=1:length(points(:,1))
        X=round((points(i,1)-X_min)*W);
        Y=round((points(i,2)-Y_min)*W);
        X=max(X,1);
        Y=max(Y,1);
        
        X=min(Sx,X);
        Y=min(Sy,Y);
       
        
       
        Img(X,Y)=Img(X,Y)+1;
             
    end
    
    if max(Img(:))>0
        Img=Img/max(Img(:));
    end
    
    Density=zeros(size(points(:,1)));
    for i=1:length(points(:,1))
        X=max(round((points(i,1)-X_min)*W),1);
        Y=max(round((points(i,2)-Y_min)*W),1);
        Density(i)=Img(X,Y);             
    end
    
end