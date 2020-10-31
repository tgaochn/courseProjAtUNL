function ZI = imblizoom(I, zmf )

%----------------------˫���Բ�ֵ�����ž�����ͼ��---------------------------

% Input��

%       I��ͼ���ļ���������������ֵ��0~255����

%       zmf���������ӣ������ŵı���

% Output��

%       ���ź���ͼ������ ZI

% Usage:

%       ZI = SSELMHSIC('ImageFileName',zmf)

%       ��ͼ��I����zmf�������Ų���ʾ

%    Or:

%       ZI = SSELMHSIC(I,zmf)

%       �Ծ���I����zmf�������Ų���ʾ

%    ...

%-------------------------------------------------------------------

    %%%%    Authors:   Zhi Liu

    %%%%    XiDian University Student

    %%%%    EMAIL:     zhiliu.mind@gmail.com

    %%%%    DATE:      16-12-2013

%% Step1 �����ݽ���Ԥ����

if ~exist('I','var') || isempty(I)

    error('����ͼ�� Iδ������Ϊ�գ�');

end

if ~exist('zmf','var') || isempty(zmf) || numel(zmf) ~= 1

     error('λ��ʸ�� zmfδ������Ϊ�ջ� zmf�е�Ԫ�س���2��');

end

if isstr(I)

    [I,M] = imread(I);

end

if zmf <= 0

     error('���ű��� zmf��ֵӦ�ô���0��');

end

%% Step2 ͨ��ԭʼͼ�����������ӵõ���ͼ���Ĵ�С����������ͼ����

[IH,IW,ID] = size(I);

ZIH = round(IH*zmf); % �������ź���ͼ���߶ȣ�����ȡ��

ZIW = round(IW*zmf); % �������ź���ͼ�����ȣ�����ȡ��

ZI = zeros(ZIH,ZIW,ID); % ������ͼ��

%% Step3 ��չ����I��Ե

IT = zeros(IH+2,IW+2,ID);

IT(2:IH+1,2:IW+1,:) = I;

IT(1,2:IW+1,:)=I(1,:,:);IT(IH+2,2:IW+1,:)=I(IH,:,:);

IT(2:IH+1,1,:)=I(:,1,:);IT(2:IH+1,IW+2,:)=I(:,IW,:);

IT(1,1,:) = I(1,1,:);IT(1,IW+2,:) = I(1,IW,:);

IT(IH+2,1,:) = I(IH,1,:);IT(IH+2,IW+2,:) = I(IH,IW,:);

%% Step4 ����ͼ����ĳ�����أ�zi��zj��ӳ�䵽ԭʼͼ��(ii��jj)��������ֵ��

for zj = 1:ZIW         % ��ͼ�����а�����Ԫ��ɨ��

    for zi = 1:ZIH

        ii = (zi-1)/zmf; jj = (zj-1)/zmf;

        i = floor(ii); j = floor(jj); % ����ȡ��

        u = ii - i; v = jj - j;

        i = i + 1; j = j + 1;

        ZI(zi,zj,:) = (1-u)*(1-v)*IT(i,j,:) +(1-u)*v*IT(i,j+1,:) + u*(1-v)*IT(i+1,j,:) +u*v*IT(i+1,j+1,:);

    end

end

ZI = uint8(ZI);

%% ��ͼ������ʽ��ʾͬ�־���P

% figure
%
% imshow(I,M);
%
% axis on
%
% title(['ԭͼ�񣨴�С�� ',num2str(IH),'*',num2str(IW),'*',num2str(ID),')']);
%
% figure
%
% imshow(ZI,M);
%
% axis on
%
% title(['���ź���ͼ�񣨴�С�� ',num2str(ZIH),'*',num2str(ZIW),'*',num2str(ID)',')']);

end
