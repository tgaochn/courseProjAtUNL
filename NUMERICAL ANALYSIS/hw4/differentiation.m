function diffRlt = differentiation(dataMat)
    diffRlt = [];
    n = size(dataMat, 1);
    h = dataMat(2, 1) - dataMat(1, 1);

    initTerm = (1 / (h * 2)) * ((-3) * dataMat(1, 2) + 4 * dataMat(2, 2) - dataMat(3, 2));
    diffRlt = [diffRlt, initTerm];

    for i = 1: n - 2
        midTerm = (1 / (h * 2)) * (dataMat(i + 2, 2) - dataMat(i, 2));
        diffRlt = [diffRlt, midTerm];
    end

    endTerm = (1 / (h * 2)) * (dataMat(end - 2, 2) - 4 * dataMat(end - 1, 2) + 3 * dataMat(end, 2));
    diffRlt = [diffRlt, endTerm];
end
