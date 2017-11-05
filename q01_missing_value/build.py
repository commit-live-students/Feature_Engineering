# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(df2):
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(df2[['MasVnrArea']])
    df2[['MasVnrArea']] =imp_mean.transform(df2[['MasVnrArea']])

    df2['GarageType'] = df2['GarageType'].fillna(df2['GarageType'].mode()[0])
    return df2[['MasVnrArea']],pd.core.frame.DataFrame(df2['GarageType'])
