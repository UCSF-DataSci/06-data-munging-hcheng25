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
    - Non-Null Count:119412
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
- A relatively small, but significant fraction of data entries have the number 3 written under *gender*, which is likely an invalid option as most studies separate *gender* into two categories.
- Potential impact: data entries with a 3 cannot contribute to the statistics of appropriate *gender* category, and the 3 creates a third *gender* category that likely should not be there at all

**Future years**
- The *year* column contains entries that are in the future, which should not be possible.
- Potential impact: the data is incorrect and could affect any analysis of time trends

**Possible outliers**
- The *population* column has high variability, and there are several values considered outliers when using 1.5 times the IQR to identify them.
- Potential impact: Outliers can indicate an error in measurement or data entry. Additionally, true outliers could skew statistical analyses and result in conclusions that do not reflect the average in reality.

**NA values**
- Several thousand values are not valid
- Affects all columns
- Potential impact: using incomplete data for data analysis may result in inaccurate statistical analyses if some entries can only contribute to some columns of data and not others

**Duplicated Rows**
- .duplicated() found 2950 rows of data that are completely duplicated.
- Affects all columns
- Potential impact: would cause the duplicated data to have an inaccurately large impact during analysis compared to non-duplicated data

## 2. Data Cleaning

### Issue 1: NA Values
- **Cleaning Method**: Exclude rows that contain an NA value
- **Implementation**:
```python
#code
```
- **Justification**: Incomplete data may lead to inaccurate analyses when placed in context of each other since some statistics may include a particular data entry while others would exclude it. Because the fraction of NA entries is relatively small, it would be beneficial to exclude those rows altogether.

### Issue 2: Future years and Gender 3
- **Cleaning Method**: Remove rows containing a year past 2023 and a *gender* entry of "3"
- **Implementation**:
```python
#code
```
- **Justification**: It's impossible to be certain what year was intended to be entered in the invalid future year entries or what gender was intended to be entered for those with "3" entered, so it would be easier to exclude those rows altogether.

### Issue 3: *population* outliers

### Issue 3: Typos in *income_groups*
- **Cleaning Method**: Remove *_typo* from the end of entries that have them
- **Implementation**:
```python
#code
```
- **Justification**: In a real dataset typos may be harder to correct since they can happen in ways that result in the original intended entry being unknown. In this project, however, the typos are very straightforward and can be corrected to their intended original entries.

### Issue 4: Duplicated rows
- **Cleaning Method**: Remove rows that are complete duplicates, leaving only one entry.
- **Implementation**:
```python
#code
```
- **Justification**: The rows that are exact duplicates of other rows are likely actual data that were mistakenly entered multiple times, so removing all but one of the duplicates would ensure the impact of that data during statistical analyses is not overstated.