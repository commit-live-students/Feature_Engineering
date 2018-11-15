# %load q01_missing_value/build.py
# Default imports
import pandas as pd
import numpy as np
import statistics
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    categoricals = housing_data.select_dtypes(exclude=[np.number])
    categoricals['GarageType'].fillna(statistics.mode(categoricals['GarageType'].values), inplace = True)
    
    numericals = housing_data.select_dtypes(include=[np.number])
    numericals.fillna(numericals.mean(),inplace=True)
    return numericals,categoricals


