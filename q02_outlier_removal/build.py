# %load q02_outlier_removal/build.py
# Default imports
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
#housing_data.describe()
def outlier_removal(housing_data):
    housing_data1=housing_data[housing_data.loc[:,['MasVnrArea','GrLivArea','LotShape','GarageType','SalePrice']].notnull()]
    housing_data1=housing_data1.dropna()
    housing_data2=housing_data1.sort_values(['MasVnrArea', 'GrLivArea','SalePrice'])
    upper_quartile = np.percentile(housing_data2['SalePrice'],95)
    h2=(housing_data2[housing_data2['SalePrice']<upper_quartile])
    return(h2)

outlier_removal(housing_data)

