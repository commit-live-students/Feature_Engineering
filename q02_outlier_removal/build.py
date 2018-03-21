# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(df):
    df2 = df.copy()
    numeric_cols =df2.select_dtypes(include=['float64','int64'])
    quant = numeric_cols.quantile(0.95)
    for col in numeric_cols:
        df2 = df2.drop(df2[df2[col]>quant[col]].index)
    return df2
