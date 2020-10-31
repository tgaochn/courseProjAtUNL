function func = intergration
 func.LowerUpperSum=@LowerUpperSum;
 func.trapezoid=@trapezoid;
 func.simpson=@simpson;
end

% has bugs
function [upper, lower] = LowerUpperSum(f, partition)
    syms x;
    n = size(partition, 2);
    h = partition(2) - partition(1);
    f_xi = subs(f, x, partition)
    term1 = sum(f_xi(2: end))
    term2 = sum(f_xi(1: end - 1))
    upper = max(term1, term2) * h
    lower = min(term1, term2) * h
end

function rlt = trapezoid(f, partition, mode)
    syms x;
    n = size(partition, 2);

    % mode 1: given function
    % mode 2: given function value
    if mode == 1
        f_xi_Mat = subs(f, x, partition);
    elseif mode ==2
        f_xi_Mat = f
    end

    Ai = [];
    for i = 1: n - 1
        xi = partition(i);
        xi1 = partition(i + 1);
        f_xi = f_xi_Mat(i);
        f_xi1 = f_xi_Mat(i + 1);
        Ai = [Ai, (xi1 - xi) * (f_xi1 + f_xi) / 2];
    end
    rlt = sum(Ai);
end

function rlt = simpson(f, partition)
    syms x;
    h = partition(2) - partition(1);
    n = (partition(end) - partition(1)) / h;
    a = partition(1);
    b = partition(end);
    term_x_2k1 = a + h: 2 * h: a + (n - 1) * h;
    term_fx_2k1 = subs(f, x, term_x_2k1);
    term_x_2k = a + 2 * h : 2 * h: a + (n - 2) * h;
    term_fx_2k = subs(f, x, term_x_2k);
    rlt = (subs(f, x, a) + subs(f, x, b) + 4 * sum(term_fx_2k1) + 2 * sum(term_fx_2k)) * h / 3;
end
