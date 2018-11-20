# %load q01_missing_value/build.py
# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
def imputation(housing_data):
    housing_data1=housing_data.loc[:,['MasVnrArea', 'GrLivArea']]
    total =housing_data1.loc[:,['MasVnrArea','GrLivArea']].notnull()
    total1 =total.notna()
    housing_data2=housing_data.loc[:,['LotShape', 'GarageType']]
    total2=housing_data2.loc[:,['LotShape', 'GarageType']].notnull()
    total3 =total2.notna()
    return(total1,total3)


