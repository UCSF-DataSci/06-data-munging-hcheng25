import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('messy_population_data.csv')
with open('eda_results.txt', 'wt') as fout:
    df.info() # prints into terminal
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
    # identify outliers in population
    Q1 = df['population'].quantile(0.25)
    Q3 = df['population'].quantile(0.75)
    IQR = Q3 - Q1
    popdata = df[~((df['population'] < (Q1 - 1.5 * IQR)) | (df['population'] > (Q3 + 1.5 * IQR)))]
    popdata = popdata.sort_values(by = 'population')
    popdata = popdata.dropna()
    print(popdata, '\n', file = fout)
    # how many rows have future years?
    futureyear = df[df['year']>2023]
    print('# of rows/columns with future years:', futureyear.shape, file = fout)