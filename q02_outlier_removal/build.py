# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(df):
    quantile_MasArea = df['MasVnrArea'].quantile(0.95)
    quantile_grLivArea = df['GrLivArea'].quantile(0.95)
    quantile_SalePrice = df['SalePrice'].quantile(0.95)

    df1 = df.drop(df[df['MasVnrArea']>quantile_MasArea].index)
    df2 = df1.drop(df1[df1['GrLivArea']>quantile_grLivArea].index)
    df3 = df2.drop(df2[df2['SalePrice']>quantile_SalePrice].index)



    return df3
# Write your code here:
