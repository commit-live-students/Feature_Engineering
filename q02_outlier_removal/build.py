# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
ny_housing
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
housing_data

# Write your code here:
def outlier_removal(housing_data):
    x = housing_data.quantile(q=0.95)
    housing_data.drop(housing_data[housing_data.MasVnrArea > x[0]].index,inplace = True)
    housing_data.drop(housing_data[housing_data.GrLivArea > x[1]].index,inplace = True)
    housing_data.drop(housing_data[housing_data.SalePrice > x[2]].index,inplace = True)
    return housing_data
    
outlier_removal(housing_data)
    

