# %load q01_missing_value/build.py
# Default imports
import pandas as pd
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns
from scipy import stats
#For some Statistics
from scipy.stats import norm, skew
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(housing_data):
    # missing data
    imp_mean=Imputer(missing_values='NaN',strategy='mean')
    housing_data['MasVnrArea']=imp_mean.fit_transform(housing_data[['MasVnrArea']])
    housing_data['GrLivArea']=imp_mean.fit_transform(housing_data[['GrLivArea']])
    housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['GarageType'].mode()[0])
    housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['LotShape'].mode()[0])
    return housing_data[['MasVnrArea','GrLivArea','SalePrice']],housing_data[['GarageType','LotShape']]


imputation(housing_data)










    
    
    


