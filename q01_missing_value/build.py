# Default imports
import pandas as pd
import numpy as np
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    cols = dataset.columns[dataset.isnull().any()].tolist()
    num_types = ['int8', 'int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    num_cols = dataset.select_dtypes(include=num_types).columns.tolist()
    for val in cols:
        if val in num_cols:
            temp = dataset[dataset.loc[:,val] != 0][val]
            dataset.loc[dataset.loc[:,val] == 0,val] = temp.mean()
            dataset.loc[dataset.loc[:,val].isnull(), val] = temp.mean()

        else:
            x = dataset.loc[dataset.loc[:,val].notnull(), val]
            z = np.unique(x, return_counts=True)
            y = np.unique(x, return_counts=True)[1].tolist()
            ind = y.index(max(y))
            dataset.loc[dataset.loc[:,val].isnull(), val] = z[0][ind]

    return dataset[list(set(cols).intersection(set(num_cols)))], dataset[list(set(cols) - set(num_cols))]
