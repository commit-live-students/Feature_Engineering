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
    total = df.isnull().sum(axis=0).sort_values(ascending=False)
    percent = ((df.isnull().sum(axis=0)/df.isnull().count(axis=0))*100).sort_values(ascending=False)
    # count the number of null values in the column and their perecentage of the total data
    missing_data_columns = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    #print(missing_data_columns.head())
    df_new = df.copy()
    #Numerical Imputation
    # Imputation Using Imputer
    df_new = df.copy()
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(df_new[['MasVnrArea']])
    df_new['MasVnrArea'] = imp_mean.transform(df[['MasVnrArea']])
    #Mode value imputation
    df_new['GarageType'] = df_new['GarageType'].fillna(df_new['GarageType'].mode()[0])
    return df_new['MasVnrArea'].to_frame(),df_new['GarageType'].to_frame()



