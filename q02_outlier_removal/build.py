# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(housing_data):

    quan_mva =housing_data['MasVnrArea'].quantile(0.95)
    quan_gla =housing_data['GrLivArea'].quantile(0.95)
    quan_sp =housing_data['SalePrice'].quantile(0.95)
    housing_data= housing_data.drop(housing_data[(housing_data['MasVnrArea']>quan_mva) | (housing_data['GrLivArea']>quan_gla) | (housing_data['SalePrice']>quan_sp)].index)
    return housing_data
