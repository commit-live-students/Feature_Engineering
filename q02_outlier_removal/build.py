# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(housing_data):
    numeric_df = housing_data._get_numeric_data()
    numeric_df = numeric_df.drop(['SalePrice'], axis=1)
    for column in numeric_df.columns:
        quantile_95 = housing_data[column].quantile(0.95)
        index_to_drop = housing_data[housing_data[column] > quantile_95].index
        housing_data = housing_data.drop(index_to_drop)
        
    return housing_data





