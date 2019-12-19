# Chi-Square-Test
Hard coded and scipy.stats used to solve if there was an statistical significance for: 

1.Non-smokers, moderate-smokers, and heavy-smokers are in equal proportion having hypertension and no hypertension. Alternative Hypothesis: Non-smokers, moderate-smokers, and heavy-smokers are in equal proportion having hypertension and no hypertension. 

'Observed' Data
________________________________________________________________________________
                | Nonsmokers    |  Moderate - smokers   |   Heavy - smokers
Hypertension    |    21         |          36           |        30
No hypertension |    48         |          26           |        19
________________________________________________________________________________


2. NyQuil, Robitussin, Triaminic all provide an equal relief response to participants. Alternative Hypothesis: One or more cough remedies provides significant relief.

'Observed' Data
              NyQuil             Robitussin      Triaminic     Total
No relief       11                  13              9           33
Some relief     32                  28              27          87
Total relief    7                   9               14          30
Total           50                  50              50          150


Theory:
Chi-Squared Statistic
The test statistic should be designed to describe, with a single
number, how much the “observed” frequencies differ from the
“expect” frequencies (i.e, the frequencies we would expect if the null hypothesis is true)

χ2 = ∑((O − E)^2)/E

If Statistic >= Critical Value: significant result, reject null hypothesis (H0), dependent.
If Statistic < Critical Value: not significant result, fail to reject null hypothesis (H0), independent.

degrees of freedom: (rows - 1) * (cols - 1)

Apply Holm-Sidak Correction (Multiple Pairwise comparison)
alpha = 1 - (1- a_fw)^(1/k-j+1)
# Family-wise error rate (for multiple post-hoc tests)
a_fw = 1-(1-alpha)^k
alpha = level of significance for each test
k = the number of post-hoc tests
j = time (time is invariant in this case)
alpha_fw = family-wise error rate ( We want it to be 0.01)

Must first obtain p-value for each chi-square test
    -List p-value from each test from least to greatest.

Find alpha for each post-hoc test
alpha_1 = 1-(1-0.01)^(1/3-1+1)
alpha_2 = 1-(1-0.01)^(1/3-2+1)
alpha_3 = 1-(1-0.01)^(1/3-3+1)
