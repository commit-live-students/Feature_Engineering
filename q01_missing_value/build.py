# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def imputation(housing_data):

    df2 = housing_data.copy()

    lot_shape_imputer = df2['LotShape'].value_counts().index.max()
    garage_type_imputer = df2['GarageType'].value_counts().index.max()

    df2['LotShape'] = df2['LotShape'].fillna(lot_shape_imputer)
    df2['GarageType'] = df2['GarageType'].fillna(garage_type_imputer)

    for col in ('MasVnrArea', 'GrLivArea', 'SalePrice'):
        df2[col] = df2[col].fillna(df2[col].mean())

    return df2[['MasVnrArea', 'GrLivArea', 'SalePrice']], df2[['LotShape','GarageType']]

#imputation(housing_data)
