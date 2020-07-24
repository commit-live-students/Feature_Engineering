# Default imports
import pandas as pd
import numpy as np

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    dataset_copy = dataset.copy()
    num_df = dataset_copy.select_dtypes(include=[np.number])
    for column in num_df.columns:
        col_quantile = num_df[column].quantile(0.95)
        dataset_copy =  dataset_copy.drop(dataset_copy[dataset_copy[column] > col_quantile].index)
    return dataset_copy
