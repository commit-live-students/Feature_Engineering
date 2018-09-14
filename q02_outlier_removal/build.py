# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    data=housing_data.copy()
    MasVnrArea=data['MasVnrArea'].quantile(.95)
    GrLivArea=data['GrLivArea'].quantile(.95)
    SalePrice=data['SalePrice'].quantile(.95)
    data.drop(data[data['MasVnrArea']>MasVnrArea].index,inplace=True)
    data.drop(data[data['GrLivArea']>GrLivArea].index,inplace=True)
    data.drop(data[data['SalePrice']>SalePrice].index,inplace=True)
    return data
    

