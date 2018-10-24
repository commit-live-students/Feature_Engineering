# %load q01_missing_value/build.py
# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
df = housing_data.copy()
df1 =df.select_dtypes(include=['int','float'])
# Write your code here:

def imputation(df):
    df1=df.select_dtypes(include=['int','float'])
    df2=df.select_dtypes(include=['object'])
    df2['LotShape']=df2['LotShape'].fillna(df2['LotShape'].mode().index[0])
    df2['GarageType']=df2['GarageType'].fillna(df2['GarageType'].value_counts().index[0])
    for col in df1.columns:
        df1[col] = df1[col].fillna(df1[col].mean())

    return df1,df2


