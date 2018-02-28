# Default imports
import pandas as pd
import numpy as np
# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(datasets):
    df = datasets.copy()
    num_cols = df.select_dtypes(include=['float64', 'int64'])
    quantile_95 = num_cols.quantile(0.95)
    for colu in num_cols:
        quantile = quantile_95[colu]
        print quantile
        df=df.drop(df[df[colu]>quantile].index)
    return df.shape
    #return col

print outlier_removal(housing_data)
