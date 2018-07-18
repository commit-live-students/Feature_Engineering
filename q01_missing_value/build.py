# %load q01_missing_value/build.py
# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    na = housing_data.isnull().sum()
    print(na)
    housing_data[['MasVnrArea']] = housing_data[['MasVnrArea']].fillna(housing_data[['MasVnrArea']].mean())
    housing_data[['GarageType']] = housing_data[['GarageType']].apply(lambda x: x.fillna(x.value_counts().index[0]))
    return housing_data[['MasVnrArea']], housing_data[['GarageType']]

