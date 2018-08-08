# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:
def outlier_removal(dataset):
    dataset = housing_data.copy()
    
    mva = dataset['MasVnrArea'].quantile(q=0.95)
    gla = dataset['GrLivArea'].quantile(q=0.95)
    spc = dataset['SalePrice'].quantile(q=0.95)
    
    dataset.drop(dataset[dataset['MasVnrArea'] > mva].index,inplace=True)
    dataset.drop(dataset[dataset['GrLivArea'] > gla].index,inplace=True)
    dataset.drop(dataset[dataset['SalePrice'] > spc].index,inplace=True)
    #f,ax = plt.subplots(2,1,figsize=(10,10))
    
    #ax[0].scatter(x=dataset['MasVnrArea'],y=dataset['SalePrice'])
    #ax[1].scatter(dataset['GrLivArea'],dataset['SalePrice'])
    
    return dataset


