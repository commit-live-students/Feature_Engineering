# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation(housing_data):

    housing_data2 = housing_data.copy()
    # Imputation Using Imputer
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(housing_data2[['MasVnrArea']])
    housing_data2['MasVnrArea'] = imp_mean.transform(housing_data[['MasVnrArea']])

    #Mode value imputation
    housing_data2['GarageType'] = housing_data2['GarageType'].fillna(housing_data['GarageType'].mode()[0])

    return housing_data2[['MasVnrArea', 'GrLivArea']],housing_data2[['LotShape', 'GarageType']]
