# %load q01_missing_value/build.py
# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(housing_data):
    numeric_col = housing_data._get_numeric_data().columns
    numeric_df = housing_data[numeric_col]
    numeric_df['MasVnrArea'].fillna(numeric_df['MasVnrArea'].mean(),inplace =True)
    
    category_col = housing_data.select_dtypes(include=[object]).columns
    category_df = housing_data[category_col]
    category_df['GarageType'].fillna(category_df['GarageType'].mode()[0],inplace = True)
    
    return numeric_df, category_df







