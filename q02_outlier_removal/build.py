# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(df):
    quantiles = df.quantile(0.95)
    for column in df.columns:
        if column in quantiles:
            df = df.drop(df[(df[column] > quantiles[column])].index)
    return df
