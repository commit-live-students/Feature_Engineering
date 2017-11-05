# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(df):
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(df[['MasVnrArea']])
    df[['MasVnrArea']] =imp_mean.transform(df[['MasVnrArea']])

    df['GarageType'] = df['GarageType'].fillna(df['GarageType'].mode()[0])
    return df[['MasVnrArea']],pd.core.frame.DataFrame(df['GarageType'])
