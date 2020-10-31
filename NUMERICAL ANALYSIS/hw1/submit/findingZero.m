function func = findingZero
    func.bisection = @bisection;
    func.newton = @newton;
    func.secant = @secant;
end

function p = bisection(f, p1, p2, TOL)
    syms x
    v1 = subs(f, x, p1)
    v2 = subs(f, x, p2)

    if abs(v1) < TOL
        p = p1
        return
    end
    if abs(v2) < TOL
        p = p2
        return
    end

    mid = (p1 + p2) / 2
    vm = subs(f, x, mid)

    if abs(vm) < TOL
        p = mid
        return
    end

    if v1 * vm < 0
        p2 = mid
    else
        p1 = mid
    end
    p = bisection(f, p1, p2, TOL);
end

function p = newton(f, p0, TOL, maxIter)
    syms x
    v0 = subs(f, x, p0)

    if abs(v0) < TOL | maxIter <= 0
        p = p0
    else
        p1 = p0 - v0 / subs(diff(f), x, p0)
        p = newton(f, p1, TOL, maxIter - 1);
    end
end

function p = secant(f, p0, p1, TOL, maxIter)
    syms x
    v0 = subs(f, x, p0)
    v1 = subs(f, x, p1)

    if abs(v0) < TOL
        p = p0
        return
    end

    if abs(v1) < TOL | maxIter <= 0
        p = p1
        return
    end

    p2 = p1 - v1 * (p1 - p0) / (v1 - v0)
    p = secant(f, p1, p2, TOL, maxIter - 1);
end
