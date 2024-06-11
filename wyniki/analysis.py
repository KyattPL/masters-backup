import pandas as pd
import pingouin as pg
from scipy.stats import shapiro, levene, wilcoxon, mannwhitneyu, kruskal


# Load your data
version_a = pd.read_csv('verA.csv')
version_b = pd.read_csv('verB.csv')

# Descriptive statistics for demographic data (columns 0-6)
demographics_a = version_a.iloc[:, 0:7].describe()
demographics_b = version_b.iloc[:, 0:7].describe()

print("Demographics for Version A")
print(demographics_a)

print("Demographics for Version B")
print(demographics_b)

# Extract questionnaire responses (assuming they start from column 7 and onwards)
read_merged = pd.read_excel('merged_in_order.xlsx')

read_merged.iloc[:, 7:26].describe().to_excel('NONAI_statistics.xlsx')
read_merged.iloc[:, 30:49].describe().to_excel('AI_statistics.xlsx')

non_ai_a = version_a.iloc[:, 7:26]
ai_a = version_a.iloc[:, 30:49]
non_ai_b = version_b.iloc[:, 30:49]
ai_b = version_b.iloc[:, 7:26]

normality_results = {
    'Form_A_Non_AI': [shapiro(non_ai_a[col]) for col in non_ai_a.columns],
    'Form_A_AI': [shapiro(ai_a[col]) for col in ai_a.columns],
    'Form_B_Non_AI': [shapiro(non_ai_b[col]) for col in non_ai_b.columns],
    'Form_B_AI': [shapiro(ai_b[col]) for col in ai_b.columns]
}

levene_results_non_ai = [levene(non_ai_a[cols[0]], non_ai_b[cols[1]])
                         for cols in zip(non_ai_a.columns, non_ai_b.columns)]
levene_results_ai = [levene(ai_a[cols[0]], ai_b[cols[1]])
                     for cols in zip(ai_a.columns, ai_b.columns)]

# Wilcoxon signed-rank test
wilcoxon_results_a = [wilcoxon(non_ai_a[cols[0]], ai_a[cols[1]], correction=True)
                      for cols in zip(non_ai_a.columns, ai_a.columns)]
wilcoxon_results_b = [wilcoxon(non_ai_b[cols[0]], ai_b[cols[1]], correction=True)
                      for cols in zip(non_ai_b.columns, ai_b.columns)]

# Mann-Whitney U test
mannwhitneyu_results_non_ai = [mannwhitneyu(
    non_ai_a[cols[0]], non_ai_b[cols[1]], use_continuity=True) for cols in zip(non_ai_a.columns, non_ai_b.columns)]
mannwhitneyu_results_ai = [mannwhitneyu(
    ai_a[cols[0]], ai_b[cols[1]], use_continuity=True) for cols in zip(ai_a.columns, ai_b.columns)]


def create_test_results_df(test_results, test_name, columns):
    data = {
        'Question': columns,
        f'{test_name}_Statistic': [result[0] for result in test_results],
        f'{test_name}_p-value': [result[1] for result in test_results]
    }
    return pd.DataFrame(data)


columns = non_ai_a.columns

# Normality results
normality_df = pd.DataFrame({
    'Question': columns,
    'Form_A_Non_AI_Statistic': [res[0] for res in normality_results['Form_A_Non_AI']],
    'Form_A_Non_AI_p-value': [res[1] for res in normality_results['Form_A_Non_AI']],
    'Form_A_AI_Statistic': [res[0] for res in normality_results['Form_A_AI']],
    'Form_A_AI_p-value': [res[1] for res in normality_results['Form_A_AI']],
    'Form_B_Non_AI_Statistic': [res[0] for res in normality_results['Form_B_Non_AI']],
    'Form_B_Non_AI_p-value': [res[1] for res in normality_results['Form_B_Non_AI']],
    'Form_B_AI_Statistic': [res[0] for res in normality_results['Form_B_AI']],
    'Form_B_AI_p-value': [res[1] for res in normality_results['Form_B_AI']]
})

# Levene's test results
levene_non_ai_df = create_test_results_df(
    levene_results_non_ai, 'Levene_Non_AI', columns)
levene_ai_df = create_test_results_df(levene_results_ai, 'Levene_AI', columns)

# Wilcoxon test results
wilcoxon_a_df = create_test_results_df(
    wilcoxon_results_a, 'Wilcoxon_A', columns)
wilcoxon_b_df = create_test_results_df(
    wilcoxon_results_b, 'Wilcoxon_B', columns)

# Mann-Whitney U test results
mannwhitneyu_non_ai_df = create_test_results_df(
    mannwhitneyu_results_non_ai, 'Mann_Whitney_Non_AI', columns)
mannwhitneyu_ai_df = create_test_results_df(
    mannwhitneyu_results_ai, 'Mann_Whitney_AI', columns)

# Write all results to an Excel file
with pd.ExcelWriter('statistical_tests_results.xlsx', engine='openpyxl') as writer:
    normality_df.to_excel(writer, sheet_name='Normality_Results', index=False)
    levene_non_ai_df.to_excel(
        writer, sheet_name='Levene_Non_AI_Results', index=False)
    levene_ai_df.to_excel(writer, sheet_name='Levene_AI_Results', index=False)
    wilcoxon_a_df.to_excel(
        writer, sheet_name='Wilcoxon_A_Results', index=False)
    wilcoxon_b_df.to_excel(
        writer, sheet_name='Wilcoxon_B_Results', index=False)
    mannwhitneyu_non_ai_df.to_excel(
        writer, sheet_name='Mann_Whitney_Non_AI_Results', index=False)
    mannwhitneyu_ai_df.to_excel(
        writer, sheet_name='Mann_Whitney_AI_Results', index=False)

print("Results saved to statistical_tests_results.xlsx")


def create_test_results_df(test_results, test_name, columns):
    data = {
        'Question': columns,
        f'{test_name}_Statistic': [result[0] for result in test_results],
        f'{test_name}_p-value': [result[1] for result in test_results]
    }
    return pd.DataFrame(data)


columns = non_ai_a.columns

kruskal_results = []
for cols in zip(non_ai_a.columns, ai_a.columns, non_ai_b.columns, ai_b.columns):
    stat, p_value = kruskal(
        non_ai_a[cols[0]], ai_a[cols[1]], non_ai_b[cols[2]], ai_b[cols[3]])
    kruskal_results.append((cols[0], stat, p_value))

kruskal_df = pd.DataFrame(kruskal_results, columns=[
                          'Question', 'Kruskal_Statistic', 'p-value'])

# Write all results to an Excel file
with pd.ExcelWriter('non_parametric_tests_results.xlsx', engine='openpyxl') as writer:
    kruskal_df.to_excel(
        writer, sheet_name='Kruskal_Results', index=False)

print("Results saved to non_parametric_tests_results.xlsx")
