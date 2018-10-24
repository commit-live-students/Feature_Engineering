# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer


# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
def imputation(dataset):
    imp_mean = Imputer(missing_values='NaN', strategy='mean')
    imp_mean.fit(dataset[['MasVnrArea']])
    masVnrArea = imp_mean.transform(dataset[['MasVnrArea']]).ravel()
    garageType = dataset.GarageType.fillna(dataset.GarageType.mode()[0])
    return pd.DataFrame(masVnrArea), pd.DataFrame(garageType)
    

# Write your code here:
