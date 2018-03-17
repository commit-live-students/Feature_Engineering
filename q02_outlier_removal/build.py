# Default imports
import pandas as pd
import numpy as np
# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    num_types = ['int8', 'int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    num_cols = dataset.select_dtypes(include=num_types).columns.tolist()
    temp = dataset.loc[dataset.loc[:,'MasVnrArea'] != 0.0,'MasVnrArea']
    dataset.loc[dataset.loc[:,'MasVnrArea'] == 0.0, 'MasVnrArea'] = temp.mean()
    dataset.loc[dataset.loc[:,'MasVnrArea'].isnull(), 'MasVnrArea'] = temp.mean()
    dataset.loc[dataset.loc[:,'GarageType'].isnull(), 'GarageType'] = 'Attchd'
    for val in num_cols:
        col_name = str(val) + '1'
        temp_mean = dataset.loc[dataset.loc[:,val] != 0.0,val].mean()
        temp_std = dataset.loc[dataset.loc[:,val] != 0.0,val].std()
        dataset[col_name] = (dataset.loc[:,val] - temp_mean) / float(temp_std)
        dataset.loc[dataset.loc[:,col_name] > 1.78, col_name] = np.nan

    dataset.dropna(inplace=True)
    dataset.drop(labels=dataset.iloc[:,[5,6,7]].columns.values, axis=1, inplace=True)
    return dataset
