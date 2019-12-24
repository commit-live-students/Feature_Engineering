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
    df =housing_data.drop(housing_data[(housing_data['GrLivArea']>2466.1)].index)
    df1=df.drop(df[(df['MasVnrArea']>456.0)].index)
    df2=df1.drop(df1[(df1['SalePrice']>326099.99999999994)].index)
    return df2


