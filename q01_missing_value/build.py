# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation(housing_data) :
    df = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
   # print housing_data
    df2 = df[['MasVnrArea','GrLivArea','SalePrice']].copy()
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(df2[['MasVnrArea']])
    imp_mean.fit(df2[['GrLivArea']])
    imp_mean.fit(df2[['SalePrice']])
    df2['MasVnrArea'] = imp_mean.transform(df[['MasVnrArea']]).ravel()
    df2['GrLivArea'] = imp_mean.transform(df[['GrLivArea']]).ravel()
    df2['SalePrice'] = imp_mean.transform(df[['SalePrice']]).ravel()
    df3 = df[['LotShape','GarageType']].copy()
    df3['LotShape'] = df3['LotShape'].fillna(df3['LotShape'].mode()[0])
    df3['GarageType'] = df3['GarageType'].fillna(df3['GarageType'].mode()[0])
    #df2=df.copy('MasVnrArea','GrLivArea','SalePrice')
    #new = old.drop('B', axis=1)
    return df2,df3


# Write your code here:
