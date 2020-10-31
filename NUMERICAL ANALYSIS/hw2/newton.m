function Px = newton(inputMat)
    syms x;
    n = size(inputMat, 1);
    initLis = 1: n;
    [fx, aMat] = newtonGetFx(inputMat, [], initLis);
    PxMat = [1];
    for i = 1:n - 1
        xi = inputMat(i, 1);
        curPoly = PxMat(end) * (x - xi);
        PxMat = [PxMat, curPoly];
    end
    PxMat = aMat .* PxMat;
    Px = sum(PxMat);
end

function [fx_comb, aMat] = newtonGetFx(inputMat, aMat, lis)
    syms x;
    x0_id = lis(1);
    k = lis(end);
    x0 = inputMat(x0_id, 1);
    xk = inputMat(k, 1);

    if size(lis, 2) == 2
        fx_t1 = inputMat(k, 2);
        fx_t2 = inputMat(x0_id, 2);
        aMat(1) = fx_t2;
    else
        [fx_t1, aMat] = newtonGetFx(inputMat, aMat, lis(1, 2:end));
        [fx_t2, aMat]= newtonGetFx(inputMat, aMat, lis(1, 1:end - 1));
    end

    fx_comb = (fx_t1 - fx_t2) / (xk - x0);
    % [lis(1) - 1, lis(end) - 1, fx_comb]
    if length(lis) == lis(end)
        aMat(length(lis)) = fx_comb;
    end
end
