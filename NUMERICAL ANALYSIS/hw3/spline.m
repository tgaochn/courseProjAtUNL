function func = spline
    func.linear = @linear;
    func.quadratic = @quadratic;
    func.cubic = @cubic;
    func.cubic_r = @cubic_r;
end

function S = linear(statMat)
    syms x Si;
    S = {};
    for i = 1:size(statMat, 1) - 1
        y_i = statMat(i, 2);
        y_i1 = statMat(i + 1, 2);
        t_i = statMat(i, 1);
        t_i1 = statMat(i + 1, 1);
        S_i = y_i + (y_i1 - y_i) * (x - t_i) / (t_i1 - t_i);
        S_i = collect(S_i);
        S{i} = S_i;
    end
end

function S = quadratic(statMat)
    syms x Si;
    S = {};
    Z = [0];
    for i = 1:size(statMat, 1) - 1
        y_i = statMat(i, 2);
        y_i1 = statMat(i + 1, 2);
        t_i = statMat(i, 1);
        t_i1 = statMat(i + 1, 1);
        z_i = Z(i);
        z_i1 = -z_i + 2 * (y_i1 - y_i) / (t_i1 - t_i);

        S_i = (z_i1 - z_i) / (2 * (t_i1 - t_i)) * (x - t_i)^2 + z_i * (x - t_i) + y_i;
        % S_i = collect(S_i);
        Z = [Z z_i1];
        display(z_i1, ['z_', int2str(i)])
        % display((z_i1 - z_i) / (2 * (t_i1 - t_i)), ['a_', int2str(i)])
        S{i} = S_i;
    end
end

function S = cubic(statMat)
    syms x Si;
    S = {};
    a = statMat(:, 2);
    h = statMat(2 : end, 1) - statMat(1 : end - 1, 1);
    n = size(statMat, 1);
    A = zeros(n);
    b = [];
    d = [];
    A(1, 1) = 1;
    A(n, n) = 1;
    B = zeros(n, 1);

    for i = 2: n-1
        A(i, i - 1) = h(i - 1);
        A(i, i) = 2 * (h(i - 1) + h(i));
        A(i, i + 1) = h(i);
        B(i) = 3 * (a(i + 1) - a(i)) / h(i) - 3 * (a(i) - a(i - 1)) / h(i - 1);
    end

    c = A \ B;
    for i = 1: n - 1
        b_i = (a(i + 1) - a(i)) / h(i) - h(i) * (c(i + 1) + 2 * c(i)) / 3;
        d_i = (c(i + 1) - c(i)) / (3 * h(i));
        t_i = statMat(i, 1);
        t_i1 = statMat(i + 1, 1);

        S_i = a(i) + b_i * (x - t_i) + c(i) * (x - t_i)^2 + d_i * (x - t_i)^3;
        % S_i = collect(S_i);
        S{i} = S_i

        b = [b b_i];
        d = [d d_i];

        % display(b_i, ['b_', int2str(i)])
        % display(d_i, ['d_', int2str(i)])
    end
    display(A);
    display(B);
    display(a);
    display(c);
    display(h);
    display(b);
    display(d);
end

function S = cubic_r(statMat)
    syms x Si;
    S = {};
    a = statMat(:, 2);
    h = statMat(2 : end, 1) - statMat(1 : end - 1, 1);
    h = h(1);
    n = size(statMat, 1);
    r = 2 + sqrt(3);
    A = zeros(n);
    A(1, 1) = r;
    A(1, 2) = 1;
    A(n, n) = 1;
    B = zeros(n, 1);
    B(1) = 3 * r * (a(2) - a(1)) / (2 * h * h);

    b = [];
    d = [];

    for i = 2: n-1
        A(i, i - 1) = 1;
        A(i, i) = 4;
        A(i, i + 1) = 1;
        B(i) = ((a(i - 1) - 2 * a(i) + a(i + 1)) * 3) / (h ^ 2);
    end
    e = B;

    alpha = [e(1) / r];
    for i = 2: n-1
        alpha_i = (e(i) - alpha(end)) / r;
        alpha = [alpha alpha_i];
    end
    alpha = [alpha e(n)];

    c = zeros(1, n);
    c(n) = alpha(n);
    for i = n-1: -1: 1
        c(i) = alpha(i) - c(i + 1) / r;
    end

    c1 = A \ B;

    for i = 1: n - 1
        b_i = (a(i + 1) - a(i)) / h - h * (c(i + 1) + 2 * c(i)) / 3;
        d_i = (c(i + 1) - c(i)) / (3 * h);
        t_i = statMat(i, 1);
        t_i1 = statMat(i + 1, 1);

        S_i = a(i) + b_i * (x - t_i) + c(i) * (x - t_i)^2 + d_i * (x - t_i)^3;
        S{i} = S_i;

        b = [b b_i];
        d = [d d_i];

        % display(b_i, ['b_', int2str(i)])
        % display(d_i, ['d_', int2str(i)])
    end
    display(A);
    display(B);
    display(e);
    display(a);
    display(alpha);
    display(c);
    display(c1);
    display(h);
    display(b);
    display(d);
end
