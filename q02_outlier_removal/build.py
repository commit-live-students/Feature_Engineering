# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(housing_data):
    housing_data = housing_data.drop(
    housing_data[(housing_data['MasVnrArea'] > housing_data['MasVnrArea'].quantile(0.95)) |
                 (housing_data['GrLivArea'] >  housing_data['GrLivArea'].quantile(0.95)) |
                 (housing_data['SalePrice'] >  housing_data['SalePrice'].quantile(0.95))
                ].index)

    return housing_data
