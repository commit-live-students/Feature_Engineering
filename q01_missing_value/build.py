# Default imports
import pandas as pd
import numpy as np

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    for i in dataset.columns:
        if dataset[i].dtypes == 'int64' or dataset[i].dtypes=='float64':
            dataset[i] = dataset[i].fillna(dataset[i].mean(),axis=0)
        elif dataset[i].dtypes == 'object':
            dataset[i] = dataset[i].fillna(dataset[i].mode()[0],axis=0)

    data1 = dataset.select_dtypes(include=[np.float64,np.int64])
    data2 = dataset.select_dtypes(include=[np.object])

    return data1,data2
