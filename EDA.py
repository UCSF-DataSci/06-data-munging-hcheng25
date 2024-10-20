import pandas as pd

df = pd.read_csv('messy_population_data.csv')
with open('eda_results.txt', 'wt') as fout:
    print(df.info(), '\n', file = fout) # prints into terminal
    print(df.describe(), '\n', file = fout)
    # count unique values
    print('Unique values per column:', file = fout)
    print(df.nunique(), '\n', file = fout)
    # find mean for numeric columns
    print('Column means:', file = fout)
    print(df.mean(skipna = True, numeric_only = True), '\n', file = fout)
    # count the number of each unique value in each column
    print(df.value_counts(subset = "income_groups", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "age", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "gender", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "year", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "population", sort = False), '\n', file = fout)
    # count NAs in each column
    print('Total NA count by column:', file = fout)
    print(df.isna().sum(), '\n', file = fout)
    # count the number of completely duplicated rows
    print('Total duplicated rows:', file = fout)
    print(df.duplicated().sum(), '\n', file = fout)