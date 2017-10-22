# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    for i in dataset.columns:
        if dataset[i].dtypes == 'int64' or dataset[i].dtypes == 'float64':
            th = dataset[i].quantile(0.95)
            data = dataset[dataset[i]< th]
            data = data[1:1306]
    return data
