import pandas as pd

# remove row if any cell contains NA
def rm_NA(dataframe):
    dataframe.dropna(inplace = True)
    return dataframe

# remove future years and gender 3
def rm_yeargender(dataframe):
    # remove rows with years later than 2024
    dataframe = dataframe[dataframe['year'] <= 2023]
    # remove rows with gender = 3
    dataframe = dataframe[dataframe['gender'] != 3]
    return dataframe

# remove population outliers
def rm_popout(dataframe):
    Q1 = df['population'].quantile(0.25)
    Q3 = df['population'].quantile(0.75)
    IQR = Q3 - Q1
    dataframe = dataframe[dataframe["population"] > Q1 - 1.5*IQR]
    dataframe = dataframe[dataframe["population"] < Q3 + 1.5*IQR]
    return dataframe

# remove "_typo" from income_groups
def income_typofix(dataframe):
    dataframe = dataframe.replace(to_replace='income_typo', value='income', regex=True)
    return dataframe

# remove duplicate rows
def rm_dupes(dataframe):
    dataframe = dataframe.drop_duplicates(keep = 'first')
    return dataframe

if __name__ == "__main__":
    df = pd.read_csv('messy_population_data.csv')
    fout = open('cleaning_log.txt', 'wt')
    
    # remove NA
    print('Step 1: remove NAs', '\n', file = fout)
    df = rm_NA(df)
    print('Rows and columns remaining after removing NAs:', df.shape, '\n', file = fout)

    # remove future years and gender 3
    print('Step 2: remove future years and gender 3', '\n', file = fout)
    df = rm_yeargender(df)
    print(df.value_counts(subset = "gender", sort = False), '\n', file = fout)
    print(df.value_counts(subset = "year", sort = False), '\n', file = fout)
    print('Rows and columns remaining after removing future years and gender 3:', df.shape, '\n', file = fout)

    # remove population outliers
    print('Step 3: remove population outliers', '\n', file = fout)
    df = rm_popout(df)
    print('Rows and columns remaining after removing population outliers:', df.shape, '\n', file = fout)

    # fix income_groups typos
    print('Step 4: fix income_groups typos', '\n', file = fout)
    df = income_typofix(df)
    print(df.value_counts(subset = "income_groups", sort = False), file = fout)
    print('No typos remaining', '\n', file = fout)

    # remove duplicate rows
    print('Step 5: remove duplicate rows', '\n', file = fout)
    df = rm_dupes(df)
    print('Duplicate rows remaining:', df.duplicated().sum(), file = fout)
    print('Rows and columns remaining after removing duplicate rows:', df.shape, '\n', file = fout)
    
    # print somee final stats
    print('Rows and columns remaining after cleaning', df.shape, '\n', file = fout)
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

    fout.close
    df.to_csv('cleaned_population_data.csv')