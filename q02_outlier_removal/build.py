# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(housing_data):
    df = housing_data

    q = df["MasVnrArea"].quantile(0.95)
    #housing_data = housing_data[housing_data["MasVnrArea"] < q]
    q1 = df["GrLivArea"].quantile(0.95)
    #housing_data = housing_data[housing_data["GrLivArea"] < q1]
    q2 = df["SalePrice"].quantile(0.95)
    #df = housing_data[housing_data["SalePrice"] < q2]

    df_out = df.drop(df[(df["MasVnrArea"] > q)|
                        (df["GrLivArea"] > q1) |
                        (df["SalePrice"] > q2)].index)
    return df_out
# Write your code here:
