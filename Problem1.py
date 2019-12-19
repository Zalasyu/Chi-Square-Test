"""
Problem 1 (10 points)
In an experiment to study the dependence of hypertension on smoking habits, the
following data were taken on 180 individuals:

'Observed' Data
________________________________________________________________________________
                | Nonsmokers    |  Moderate - smokers   |   Heavy - smokers
Hypertension    |    21         |          36           |        30
No hypertension |    48         |          26           |        19
________________________________________________________________________________

- Formulate null and alternative hypothesis for this study, and choose a level of
significance.
- Draw a contingency table for the expected data, if the null hypothesis were true.
- Calculate the value of the statistic, as well as the number of degrees of freedom,
and decide whether you can reject or not reject the null hypothesis.
"""
####################################################################################

from scipy.stats import chi2_contingency
from scipy.stats import chi2

"""
A.
Null Hypothesis: Non-smokers, moderate-smokers, and heavy-smokers are in equal proportion having hypertension and no hypertension.
Alternative Hypothesis: Non-smokers, moderate-smokers, and heavy-smokers are in equal proportion having hypertension and no hypertension.
Level of Significance: alpha = 0/01
"""
alpha = 0.01
# Contingency Table
actual_data = [[21, 36, 30],
               [48, 26, 19]]
####################################################################################
"""
B.
'Observed' Data
________________________________________________________________________________
                | Nonsmokers    |  Moderate - smokers   |   Heavy - smokers     |   Total
Hypertension    |    21         |          36           |        30             |    87
No hypertension |    48         |          26           |        19             |    93
Total           |    69         |          62           |        49             |    180
________________________________________________________________________________

"""
# Hypertension Ratios
hyp_ratio = 87 / 180  # Of the 180 participants 48.33% developed Hypertension.
nonhyp_ratio = 93 / 180  # Of the 180 participants 51.67% developed Hypertension.
"""
Expected Statements if null hypothesis is true:
Of the 180 participants in this study, 48.33% developed Hypertension and 51.67% did not.
"""
# Non-Smoker Column
nonsmk_expected_hyp = hyp_ratio * 69
print(f'Non-smoker hyp expected: {nonsmk_expected_hyp}\n')
nonsmk_expected_nonhyp = nonhyp_ratio * 69
print(f'Non-smoker non-hyp expected: {nonsmk_expected_nonhyp}\n')

# Moderate - Smoker Column
modsmk_expected_hyp = hyp_ratio * 62
print(f'Moderate-smoker hyp expected: {modsmk_expected_hyp}\n')
modsmk_expected_nonhyp = nonhyp_ratio * 62
print(f'Moderate-smoker nonhyp expected: {modsmk_expected_nonhyp}\n')

# Heavy - Smoker Column
heavsmk_expected_hyp = hyp_ratio * 49
print(f'Heavy-smoker hyp expected: {heavsmk_expected_hyp}\n')
heavsmk_expected_nonhyp = nonhyp_ratio * 49
print(f'Heavy-smoker nonhyp expected: {heavsmk_expected_nonhyp}\n')

"""
B.
'Expected' Data
________________________________________________________________________________
                | Nonsmokers    |  Moderate - smokers   |   Heavy - smokers     |   Total
Hypertension    |    33.35*     |          29.96*       |        23.68*         |    87
No hypertension |    35.65*     |          32.03*       |        25.32*         |    93
Total           |    69         |          62           |        49             |    180
________________________________________________________________________________
"""
print(actual_data)
stat, p, dof, expected = chi2_contingency(actual_data)
print(expected)
####################################################################################
"""
C.
Chi-Squared Statistic
The test statistic should be designed to describe, with a single
number, how much the “observed” frequencies differ from the
“expect” frequencies (i.e, the frequencies we would expect if the null hypothesis is true)

χ2 = ∑((O − E)^2)/E

If Statistic >= Critical Value: significant result, reject null hypothesis (H0), dependent.
If Statistic < Critical Value: not significant result, fail to reject null hypothesis (H0), independent.

degrees of freedom: (rows - 1) * (cols - 1)
"""
# Degrees of Freedom
rows = 2
columns = 3
DOF = (rows - 1) * (columns - 1)
print(f'The Degrees of Freedom for the chi-squared distribution is: {DOF}\n')

# χ2 = ∑((O − E)^2)/E
print(f'The chi-statistic is: {stat}')  # Chi-statistic
prob = 1 - alpha
critical = chi2.ppf(prob, DOF)
print(f'The critical value is: {critical}\n')

if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
#############################################################################################
# OUPUT
"""
Non-smoker hyp expected: 33.35

Non-smoker non-hyp expected: 35.650000000000006

Moderate-smoker hyp expected: 29.96666666666667

Moderate-smoker nonhyp expected: 32.03333333333334

Heavy-smoker hyp expected: 23.683333333333334

Heavy-smoker nonhyp expected: 25.31666666666667

[[21, 36, 30], [48, 26, 19]]

[[33.35       29.96666667 23.68333333]
 [35.65       32.03333333 25.31666667]]
 
The Degrees of Freedom for the chi-squared distribution is: 2

The chi-statistic is: 14.463579015563466
The critical value is: 9.21034037197618

Dependent (reject H0)
"""