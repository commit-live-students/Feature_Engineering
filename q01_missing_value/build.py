# %load q01_missing_value/build.py
# Default imports
import pandas as pd
import numpy as np

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    mean = housing_data['MasVnrArea'].mean()
    dataset['GarageType'].fillna('Attchd',inplace=True)
    dataset['MasVnrArea'].fillna(int(mean),inplace=True)
    return pd.DataFrame(dataset['MasVnrArea']),pd.DataFrame(dataset['GarageType'])
housing_data['GarageType'].value_counts()






