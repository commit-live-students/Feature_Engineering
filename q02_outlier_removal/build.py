# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
def outlier_removal(dataset):
    data=housing_data.copy()
    
    masvnr=data['MasVnrArea'].quantile(.95)
    grliv=data['GrLivArea'].quantile(.95)
    saleprice=data['SalePrice'].quantile(.95)
    data.drop(data[data['MasVnrArea']>masvnr].index,inplace=True)
    data.drop(data[data['GrLivArea']>grliv].index,inplace=True)
    data.drop(data[data['SalePrice']>saleprice].index,inplace=True)
    return data

outlier_removal(housing_data)










