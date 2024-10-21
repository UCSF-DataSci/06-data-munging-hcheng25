import pandas as pd

# remove row if any cell contains NA
def rm_NA(dataframe):
    dataframe.dropna()

# remove future years and gender 3
def rm_yeargender(dataframe):
    # remove rows with years later than 2024
    dataframe = dataframe[dataframe['year'] < 2023]
    # remove rows with gender = 3
    dataframe = dataframe[dataframe['year'] != 3]

# remove population outliers
def rm_popout(dataframe):
    Q1 = df['population'].quantile(0.25)
    Q3 = df['population'].quantile(0.75)
    IQR = Q3 - Q1
    dataframe = dataframe[dataframe["population"] > Q1 - 1.5*IQR and dataframe["population"] > Q3 + 1.5*IQR]

# remove "_typo" from income_groups
def income_typofix(dataframe):
    dataframe.replace(to_replace='income_typo', value='income', regex=True)

# remove duplicate rows
def rm_dupes(dataframe):
    dataframe = dataframe.drop_duplicates(keep = 'first')

if __name__ == "__main__":
    df = pd.read_csv('messy_population_data.csv')