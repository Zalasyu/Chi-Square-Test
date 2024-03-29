# Chi-Square-Test
Hard coded and scipy.stats used to solve if there was an statistical significance for: 


# Problem 1
In an experiment to study the dependence of hypertension on smoking habits, the
following data were taken on 180 individuals:

actual_data = [[21, 36, 30],
               [48, 26, 19]]

- Formulate null and alternative hypothesis for this study, and choose a level of
significance.
- Draw a contingency table for the expected data, if the null hypothesis were true.
- Calculate the value of the statistic, as well as the number of degrees of freedom,
and decide whether you can reject or not reject the null hypothesis.

Null Hypothesis: Non-smokers, moderate-smokers, and heavy-smokers are in equal proportion having hypertension and no hypertension.
Alternative Hypothesis: Non-smokers, moderate-smokers, and heavy-smokers are in equal proportion having hypertension and no hypertension.


# Problem 2
A college infirmary conducted an experiment to determine the degree of relief provided
by three cough remedies. Each cough remedy was tried on 50 students and the following
data recorded:

overall_actual = [[11, 13, 9],
                  [32, 28, 27],
                  [7, 9, 14]]

Test the hypothesis that the three cough remedies are equally effective. Use a P-value
in your conclusion.

Null Hypothesis: NyQuil, Robitussin, Triaminic all provide an equal relief response to participants.
Alternative Hypothesis: One or more cough remedies provides significant relief.


# Theory:
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
