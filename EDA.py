import pandas as pd

df = pd.read_csv('messy_population_data.csv')
with open('eda_results.txt', 'wt') as fout:
    print(df.value_counts(subset = "income_groups", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "age", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "gender", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "year", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "population", sort = False), '\n', file = fout)
    print('Total NA count by column:', file = fout)
    print(df.isna().sum(), '\n', file = fout)
    print('Total duplicated rows:', file = fout)
    print(df.duplicated().sum(), '\n', file = fout)