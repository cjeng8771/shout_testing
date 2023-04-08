% SNR Calculations for Error Estimation

T_1 = readtable('pxx_1.csv');
snrs_1 = zeros(height(T_1),1);

for r = 1:height(T_1)
    snrs_1(r) = snr(T_1{r,:});
end