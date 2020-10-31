clear;
clc;

syms x;
ployFuncLis = {@lagrange, @neville, @newton};
statMat{1} = [
            1 30;
            5 33;
            8 35;
            12 27;
            15 29;
            19 32;
            22 35;
            26 37;
            29 39;
                    ];
statMat{2} = [
            2 36;
            4 35;
            9 30;
            11 28;
            16 34;
            18 32;
            23 36;
            25 37;
            30 40;
                    ];
statMat{3} = [
            6 42;
            13 36;
            20 38;
            27 40;
                    ];
statMat{4} = [
            7 32;
            14 34;
            21 36;
            28 35;
                    ];

for i=1:size(statMat, 2)
        for j=1:size(ployFuncLis, 2)
            display(['Method: ', func2str(ployFuncLis{j})]);
            display(['Wheather station id: ', num2str(i)]);
            Px = ployFuncLis{j}(statMat{i});
            Px = collect(Px);
            P10 = eval(subs(Px, x, 10));
            display(['Interpolating polynomials: ']);
            display(Px);
            display(['Estimated PM2.5 at T=10 is: ', num2str(P10)]);
            display('==========================================');
    end
end
