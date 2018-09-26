# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    df = dataset.copy()
    
    num_cols = df.select_dtypes(include=['float64','int64'])
    
    quantile_values = num_cols.quantile(0.95)
    
    for col in num_cols:
        quantile = quantile_values[col]
        print(quantile)
        df = df.drop(df[df[col]>quantile].index)
        
    return df

outlier_removal(housing_data)


