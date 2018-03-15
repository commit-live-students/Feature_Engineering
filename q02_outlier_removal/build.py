# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(housing_data):
    df = housing_data.copy()
    filter1 = housing_data.quantile(0.95)
    df = df.drop(df[(df['GrLivArea']>filter1['GrLivArea']) | (df['MasVnrArea']>filter1['MasVnrArea']) |  (df['SalePrice']>filter1['SalePrice'])].index)
    return df
