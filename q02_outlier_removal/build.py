# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(housing_data):

    a=housing_data.MasVnrArea.quantile(q=0.95)

    b=housing_data.GrLivArea.quantile(q=0.95)
    c=housing_data.SalePrice.quantile(q=0.95)
    df1 = housing_data[(housing_data.MasVnrArea <= a) &(housing_data.GrLivArea <= b) &(housing_data.SalePrice <=c)]

    return df1
    
