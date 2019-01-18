# %load q01_missing_value/build.py
# Default imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer


# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(housing_data):
    ''' Function to impute numerical data with mean
        impute categorical data with mode '''
    #Seperate numercial and categorical columns
    num_col = housing_data._get_numeric_data().columns
    cat_col = housing_data.columns.difference(num_col)

    #impute numerical data
    imput_num = Imputer(missing_values=np.NaN , strategy= 'mean')
    df_num = imput_num.fit_transform(housing_data.loc[: , num_col])
    df_num = pd.DataFrame(df_num)
    df_num.columns = num_col

    #impute categorial data
    for col in cat_col:
        housing_data.loc[: , col].fillna(housing_data.loc[:,col].mode()[0] , inplace = True)
    df_cat = housing_data.loc[:,cat_col]

    return df_num,df_cat

imputation(housing_data)



