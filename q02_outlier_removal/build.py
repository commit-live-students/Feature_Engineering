# Default imports
import pandas as pd

# Data
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


def outlier_removal(dataset):
    cols = dataset._get_numeric_data().columns.tolist()
    print cols
    q1 = dataset['MasVnrArea'].quantile(0.95)
    q2 = dataset['GrLivArea'].quantile(0.95)
    q3 = dataset['SalePrice'].quantile(0.95)
    dataset = dataset.drop(dataset[(dataset['MasVnrArea']>q1)].index)
    dataset = dataset.drop(dataset[(dataset['GrLivArea']>q2)].index)
    dataset = dataset.drop(dataset[(dataset['SalePrice']>q3)].index)
    print dataset.shape
    return dataset
