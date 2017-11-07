# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def outlier_removal(df):
    quantiles = df.quantile(q=0.95)
    for col in df.columns:
        if col in quantiles:
            df = df.drop(df[(df[col] > quantiles[col])].index)
    return df
