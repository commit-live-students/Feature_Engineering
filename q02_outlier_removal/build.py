# Default imports
import pandas as pd
#import numpy as np
# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]                 


# Write your code here:
def outlier_removal(datasets):
    df2 = datasets.copy()
    numeric_cols =df2.select_dtypes(include=['float64','int64'])
    quant = numeric_cols.quantile(0.952)
    for col in numeric_cols:
        df2 = df2.drop(df2[df2[col]>quant[col]].index)
    return df2
    #return col
(outlier_removal(housing_data))
#housing_data[['MasVnrArea', 'GrLivArea']] > P[1]


