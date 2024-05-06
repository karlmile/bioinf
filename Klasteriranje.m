clear  % ocisti "workspace"
close all % zatvori sve "figures"

% Podaci za treniranje
load azip    % 16 x 16 bitmape vekorizirane u 256 x 1 stupce od A
%..........................................................................
% podaci za testiranje
load testzip % 16 x 16 bitmape vekorizirane u 256 x 1 stupce od A1
load dtest   % dzip(i) = j <=> i-stupac od A1 sadrzi znamenku j
%..........................................................................
A  = azip ;
A1 = testzip ;
D1 = dtest   ;
clear azip dzip testzip dtest 
centers0 = cell(1, 10);
centers1 = cell(1, 10);


[m,n] = size(A);
digits = zeros(n);
%suma = zeros(10, m);
%broj = zeros(10, m);

for i = 1 : n
    digits{i} = mod(i-1, 10);
end

breakCondition = 0;
for i = 1 : 10000
    for znamenka = 1 : 10
        indexi = find(digits == znamenka-1);
        znamenkei = A(:, indexi);
        centar = mean(znamenkei);
        centers0{znamenka-1} = centar;
            
    end
    
    for j = 1 : n
        slika = A(j)
        znamenka = digits(j)
        najmanji = 1;
        for k = 1 : 10
            stara_norma = norm(centers0(najmanji) - slika);
            nova_norma = norm(centers0(k) - slika);
            if(nova_norma < stara_norma)
                najmanji = k;
            end
        end
        
    end
    
    
    (znamenkei - centers0) .^ 2 
    
    sum(digits[i])
end
