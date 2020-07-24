# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:
def outlier_removal(df1):
    df=df1.copy()
    q1 = df.quantile(.95)
    df=df[(df['MasVnrArea']<=q1['MasVnrArea']) & (df['GrLivArea']<=q1['GrLivArea']) & (df['SalePrice']<= q1['SalePrice'])]
    return df
    

