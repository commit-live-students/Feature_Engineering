# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(housing_data):
    num_col = housing_data._get_numeric_data().columns
    for col in num_col:
        housing_data = housing_data.drop(housing_data[housing_data[col] > housing_data[col].quantile(0.95)].index)
    return housing_data

outlier_removal(housing_data)



