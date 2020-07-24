# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(data):
    df=data.copy()
    numerical_col=data.select_dtypes(include=['int64','float64'])
    for col in numerical_col:
        df=df.drop(df[df[col]>numerical_col.quantile(0.95)[col]].index)

    return df
