# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    dataset = dataset[dataset['MasVnrArea'] <= dataset.quantile(.95)['MasVnrArea']]

    dataset = dataset[dataset['GrLivArea'] <= dataset.quantile(.95)['GrLivArea']]

    dataset = dataset[dataset['SalePrice'] <= dataset.quantile(.95)['SalePrice']]
    
    return dataset







