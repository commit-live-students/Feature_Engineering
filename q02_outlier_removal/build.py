# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
def outlier_removal(housing_data):
    high = .95
    quant_df = housing_data.quantile(high)
    df = housing_data.drop(housing_data[(housing_data['GrLivArea']>quant_df['GrLivArea']) |
                                    (housing_data['SalePrice']>quant_df['SalePrice'])|
                                    (housing_data['MasVnrArea']>quant_df['MasVnrArea'])].index)
#housing_data[(housing_data['GrLivArea']>quant_df['GrLivArea']) | (housing_data['GrLivArea']<quant1_df['GrLivArea'])]
    return df
