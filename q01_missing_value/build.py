# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer
import numpy as np

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    numeric_df = dataset._get_numeric_data()
    categorical_df = dataset[list(set(housing_data.columns) - set(numeric_df.columns))]
    
    for column in categorical_df.columns:
        most_frequent = categorical_df[column].value_counts().index[0]
        categorical_df[column] = categorical_df[column].replace(np.nan, most_frequent)
    
    numeric_df = numeric_df.replace(np.nan, 0)
        
    imputer = Imputer(missing_values=0, strategy='mean')
    numeric_df = pd.DataFrame(imputer.fit_transform(numeric_df), columns=numeric_df.columns)
    
    return numeric_df, categorical_df






