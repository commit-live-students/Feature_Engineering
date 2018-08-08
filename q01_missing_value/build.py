# %load q01_missing_value/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType']]
# Write your code here:
def imputation(dataset):
    
    imp_mean = Imputer(missing_values='NaN',strategy='mean')
    imp_mean.fit(dataset[['MasVnrArea']])
    dataset['MasVnrArea'] = imp_mean.transform(dataset[['MasVnrArea']])
    dataset['GarageType'].fillna(dataset['GarageType'].mode()[0],inplace=True)
    return dataset[['MasVnrArea','GrLivArea']],dataset[['LotShape','GarageType']]


