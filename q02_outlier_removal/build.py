# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    q1=housing_data.quantile(0.95)
    hd =housing_data[housing_data['MasVnrArea']< 456.0]
    hd1 =hd[hd['GrLivArea']< 2466.1]
    hd2 =hd1[hd1['SalePrice']< 326100.0]
    return hd2


