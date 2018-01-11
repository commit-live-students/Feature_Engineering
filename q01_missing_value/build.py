# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(housing_data) :

    df1 = housing_data
    df1['GarageType'] = df1['GarageType'].fillna(df1['GarageType'].mode()[0])

    df1['MasVnrArea'] = df1['MasVnrArea'].replace(0.0,df1['MasVnrArea'].mean()).fillna(df1['MasVnrArea'].mean())
    return pd.DataFrame(df1['MasVnrArea']),pd.DataFrame(df1['GarageType'])
# imputation(housing_data)[0].isnull().sum(axis=0)
