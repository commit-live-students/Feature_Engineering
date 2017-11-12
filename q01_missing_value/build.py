# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation(housing_data):
    #total = housing_data.isnull().sum(axis=0).sort_values(ascending=False)

    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')
    imp_mean.fit(housing_data[['MasVnrArea']])
    housing_data['MasVnrArea'] = imp_mean.transform(housing_data[['MasVnrArea']])

    housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['GarageType'].mode()[0])

    df1 = pd.DataFrame(housing_data["MasVnrArea"])
    df2 = pd.DataFrame(housing_data["GarageType"])

    return(df1,df2) 
