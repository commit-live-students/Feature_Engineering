# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def outlier_removal(dataset):
    qual_vals = dataset.quantile(0.95)

    dataset =dataset.drop(dataset[dataset['MasVnrArea'] > qual_vals[0]].index)
    dataset= dataset.drop(dataset[dataset['GrLivArea'] > qual_vals[1]].index)
    dataset= dataset.drop(dataset[dataset['SalePrice'] > qual_vals[2]].index)

    return dataset
