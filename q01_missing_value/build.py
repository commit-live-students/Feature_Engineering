# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

housing_data.isnull().sum() # For finding no. of missing values in each column

# Write your code here:
def imputation(data):
    imp_mean = Imputer(missing_values='NaN', strategy='mean')
    imp_mean.fit(data['MasVnrArea'].reshape(-1,1))
    data['MasVnrArea'] = imp_mean.transform(data['MasVnrArea'].reshape(-1,1))
    data['LotShape'] = data['LotShape'].fillna(data['LotShape'].mode()[0])
    return pd.DataFrame(data['MasVnrArea']), pd.DataFrame(data['LotShape'])
