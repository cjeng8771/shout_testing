% SNR Calculations for Error Estimation

% Column 1: repNum = 0
T_1 = readtable('pxx_1.csv');
snr_1 = zeros(height(T_1),1);

for r = 1:height(T_1)
    snr_1(r) = db2mag(snr(T_1{r,:}));
end

% Column 2: repNum = 1
T_2 = readtable('pxx_2.csv');
snr_2 = zeros(height(T_2),1);

for r = 1:height(T_2)
    snr_2(r) = db2mag(snr(T_2{r,:}));
end

% Column 3: repNum = 2
T_3 = readtable('pxx_3.csv');
snr_3 = zeros(height(T_3),1);

for r = 1:height(T_3)
    snr_3(r) = db2mag(snr(T_3{r,:}));
end

% Column 4: repNum = 3
T_4 = readtable('pxx_4.csv');
snr_4 = zeros(height(T_4),1);

for r = 1:height(T_4)
    snr_4(r) = db2mag(snr(T_4{r,:}));
end

save 'snrs.mat' snr_1 snr_2 snr_3 snr_4