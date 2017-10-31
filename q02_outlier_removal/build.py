# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def outlier_removal(dataset):
    df = dataset
    df = df.drop(df[(df['MasVnrArea'] > 456) | (df['GrLivArea']>2466) | (df['SalePrice'] > 326100)].index)
    return df
