# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd
import numpy as np
# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    p = {}
    for col in dataset:
        if dataset[col].dtype == np.int or dataset[col].dtype == np.float:
            p[col] = dataset[col].quantile(.953)

    for col, p3 in p.items():
        dataset = dataset[dataset[col] < p3]
    return dataset
