import numpy as np
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def outlier_removal(housing_data):
    q = (housing_data.quantile(q=0.95 , axis = 0))
    housing_data = housing_data.drop(housing_data[housing_data.MasVnrArea > q[0]].index)
    housing_data = housing_data.drop(housing_data[housing_data.GrLivArea > q[1]].index)
    housing_data = housing_data.drop(housing_data[housing_data.SalePrice > q[2]].index)
    return(housing_data)
