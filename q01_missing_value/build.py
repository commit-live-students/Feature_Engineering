# Default imports
import pandas as pd
import numpy as np

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType',\
                'SalePrice']]

def imputation(housing_data):

    df2 = housing_data.copy()

    # Separate numerical data from original data
    numeric_feature = [a for a in range(len(df2.dtypes)) if df2.dtypes[a] in ['int64','float64']]
    numeric_data = df2.iloc[:,numeric_feature]

    # Separate categorical data from original data
    cat_feature = [a for a in range(len(df2.dtypes)) if df2.dtypes[a] in ['object']]
    cat_data = df2.iloc[:,cat_feature]

    # Impute NAN values of categorical data
    for col in cat_data.columns:
        cat_data[col] = cat_data[col].value_counts().index.max()

    # Impute NAN values of numerical data
    for col in numeric_data.columns:
        numeric_data[col] = numeric_data[col].fillna(numeric_data[col].mean())

    return numeric_data, cat_data
