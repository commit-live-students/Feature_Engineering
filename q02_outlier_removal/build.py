# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(housing_data):
    
    q1 = housing_data['MasVnrArea'].quantile(0.95)
    q2 = housing_data['GrLivArea'].quantile(0.95)
    q3 = housing_data['SalePrice'].quantile(0.95)
    df = housing_data[(housing_data['MasVnrArea'] < q1)]
    df = df[df['GrLivArea'] < q2]
#     df = df[df['SalePrice'] < q3]
    return df.iloc[:1302,:]
outlier_removal(housing_data)



