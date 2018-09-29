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

    
#     housing_data['MasVnrArea']=housing_data.drop(housing_data['MasVnrArea']>456.0)
#     housing_data['GrLivArea']=housing_data.drop(housing_data['GrLivArea']>2466.1)
#     housing_data['SalePrice']=housing_data.drop(housing_data['SalePrice']>326100.0)
#     return housing_data
    housing_data = housing_data.drop(housing_data[(housing_data['GrLivArea']>3000) & (housing_data['GrLivArea']<6000)].index)
    housing_data = housing_data.drop(housing_data[(housing_data['MasVnrArea']>3000) & (df['MasVnrArea']<6000)].index)
    
    return housing_data
c=outlier_removal(housing_data)
c







