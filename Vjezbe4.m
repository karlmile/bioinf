clear  % ocisti "workspace"
close all % zatvori sve "figures"

% ====================== UČITAVANJE PODATAKA ===========================
% Podaci za treniranje
load azip    % 16 x 16 bitmape vekorizirane u 256 x 1 stupce od A

%..........................................................................
% podaci za testiranje
load testzip % 16 x 16 bitmape vekorizirane u 256 x 1 stupce od A1
load dtest   % dzip(i) = j <=> i-stupac od A1 sadrzi znamenku j
%..........................................................................


A  = azip ;     %Podaci za vježbanje (klasteriranje) 256x1709

A1 = testzip ;  % Podaci za testiranje
D1 = dtest   ;  % Rješenja za testiranje
clear azip dzip testzip dtest 

[m,n] = size(A);        % n je broj dokumenata, m je dimenzija vektora
digits = zeros(n,1);
k = 10;

% ======================  ===========================

W = zeros(n, n);
sigma = 100;
for i = 1 : n
    for j = 1 : n
        w = norm(A(:, i) - A(:, j));
        W(i, j) = exp(-w*w / sigma);
    end
end

en = ones(n, 1);
Wn = W * en;
D = diag(Wn);

D2 = zeros(n, n);
for i = 1 : n
    D2(i, i) = 1/sqrt(D(i, i));
end
H = D2 * W * D2;

[evec, eval] = eig(H);
[~, ind] = sort(-diag(eval));
evec = evec(:, ind);

V = evec(: , 1:k);
Z = D2 * V;

Z2 = diag(diag(Z*transpose(Z)));
for i = 1 : n
    Z2(i, i) = 1/sqrt(Z2(i, i));
end
X = Z2 * Z;
XT = X;

% 1. korak
Q = eye(k);



for iteracija = 1 : 100
    % 2. korak
    XQ = XT * Q;
    for i = 1 : n
        [~,d] = max(XQ(i, :));
        X(i, :) = zeros(1, k);
        X(i, d) = 1;
    end

    % 3. korak
    [svdU,svdD,svdV] = svd(transpose(XT)*X);
    Q = svdU*transpose(svdV);
    
end


NA = zaros(n,m);
br=1;
for i = 1 : k
    for j = 1 : n
        if(X(i,j) == 1)
            NA(br,:)=A(j,:);
            br = br+1;
        end
    end
end


IM = zeros(n, n);
sigma = 100;
for i = 1 : n
    for j = 1 : n
        w = norm(NA(:, i) - NA(:, j));
        IM(i, j) = exp(-w*w / sigma);
    end
end

imagesc(IM)



% ====================== PRIKAZ REZULTATA ===========================


