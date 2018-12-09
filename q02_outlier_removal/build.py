# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def outlier_removal(dataset = housing_data):
    for col in ['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']:
        a = dataset[dataset[col] < dataset[col].quantile(0.897)]
        return a
        
    


