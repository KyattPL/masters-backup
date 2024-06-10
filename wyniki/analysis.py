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
wilcoxon_results_a = [wilcoxon(non_ai_a[cols[0]], ai_a[cols[1]])
                      for cols in zip(non_ai_a.columns, ai_a.columns)]
wilcoxon_results_b = [wilcoxon(non_ai_b[cols[0]], ai_b[cols[1]])
                      for cols in zip(non_ai_b.columns, ai_b.columns)]

# Mann-Whitney U test
mannwhitneyu_results_non_ai = [mannwhitneyu(
    non_ai_a[cols[0]], non_ai_b[cols[1]]) for cols in zip(non_ai_a.columns, non_ai_b.columns)]
mannwhitneyu_results_ai = [mannwhitneyu(
    ai_a[cols[0]], ai_b[cols[1]]) for cols in zip(ai_a.columns, ai_b.columns)]

# ttest_results_a = ttest_rel(version_a.iloc[:, 7:26], version_a.iloc[:, 30:49])
# ttest_results_b = ttest_rel(version_b.iloc[:, 7:26], version_b.iloc[:, 30:49])

# Assuming ttest_results_a and ttest_results_b are Ttest_relResult objects
# ttest_results_a_df = pd.DataFrame(ttest_results_a._asdict())
# ttest_results_b_df = pd.DataFrame(ttest_results_b._asdict())

# Save the results to CSV
# ttest_results_a_df.to_csv('ttest_rel_version_A.csv')
# ttest_results_b_df.to_csv('ttest_rel_version_B.csv')

# Separate the responses for AI and non-AI from both versions
# non_ai_a = version_a.iloc[:, 7:26].values.flatten()
# ai_a = version_a.iloc[:, 30:49].values.flatten()
# non_ai_b = version_b.iloc[:, 7:26].values.flatten()
# ai_b = version_b.iloc[:, 30:49].values.flatten()

# # Czy średnia dla wersji AI w przypadku formularza A i B jest taka sama
# ind1_result = ttest_ind(ai_a, ai_b)

# # Czy średnia dla wersji NONAI w przypadku formularza A i B jest taka sama``
# ind2_result = ttest_ind(non_ai_a, non_ai_b)

# # Wychodzą suuuper małe czyyyli że kolejność chyba ma znaczenie (?)
# # W sensie średnia dla tej samej części ale z formularza A i B jest wyraźnie inna
# print(ind1_result)
# print(ind2_result)

# Assuming ind1_result and ind2_result are Ttest_indResult objects
# index_label = ['AI', 'Non-AI']
# result_df = pd.DataFrame(
#     {'AI': [ind1_result.pvalue], 'Non-AI': [ind2_result.pvalue]}, index=index_label)

# Save the results to CSV
# result_df.to_csv('ttest_ind_AI_NonAI.csv')

# Create DataFrames for each set of results


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

kruskal_results_non_ai = [kruskal(non_ai_a[cols[0]], non_ai_b[cols[1]])
                          for cols in zip(non_ai_a.columns, non_ai_b.columns)]
kruskal_results_ai = [kruskal(ai_a[cols[0]], ai_b[cols[1]])
                      for cols in zip(ai_a.columns, ai_b.columns)]

# Kruskal-Wallis test results
kruskal_non_ai_df = create_test_results_df(
    kruskal_results_non_ai, 'Kruskal_Non_AI', columns)
kruskal_ai_df = create_test_results_df(
    kruskal_results_ai, 'Kruskal_AI', columns)

# Write all results to an Excel file
with pd.ExcelWriter('non_parametric_tests_results.xlsx', engine='openpyxl') as writer:
    kruskal_non_ai_df.to_excel(
        writer, sheet_name='Kruskal_Non_AI_Results', index=False)
    kruskal_ai_df.to_excel(
        writer, sheet_name='Kruskal_AI_Results', index=False)

print("Results saved to non_parametric_tests_results.xlsx")

# only_quest_a = pd.read_excel('only_quest_a.xlsx')
# only_quest_b = pd.read_excel('only_quest_b.xlsx')

# # Create a DataFrame suitable for ANOVA
# df_a = pd.melt(only_quest_a, id_vars=['Sygnatura czasowa'], value_vars=only_quest_a.columns[7:45],
#                var_name='condition', value_name='score')
# df_b = pd.melt(only_quest_b, id_vars=['Sygnatura czasowa'], value_vars=only_quest_b.columns[7:45],
#                var_name='condition', value_name='score')

# df_a['order'] = 'non-AI first'
# df_b['order'] = 'AI first'

# # Modify the 'Sygnatura czasowa' column to make subject IDs unique across groups
# df_a['Sygnatura czasowa'] = df_a['Sygnatura czasowa'].astype(str) + '_A'
# df_b['Sygnatura czasowa'] = df_b['Sygnatura czasowa'].astype(str) + '_B'

# df = pd.concat([df_a, df_b])

# # Mixed-Design ANOVA
# aovrm = pg.mixed_anova(data=df, dv='score', subject='Sygnatura czasowa',
#                        within='condition', between='order')

# aovrm.to_csv('ANOVA_results.csv')
