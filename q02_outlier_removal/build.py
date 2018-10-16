# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(df):
    MasVnrAreaQuantile = df['MasVnrArea'].quantile(0.95)
    GrLivAreaQuantile = df['GrLivArea'].quantile(0.95)
    SalePriceQuantile = df['SalePrice'].quantile(0.95)

    df.drop(df[(df['MasVnrArea'] > MasVnrAreaQuantile) | (df['GrLivArea'] > GrLivAreaQuantile) | (df['SalePrice'] > SalePriceQuantile)].index, inplace = True)
    return df

outlier_removal(housing_data)


