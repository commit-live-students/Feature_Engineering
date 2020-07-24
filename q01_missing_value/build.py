# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    df2=dataset.copy()
    df2["LotShape"] = df2["LotShape"].fillna('Reg')
    df2["GarageType"] = df2["GarageType"].fillna('Attchd')

    for col in ('MasVnrArea', 'GrLivArea', 'SalePrice'):
        df2[col] = df2[col].fillna(df2[col].mean())

    return df2.iloc[:,[0,1,4]],df2.iloc[:,[2,3]]
