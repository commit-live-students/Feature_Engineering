# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(housing_data):
    a=housing_data.MasVnrArea.quantile(0.95)
    b=housing_data.GrLivArea.quantile(0.95)
    c=housing_data.SalePrice.quantile(0.95)
    print(a,b,c)

    df1 = housing_data[(housing_data.MasVnrArea <= 499) & (housing_data.GrLivArea <= 2466) & (housing_data.SalePrice <=326100)]


    df = housing_data[(housing_data.MasVnrArea <= a) & (housing_data.GrLivArea <= b) & (housing_data.SalePrice <=c)]
    return df1
