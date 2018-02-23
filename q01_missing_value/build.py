# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):

    # Imputation Using Imputer
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(housing_data[['MasVnrArea']])
    housing_data['MasVnrArea'] = imp_mean.transform(housing_data[['MasVnrArea']])
    #print(ny_housing["MasVnrArea"])

    #Mode value imputation
    housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['GarageType'].mode()[0])
    #print(ny_housing['GarageType'])
    #housing_data.info()

    return housing_data[['MasVnrArea', 'GrLivArea']], housing_data[['LotShape', 'GarageType']]
