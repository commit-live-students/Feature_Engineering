# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation(df):
    df_num = df._get_numeric_data()
    df_cat = df[list(set(df.columns)-set(df._get_numeric_data().columns))]

    df_num_miss_cols = df_num.columns[df_num.isnull().any()==True]
    df_num_miss = df_num[df_num_miss_cols]
    df_cat_miss_cols = df_cat.columns[df_cat.isnull().any()==True]
    df_cat_miss = df_cat[df_cat_miss_cols]

    df_num_miss.fillna(df_num_miss.mean(),inplace=True)
    df_cat_miss.fillna(df_cat_miss.mode()['GarageType'][0],inplace=True)

    return df_num_miss,df_cat_miss
# Write your code here:
