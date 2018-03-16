# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
housing_data

# Write your code here:

def outlier_removal(data):

    df = data.copy()


    q = df.quantile(0.95, axis = 0)

    df = df.drop(df[df.MasVnrArea > q[0]].index)
    df = df.drop(df[df.GrLivArea > q[1]].index)
    df = df.drop(df[df.SalePrice > q[2]].index)

    return df


#outlier_removal(housing_data)


