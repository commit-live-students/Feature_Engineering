# Default imports
import pandas as pd
import numpy as np
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    num_df = dataset.select_dtypes(include=[np.number])
    other_df = dataset.select_dtypes(include=['object'])
    # for numeric columns
    for col in num_df.columns:
        mean_score = np.mean(num_df[col])
        num_df[col].fillna(mean_score, inplace=True)
    # for non-numeric or object columns
    for o_col in other_df.columns:
        frequent_val = pd.value_counts(other_df[o_col].dropna()).index[0]
        other_df[o_col].fillna(frequent_val, inplace=True)
    return (num_df, other_df)
