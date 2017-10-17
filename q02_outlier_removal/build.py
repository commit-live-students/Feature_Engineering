# Default imports
import pandas as pd
import numpy as np

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:
def outlier_removal(dataset):
    q = {}
    for col in dataset:
        if dataset[col].dtype == np.int or dataset[col].dtype == np.float:
            q[col] = dataset[col].quantile(.9545)

    for col, q3 in q.items():
        dataset = dataset[dataset[col] < q3]

    print dataset.shape
    return dataset


outlier_removal(housing_data)
