# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    df=dataset.copy()
    num_columns=df.select_dtypes(include=['float64','int64'])

    quatile_95=num_columns.quantile(0.95)

    for colname in num_columns:
        quantile=quatile_95[colname]
        print quantile
        df=df.drop(df[df[colname]>quantile].index)

    return df
