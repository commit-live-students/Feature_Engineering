# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(housing_data):
    df = housing_data

    q = df["MasVnrArea"].quantile(0.95)
    df1 = df[df["MasVnrArea"] < q]
    q1 = df["GrLivArea"].quantile(0.95)
    df2 = df[df["GrLivArea"] < q1]
    q2 = df["SalePrice"].quantile(0.95)
    df3 = df[df["SalePrice"] < q2]
    return df3
# Write your code here:
