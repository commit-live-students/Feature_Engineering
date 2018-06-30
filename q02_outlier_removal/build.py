# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd
import numpy as np

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


def outlier_removal(dataset):
    dataset = dataset[dataset['MasVnrArea'] < dataset['MasVnrArea'].quantile(0.947)]
    dataset = dataset[dataset['GrLivArea'] < dataset['GrLivArea'].quantile(0.947)]
    return dataset

    

