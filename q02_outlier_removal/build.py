# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(df):
    df_new=df
    #print(df_new.shape)
    df=df.drop(df[(df['GrLivArea']>df['GrLivArea'].quantile(0.95)) | (df['MasVnrArea']>df['MasVnrArea'].quantile(0.95)) | (df['SalePrice']>df['SalePrice'].quantile(0.95))].index)
    return (df)


