# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd
import matplotlib.pyplot as plt
# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    d = housing_data.copy()
    qMas = d.MasVnrArea.quantile(0.95)
    qGrL = d.GrLivArea.quantile(0.95)
    qSP = d.SalePrice.quantile(0.95)
    d.drop(d[d.MasVnrArea > qMas ].index, inplace=True)
    d.drop(d[d.GrLivArea > qGrL].index, inplace=True)
    d.drop(d[d.SalePrice > qSP].index, inplace=True)
    return d



