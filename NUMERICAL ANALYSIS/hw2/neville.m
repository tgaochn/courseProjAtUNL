function Px = neville(inputMat)
    lis = 1:size(inputMat, 1);
    Px = nevillePoly(inputMat, lis);
    Px = collect(Px);
end


function Px = nevillePoly(inputMat, lis)
% function: Short description
%
% Extended description
    syms x;
    i = lis(1);
    j = lis(end);
    xi = inputMat(i, 1);
    xj = inputMat(j, 1);
    if size(lis, 2) == 2
        Px_t1 = inputMat(j, 2);
        Px_t2 = inputMat(i, 2);
    else
        Px_t1 = nevillePoly(inputMat, lis(1, 2:end));
        Px_t2 = nevillePoly(inputMat, lis(1, 1:end - 1));
    end
    Px = Px_t1 * (x - xi) / (xj - xi) + Px_t2 * (xj - x) / (xj - xi);
    % [i-1, j-1, Px]
    % Px = collect(Px);
end
