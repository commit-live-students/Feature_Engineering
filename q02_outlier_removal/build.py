# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal (dataset):
    a = dataset.quantile(q=0.95,interpolation = 'lower')
    Q_MasVnrArea = a['MasVnrArea']
    Q_GrLivArea = a['GrLivArea']
    Q_SalePrice = a['SalePrice']
    #Q_LotShape = a['LotShape']
    #Q_GarageType = a['GarageType']
    df1 = dataset.drop(dataset[(dataset['SalePrice']>Q_SalePrice)].index)
    df2 = df1.drop(df1[(df1['MasVnrArea']>Q_MasVnrArea)].index)
    df3 = df2.drop(df2[ (df2['GrLivArea']>Q_GrLivArea)].index)
    return df3
