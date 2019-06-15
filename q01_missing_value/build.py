# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(df):
    list = ['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']
    #missing data observing in columns
    total = df[list].isnull().sum(axis=0).sort_values(ascending=False)
    percent = ((df[list].isnull().sum(axis=0)/df[list].isnull().count(axis=0))*100).sort_values(ascending=False)

    # count the number of null values in the column and their perecentage of the total data
    missing_data_columns = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
   
    df2 = df.copy()
    df2['GarageType'] = df2['GarageType'].fillna('None')
    
    df2['MasVnrArea'] = df2['MasVnrArea'].fillna(0)
    df2['MasVnrArea'].isnull().sum()
    
    total = df2[list].isnull().sum(axis=0).sort_values(ascending=False)
    percent = ((df2[list].isnull().sum(axis=0)/df2[list].isnull().count(axis=0))*100).sort_values(ascending=False)

    # count the number of null values in the column and their perecentage of the total data
    missing_data_columns2 = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    #return df2['MasVnrArea'], df2['GarageType']

    df3 = df.copy()
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(df3[['MasVnrArea']])
    df3['MasVnrArea'] = imp_mean.transform(df[['MasVnrArea']])
    
    #Mode value imputation
    df3['GarageType'] = df3['GarageType'].fillna(df2['GarageType'].mode()[0])
    return pd.DataFrame(df3['MasVnrArea']), pd.DataFrame(df3['GarageType'])
    
imputation(ny_housing)










