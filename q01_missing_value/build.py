# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.preprocessing import Imputer
def imputation(dataset):
    imp_cont = Imputer(missing_values='NaN', strategy='mean')
    imp_cont.fit(housing_data[['MasVnrArea']]) # fit for field
    housing_data['MasVnrArea'] = imp_cont.transform(housing_data[['MasVnrArea']])
    masdf = pd.DataFrame(housing_data['MasVnrArea'])

    # Fill second field with None
    housing_data['GarageType'] = housing_data['GarageType'].fillna('None')
    grgdf = pd.DataFrame(housing_data['GarageType'])

    return masdf, grgdf

# print "#### Testing ####"
# a, b = imputation(housing_data)
# print type(a)
# print type(b)
# # print a
# # print a.dtypes
# print a.isnull().values.any()
# print a.isnull().values.any()
