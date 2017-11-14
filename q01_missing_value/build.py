# Default imports
import pandas as pd
import numpy as np
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
dataset=housing_data

# Write your code here:
def imputation(dataset):
    df_num = pd.DataFrame()
    df_cat = pd.DataFrame()

    for col in dataset.columns:
        if dataset[col].dtype == np.object:
            df_cat[col] = dataset[col] = dataset[col].fillna(dataset[col].mode()[0])
        elif dataset[col].dtype == np.int or dataset[col].dtype == np.float :
            df_num[col] = dataset[col] = dataset[col].fillna(dataset[col].mean())
    return df_cat, df_num

#imputation(dataset)
