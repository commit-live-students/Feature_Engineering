from sklearn.preprocessing import Imputer
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation(housing_data):
    #Computing mean of the numerical variable
    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(housing_data[['MasVnrArea']])
    housing_data[['MasVnrArea']] = imp_mean.transform(housing_data[['MasVnrArea']])


    #Computing mode of the categorical variable
    housing_data[['GarageType']] = housing_data['GarageType'].fillna(housing_data['GarageType'].mode()[0])

    return(housing_data[["MasVnrArea"]].head(),housing_data[["GarageType"]].head())
