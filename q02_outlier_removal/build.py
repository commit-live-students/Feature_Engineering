# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:

def outlier_removal(housing_data):
    housing_data.quantile(0.95)
    a = housing_data.drop(housing_data[(housing_data['MasVnrArea']>456) |
            (housing_data['GrLivArea']>2466) | (housing_data['SalePrice']>326100.0)].index)
    return a
