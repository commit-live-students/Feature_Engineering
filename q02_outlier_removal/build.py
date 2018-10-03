# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Data
df = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = df[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:
def outlier_removal(housing_data):
    mean=housing_data['MasVnrArea'].loc[housing_data['MasVnrArea'].notnull()].mean()
    housing_data['MasVnrArea']=housing_data['MasVnrArea'].fillna(mean)
    highly_occured=housing_data['GarageType'].loc[housing_data['GarageType'].notnull()].value_counts().index[0]
    housing_data['GarageType']=housing_data['GarageType'].fillna(highly_occured)
    
    return housing_data[(housing_data['MasVnrArea']<=housing_data['MasVnrArea'].quantile(0.95)) & (housing_data['GrLivArea']<=housing_data['GrLivArea'].quantile(0.95)) & (housing_data['SalePrice']<=housing_data['SalePrice'].quantile(0.95)) ]


c=outlier_removal(housing_data)
c







