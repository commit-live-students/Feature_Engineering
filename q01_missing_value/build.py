# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
#housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

new_df=ny_housing[ny_housing.isnull().any(axis=1)]
housing_data = new_df[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
def imputation(housing_data):
    numeric_f=housing_data._get_numeric_data().columns
    cat_f=list(set(housing_data.columns)-set(numeric_f))
    num_df=housing_data[numeric_f]
    cat_df=housing_data[cat_f]
    imp_num_df=num_df.fillna(num_df.mean())
    imp_cat_df=cat_df.fillna(cat_df.mode().iloc[0])
    return imp_num_df,imp_cat_df
