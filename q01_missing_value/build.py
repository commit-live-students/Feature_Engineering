# %load q01_missing_value/build.py
# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:
#MasVnrArea  , GarageType

def imputation(housing_data):
    missinglist = list(housing_data.columns[housing_data.isnull().any()])
    cate=[]
    num=[]
    for k in missinglist :
        if (str(housing_data[k].dtypes) == 'object' ):
            housing_data[k].fillna(housing_data[k].mode()[0], inplace =True)
            cate.append(k)
        else:
            housing_data[k].fillna(housing_data[k].mean(), inplace =True)
            num.append(k)  
    return housing_data[num] ,housing_data[cate]



























