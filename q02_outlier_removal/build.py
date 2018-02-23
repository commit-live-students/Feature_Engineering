# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(df):
    q = df.quantile(q = 0.95)

    #criteria = (df['MasVnrArea'] < q[0]) & (df['GrLivArea'] < q[1]) & (df['SalePrice'] < q[2])
    df = df.drop(df[(df['MasVnrArea'] > q[0])].index)
    df = df.drop(df[(df['GrLivArea'] > q[1])].index)
    df = df.drop(df[(df['SalePrice'] > q[2])].index)

    return df


# Write your code here:
