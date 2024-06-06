import pandas as pd
import pingouin as pg
from scipy.stats import ttest_rel, ttest_ind

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

# Czyli porównanie czy przejście z AI->NONAI albo NONAI->AI jest statystyczne różne
ttest_results_a = ttest_rel(version_a.iloc[:, 7:26], version_a.iloc[:, 30:49])
ttest_results_b = ttest_rel(version_b.iloc[:, 7:26], version_b.iloc[:, 30:49])

# Assuming ttest_results_a and ttest_results_b are Ttest_relResult objects
ttest_results_a_df = pd.DataFrame(ttest_results_a._asdict())
ttest_results_b_df = pd.DataFrame(ttest_results_b._asdict())

# Save the results to CSV
ttest_results_a_df.to_csv('ttest_rel_version_A.csv')
ttest_results_b_df.to_csv('ttest_rel_version_B.csv')

# Separate the responses for AI and non-AI from both versions
non_ai_a = version_a.iloc[:, 7:26].values.flatten()
ai_a = version_a.iloc[:, 30:49].values.flatten()
non_ai_b = version_b.iloc[:, 7:26].values.flatten()
ai_b = version_b.iloc[:, 30:49].values.flatten()

# Czy średnia dla wersji AI w przypadku formularza A i B jest taka sama
ind1_result = ttest_ind(ai_a, ai_b)

# Czy średnia dla wersji NONAI w przypadku formularza A i B jest taka sama``
ind2_result = ttest_ind(non_ai_a, non_ai_b)

# Wychodzą suuuper małe czyyyli że kolejność chyba ma znaczenie (?)
# W sensie średnia dla tej samej części ale z formularza A i B jest wyraźnie inna
print(ind1_result)
print(ind2_result)

# Assuming ind1_result and ind2_result are Ttest_indResult objects
index_label = ['AI', 'Non-AI']
result_df = pd.DataFrame(
    {'AI': [ind1_result.pvalue], 'Non-AI': [ind2_result.pvalue]}, index=index_label)

# Save the results to CSV
result_df.to_csv('ttest_ind_AI_NonAI.csv')

only_quest_a = pd.read_excel('only_quest_a.xlsx')
only_quest_b = pd.read_excel('only_quest_b.xlsx')

# Create a DataFrame suitable for ANOVA
df_a = pd.melt(only_quest_a, id_vars=['Sygnatura czasowa'], value_vars=only_quest_a.columns[7:45],
               var_name='condition', value_name='score')
df_b = pd.melt(only_quest_b, id_vars=['Sygnatura czasowa'], value_vars=only_quest_b.columns[7:45],
               var_name='condition', value_name='score')

df_a['order'] = 'non-AI first'
df_b['order'] = 'AI first'

# Modify the 'Sygnatura czasowa' column to make subject IDs unique across groups
df_a['Sygnatura czasowa'] = df_a['Sygnatura czasowa'].astype(str) + '_A'
df_b['Sygnatura czasowa'] = df_b['Sygnatura czasowa'].astype(str) + '_B'

df = pd.concat([df_a, df_b])

# Mixed-Design ANOVA
aovrm = pg.mixed_anova(data=df, dv='score', subject='Sygnatura czasowa',
                       within='condition', between='order')

aovrm.to_csv('ANOVA_results.csv')
