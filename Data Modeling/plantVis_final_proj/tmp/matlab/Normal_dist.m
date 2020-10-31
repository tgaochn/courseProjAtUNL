
function Centers=Normal_dist(V)

coeff_all=[];
interval=5;
[Sx,Sy,Sz]=size(V);

for i=6:interval:Sx-5
    for j=6:interval:Sy-5
        for k=6:interval:Sz-5
                block=V(i-5:i+5,j-5:j+5,k-5:k+5);
                points=[];
                
                [Bx,By,Bz]=size(block);
                
                for ii=1:Bx
                    for jj=1:By
                        for kk=1:Bz
                            if block(ii,jj,kk)>0
                                
                                points=[points;ii,jj,kk];
                            end
                        end
                    end
                end
                
                if length(points)>3
                   coeff=pca(points) ;
                   coeff_all=[coeff_all,coeff(:,3)];
                end
                
                
        end
    end
end

coeff_all=transpose(coeff_all);


coeff_all=unique(coeff_all,'rows');


[idx,Center]=kmeans(coeff_all, 1);

%  [ClusterCenter,idx,~] = MeanShiftCluster(coeff_all',0.6,0);

 
 
Centers=zeros(1,3);


for i=min(idx):max(idx)
    coeff_i=coeff_all(idx==i,:);
    
  
   
    CoC_i=pca(coeff_i);
    
    coeff_i_proj=coeff_i*CoC_i;
    
    
     
    W=50;
     [Img,Density]=points2Img(coeff_i_proj,W);
    
     
    coeff_i_dense=coeff_i(Density>0.2,:);
    
%     figure,scatter3(coeff_i_dense(:,1),coeff_i_dense(:,2),coeff_i_dense(:,3));
%     figure,imshow(Img>0.2);
    
    Center_i=[mean(coeff_i_dense(:,1)),mean(coeff_i_dense(:,2)), mean(coeff_i_dense(:,3))];
    
    Centers(i,:)=Center_i;
    
end



figure,scatter3(coeff_all(:,1),coeff_all(:,2),coeff_all(:,3),20,idx/max(idx));
% hold on;
% plot3(Centers(:,1),Centers(:,2),Centers(:,3),'*','LineWidth',3);
% hold off;


% [~,idx_x]=max(Centers(:,1));
% [~,idx_y]=max(Centers(:,2));
% [~,idx_z]=max(Centers(:,3));

% Vec_x=Centers(idx_x,:);
% Vec_y=Centers(idx_y,:);
% Vec_z=Centers(idx_z,:);


end


