"""
Problem 2 (10 points)
A college infirmary conducted an experiment to determine the degree of relief provided
by three cough remedies. Each cough remedy was tried on 50 students and the following
data recorded:

              NyQuil             Robitussin      Triaminic     Total
No relief       11                  13              9           33
Some relief     32                  28              27          87
Total relief    7                   9               14          30
Total           50                  50              50          150

Test the hypothesis that the three cough remedies are equally efective. Use a P-value
in your conclusion.
"""
#######################################################################################################################
from scipy.stats import chi2_contingency
from scipy.stats import chi2
"""
A.
FIRST (OVERALL) 
Overall:
Null Hypothesis: NyQuil, Robitussin, Triaminic all provide an equal relief response to participants.
Alternative Hypothesis: One or more cough remedies provides significant relief.
"""
alpha = 0.01
overall_actual = [[11, 13, 9],
                  [32, 28, 27],
                  [7, 9, 14]]
# Relief Ratios (Overall)
No_re_overall = 33/150
print(f'For the overall test, 22% had no relief from any of the cough remedies\n')
some_re_overall = 87/150
print(f'For the overall test, 58% had some relief from any of the cough remedies\n')
total_re_overall = 30/150
print(f'For the overall test, 20% had no relief from any of the cough remedies\n')

"""
'Expected' Contingency Table (if H0 True)

              NyQuil             Robitussin      Triaminic     Total
No relief       11*                 11*              11*         33
Some relief     29*                 29*              29*         87
Total relief    10*                 10*              10*         30
Total           50                  50              50          150

"""
print(overall_actual)
stat, p, dof, expected_overall = chi2_contingency(overall_actual)
print(expected_overall)
#################################
"""
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
rows = 3
columns = 3
DOF_overall = (rows - 1) * (columns - 1)
print(f'The Degrees of Freedom for the chi-squared distribution is: {DOF_overall}\n')

# χ2 = ∑((O − E)^2)/E
print(f'The chi-statistic is: {stat}')  # Chi-statistic
prob = 1 - alpha
critical = chi2.ppf(prob, DOF_overall)
print(f'The critical value is: {critical}\n')

if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0).\nNo need to conduct post-hoc chi tests.')

#######################################################################################################################
"""
Apply Holm-Sidak Correction
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
"""
alpha_1 = 1-(1-0.01)**(1/(3-1+1))
alpha_2 = 1-(1-0.01)**(1/(3-2+1))
alpha_3 = 1-(1-0.01)**(1/(3-3+1))
#######################################################################################################################
"""
B.
Draw Contingency Table for each comparison:
1. NyQuil vs. Robitussin
2. NyQuil vs. Triaminic
3. Robitussin vs. Triaminic
"""
# 'Observed' Contingency Tables
Ny_Ro_actual = [[11, 13],
                [32, 28],
                [7, 9]]
print(Ny_Ro_actual)
stat1, p1, dof1, expected1 = chi2_contingency(Ny_Ro_actual)
print(expected1)
###############################
"""
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
row1 = 3
column1 = 2
DOF1 = (row1 - 1) * (column1 - 1)
print(f'The Degrees of Freedom for the chi-squared distribution is: {DOF1}\n')

# χ2 = ∑((O − E)^2)/E
print(f'The chi-statistic is: {stat1}')  # Chi-statistic
#######################################################################################################################

Ny_Tr_actual = [[11, 9],
                [32, 27],
                [7, 14]]
print(Ny_Tr_actual)
stat2, p2, dof2, expected2 = chi2_contingency(Ny_Tr_actual)
print(expected2)


"""
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
row2 = 3
column2 = 2
DOF2 = (row2 - 1) * (column2 - 1)
print(f'The Degrees of Freedom for the chi-squared distribution is: {DOF2}\n')

# χ2 = ∑((O − E)^2)/E
print(f'The chi-statistic is: {stat2}')  # Chi-statistic

#######################################################################################################################
Ro_Tr_actual = [[13, 9],
                [28, 27],
                [9, 14]]
print(Ro_Tr_actual)
stat3, p3, dof3, expected2 = chi2_contingency(Ro_Tr_actual)
print(expected2)

"""
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
row3 = 3
column3 = 2
DOF3 = (row3 - 1) * (column3 - 1)
print(f'The Degrees of Freedom for the chi-squared distribution is: {DOF3}\n')

# χ2 = ∑((O − E)^2)/E
print(f'The chi-statistic is: {stat3}')  # Chi-statistic

#######################################################################################################################
"""
Sort p-values from least to greatest to be compared with increasing alphas.
"""
pvalue = {}
pvalue['NyRo'] = p1
pvalue['NyTr'] = p2
pvalue['RoTr'] = p3

print(f'\nThe p-values to be sorted: \n{pvalue}\n\nBelow is the sorted pvalues from least to greatest.')

sorted_pvalues_keys = sorted(pvalue, key=pvalue.__getitem__)
print(sorted_pvalues_keys)
sorted_pvalues_values = sorted(pvalue.values())
print(sorted_pvalues_values)
print('')

alphas = [alpha_1,alpha_2,alpha_3]

for i in range(len(sorted_pvalues_values)):
    if sorted_pvalues_values[i] < alphas[i]:
        print(f'There is a statistical difference between: \n{sorted_pvalues_keys[i]}\n')
        print(f'{sorted_pvalues_values[i]} <= {alphas[i]}')
    else:
        print(f'There is no statistical difference between: \n{sorted_pvalues_keys[i]}\n')
        print(f'{sorted_pvalues_values[i]} > {alphas[i]}')
########################################################################################################################
# OUTPUT
"""
For the overall test, 22% had no relief from any of the cough remedies

For the overall test, 58% had some relief from any of the cough remedies

For the overall test, 20% had no relief from any of the cough remedies

[[11, 13, 9], [32, 28, 27], [7, 9, 14]]
[[11. 11. 11.]
 [29. 29. 29.]
 [10. 10. 10.]]
The Degrees of Freedom for the chi-squared distribution is: 4

The chi-statistic is: 3.810031347962383
The critical value is: 13.276704135987622

Independent (fail to reject H0).
No need to conduct post-hoc tests.

#########################################

Ny vs. Ro

[[11, 13], [32, 28], [7, 9]]

[[12. 12.]
 [30. 30.]
 [ 8.  8.]]
The Degrees of Freedom for the chi-squared distribution is: 2

The chi-statistic is: 0.6833333333333333

#########################################

Ny vs. Tr

[[11, 9], [32, 27], [7, 14]]

[[10.  10. ]
 [29.5 29.5]
 [10.5 10.5]]
The Degrees of Freedom for the chi-squared distribution is: 2

The chi-statistic is: 2.9570621468926555

#########################################

Ro vs. Tr

[[13, 9], [28, 27], [9, 14]]

[[11.  11. ]
 [27.5 27.5]
 [11.5 11.5]]
The Degrees of Freedom for the chi-squared distribution is: 2

The chi-statistic is: 1.8324110671936757

The p-values to be sorted: 
{'NyRo': 0.7105850269122547, 'NyTr': 0.2279723171412597, 'RoTr': 0.4000340807627175}

Below is the sorted pvalues from least to greatest.
['NyTr', 'RoTr', 'NyRo']
[0.2279723171412597, 0.4000340807627175, 0.7105850269122547]

There is no statistical difference between: 
NyTr

0.2279723171412597 > 0.003344506587403595
There is no statistical difference between: 
RoTr

0.4000340807627175 > 0.005012562893380035
There is no statistical difference between: 
NyRo

0.7105850269122547 > 0.010000000000000009
"""