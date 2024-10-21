[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/u8FyG16T)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16614397)
# Data Cleaning Assignment: Population Dataset
## 1. Initial State Analysis
- **Name**: messy_population_data.csv
- **Rows**: 125718
- **Columns**: 5

### Column Details
- **income_groups**
    - Data type: Categorical
    - Non-Null Count: 119412
    - NA Count: 6306
    - Unique Values: 8
- **age**
    - Data type: Numeric
    - Non-Null Count: 119495
    - NA Count: 6223
    - Unique Values: 101
    - Mean: 50.0
    - SD: 29.15
- **gender**
    - Data type: Categorical
    - Non-Null Count: 119811
    - NA Count: 5907
    - Unique Values:3
- **year**
    - Data type: Categorical
    - Non-Null Count: 119516
    - NA Count: 6202
    - Unique Values: 169
- **population**
    - Data type: Numeric
    - Non-Null Count: 119378
    - NA Count: 6340
    - Unique Values: 114925
    - Mean: 1.112983e+08
    - SD: 1.265205e+09

### Possible Issues
**Typos in *income_groups***
- Some values under *income_groups* have *_typo* appended to the end
- Potential impact: adds additional invalid possible values for this column, causes data entries that should be grouped together when stratified by *income_groups* to be separated

**Gender 3**
- A relatively small, but significant fraction of data entries (around 6000 entries) have the number 3 written under *gender*, which is likely an invalid option as most studies separate *gender* into two categories.
- Potential impact: data entries with a 3 cannot contribute to the statistics of appropriate *gender* category, and the 3 creates a third *gender* category that likely should not be there at all

**Future years**
- The *year* column contains over 60000 entries that are in the future, which should not be possible.
- Potential impact: the data is incorrect and could affect any analysis of time trends

**Possible outliers**
- The *population* column has several values considered outliers when using 1.5 times the IQR to identify them, including some extreme values that are unrealistic as data entries for population.
- Potential impact: outliers can indicate an error in measurement or data entry. Additionally, true outliers could skew statistical analyses and result in conclusions that do not reflect the average in reality.

**NA values**
- Several thousand values are not valid
- Affects all columns
- Potential impact: using incomplete data for data analysis may result in inaccurate statistical analyses if some entries can only contribute to some columns of data and not others

**Duplicated Rows**
- .duplicated() found 2950 rows of data that are completely duplicated.
- Affects all columns
- Potential impact: would cause the duplicated data to have an inaccurately large impact during analysis compared to non-duplicated data

## 2. Data Cleaning
- Details of changes to the data are logged in cleaning_log.txt

### Issue 1: NA Values
- **Cleaning Method**: Exclude rows that contain an NA value
- **Implementation**:
```python
def rm_NA(dataframe):
    dataframe.dropna(inplace = True)
    return dataframe
```
- **Justification**: Incomplete data may lead to inaccurate analyses when placed in context of each other since some statistics may include a particular data entry while others would exclude it. Because the fraction of NA entries is relatively small, it would be beneficial to exclude those rows altogether.

### Issue 2: Future years and Gender 3
- **Cleaning Method**: Remove rows containing a year past 2023 and a *gender* entry of "3"
- **Implementation**:
```python
def rm_yeargender(dataframe):
    # remove rows with years later than 2024
    dataframe = dataframe[dataframe['year'] <= 2023]
    # remove rows with gender = 3
    dataframe = dataframe[dataframe['gender'] != 3]
    return dataframe
```
- **Justification**: It's impossible to be certain what year was intended to be entered in the invalid future year entries or what gender was intended to be entered for those with "3" entered, so it would be easier to exclude those rows altogether.

### Issue 3: *population* outliers
- **Cleaning Method**: Remove rows where the *population* value is 1.5 times the IQR less than Q1 or 1.5 times the IQR greater than Q3
- **Implementation**:
```python
def rm_popout(dataframe):
    Q1 = df['population'].quantile(0.25)
    Q3 = df['population'].quantile(0.75)
    IQR = Q3 - Q1
    dataframe = dataframe[dataframe["population"] > Q1 - 1.5*IQR]
    dataframe = dataframe[dataframe["population"] < Q3 + 1.5*IQR]
    return dataframe
```
- **Justification**: The most extreme population values are certainly invalid, such as an extremely low population of 28. However, because it is impossible to tell which of the more moderate outliers are invalid entries, it could be beneficial to exclude the outliers of the initial data set, keeping in mind that the outliers are less representative of the average subject. This isn't a perfect solution, as it is possible for a true outlier to be excluded from analysis, but it is likely the best approach given that there are many values that are certainly invalid entries.

### Issue 4: Typos in *income_groups*
- **Cleaning Method**: Remove *_typo* from the end of entries that have them
- **Implementation**:
```python
def income_typofix(dataframe):
    dataframe = dataframe.replace(to_replace='income_typo', value='income', regex=True)
    return dataframe
```
- **Justification**: In a real dataset typos may be harder to correct since they can happen in ways that result in the original intended entry being unknown. In this project, however, the typos follow a straightforward pattern and can be corrected to their intended original entries.

### Issue 5: Duplicated rows
- **Cleaning Method**: Remove rows that are complete duplicates, leaving only one entry.
- **Implementation**:
```python
def rm_dupes(dataframe):
    dataframe = dataframe.drop_duplicates(keep = 'first')
    return dataframe
```
- **Justification**: The rows that are exact duplicates of other rows are likely actual data that were mistakenly entered multiple times, so removing all but one of the duplicates would ensure that those data entries do not have a disproportionately strong effect on statistical analyses

## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv
- **Rows**: 39757
- **Columns**: 5

### Column Details
- **income_groups**
    - Data type: Categorical
    - Non-Null Count: 39757
    - NA Count: 0
    - Unique Values: 4
- **age**
    - Data type: Numeric
    - Non-Null Count: 39757
    - NA Count: 0
    - Unique Values: 101
    - Mean: 53.03
    - SD: 28.44
- **gender**
    - Data type: Categorical
    - Non-Null Count: 39757
    - NA Count: 0
    - Unique Values: 2
- **year**
    - Data type: Categorical
    - Non-Null Count: 39757
    - NA Count: 0
    - Unique Values: 74
- **population**
    - Data type: Numeric
    - Non-Null Count: 39757
    - NA Count: 0
    - Unique Values: 39308
    - Mean: 4.786459e+06
    - SD: 4.860492e+06

### Reflection and future steps
- The cleaned data set takes care of many of the issues of the dirty data sets by removing NA values, duplicate rows, and invalid entries (*gender*, *year*, and *income_groups*).
- My biggest challenge in this project was determining the approach to fix issues when it came to incorrect data entries. While I was aware that this project was focused on an artificially dirtied dataset, I tried to consider how the data should be handled in a real-world situation, where typos and data entry mistakes can happen and where outliers do exist. While I feel comfortable with my exclusion of invalid entries under age and gender because I have no way of ascertaining the intended value in a hypothetically real dataset, the outliers in population are still a big question for me.
- In the real world I might have a better idea of what values I am expecting i.e. what values are outliers for certain, but in this data set, where the variability of the population data was so high, it was difficult to remove outliers and on top of that, because the variability was so high I think in hindsight that could be justification to believe that at least some of those extreme outliers are true values.
- I think further improvements could be made to this data by further cleaning the population data. After my initial step to remove the outliers, there remained many extremely high or low values, likely because the variability was so high to begin with that removing outliers still left many values that were extreme. Alternatively, if I were to redo this project, I may leave out the outlier exclusion step altogether because the high variability could be an indication that the extreme values are true measures rather than typos or entry mistakes.