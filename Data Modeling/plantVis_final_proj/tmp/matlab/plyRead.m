function [vertices,colors,faces] = plyRead(filename,face_index_start,has_color)
%% Parse the Header
fid = fopen(filename,'r');
readFile = true;
ii = 0;
while readFile == true
    fLine = fgetl(fid);
    ii = ii + 1;
    if regexpi(fLine,'element vertex')
        fLine = strsplit(fLine,' ');
        nVertex = str2double(fLine{end});
        continue
    end
    
    if regexpi(fLine,'element face')
        fLine = strsplit(fLine,' ');
        nFace = str2double(fLine{end});
        continue
    end
    
    if regexpi(fLine,'end_header')
        readFile = false;
        endHeader = ii;
        continue
    end    
end
fclose(fid);
%% Textscan the vertex info
delimiter = ' ';
startRow = endHeader+1;
endRow = startRow + nVertex - 1;

formatSpec = '%f%f%f%*u%*u%*u%*s%[^\n\r]';


fid = fopen(filename,'r');
dataArray = textscan(fid, formatSpec, nVertex, 'Delimiter', delimiter, 'MultipleDelimsAsOne', true, 'EmptyValue' ,NaN,'HeaderLines', startRow-1, 'ReturnOnError', false);
fclose(fid);
vertices = [dataArray{1:end-1}];


if (has_color>0)
    formatSpec = '%*f%*f%*f%u%u%u%*s%[^\n\r]';

    fid = fopen(filename,'r');
    dataArray = textscan(fid, formatSpec, nVertex, 'Delimiter', delimiter, 'MultipleDelimsAsOne', true, 'EmptyValue' ,NaN,'HeaderLines', startRow-1, 'ReturnOnError', false);
    fclose(fid);
    colors = [dataArray{1:end-1}];
else
    colors=[];
end

%% Textscan the face connectivity
delimiter = ' ';
startRow = endRow + 1;
formatSpec = '%*q%f%f%f%u%*s%[^\n\r]';
fid = fopen(filename,'r');
dataArray = textscan(fid, formatSpec, 'Delimiter', delimiter, 'MultipleDelimsAsOne', true, 'EmptyValue' ,NaN,'HeaderLines' ,startRow-1, 'ReturnOnError', false);
fclose(fid);
faces = [dataArray{1:end-1}];
faces = faces + face_index_start;