# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:
def outlier_removal(df):
    vQuantile = df.quantile(q=0.95)
    df = df.drop(df[(df['MasVnrArea']>vQuantile['MasVnrArea'])
                    | (df['GrLivArea']>vQuantile['GrLivArea'])
                    | (df['SalePrice']>vQuantile['SalePrice'])
                    ].index)
    return df

a = outlier_removal(housing_data)
print type(a)
print a.shape
print a.head()
