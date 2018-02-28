# Default imports
import pandas as pd
#import numpy as np
from sklearn.preprocessing import Imputer
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    housing_data['GarageType'] = housing_data['GarageType'].fillna('None')
    imput = Imputer(missing_values = 'NaN', strategy = 'mean')
    imput.fit(housing_data[['MasVnrArea']])
    housing_data['MasVnrArea'] = imput.transform(housing_data[['MasVnrArea']])
    return pd.DataFrame(housing_data['MasVnrArea']), pd.DataFrame(housing_data['GarageType'])

    """housing_data2 = housing_data
    imput = Imputer(missing_values = 'NaN', strategy = 'mode')
    imput.fit(housing_data2)
    cat_housing = pd.DataFrame(imput.transform(housing_data2))
    print (housing_data2)#(cat_housing)"""




print imputation(dataset=housing_data)
