function Px = lagrange(inputMat)
% function: Short description
%
% Extended description
    syms x;
    n = size(inputMat, 1);
    Lx = [];
    for i = 1:n
        xi = inputMat(i, 1);
        LxTerm = 1;
        for j = 1:n
            if j == i
                continue
            end
            xj = inputMat(j, 1);
            LxTerm = LxTerm * (x - xj) / (xi - xj);
        end
        Lx = [Lx, LxTerm];
    end
    % Lx
    PxTermMat = Lx .* inputMat(:, 2)';
    Px = sum(PxTermMat);
end
