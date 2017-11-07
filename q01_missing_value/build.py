# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(housing_data):
    housing_data['MasVnrArea'] = housing_data['MasVnrArea'].fillna(housing_data['MasVnrArea'].mean())
    housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['GarageType'].mode()[0])
    imp = housing_data[['MasVnrArea','GrLivArea']]
    imp1 = housing_data[['LotShape','GarageType']]

    return imp,imp1
