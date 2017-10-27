# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    cols = dataset.columns
    #print cols
    miss_col = dataset.columns[dataset.isnull().any()]
    #print miss_col.tolist()
    num_col = dataset._get_numeric_data().columns
    #print num_col.tolist()
    cat_col = list(set(cols) - set(num_col))
    #print cat_col
    for x in miss_col:
        if x in num_col:
            #print x
            fill_mean = Imputer(missing_values='NaN', strategy='mean')
            fill_mean.fit(dataset[[x]])
            dataset[[x]] = fill_mean.transform(dataset[[x]])
            #print(dataset[x])
            dataset[x].fillna(dataset.mean())
            #ans= dataset[x].isnull().values.any()
            #print ans
        else:
            dataset[x] = dataset[x].fillna(dataset[x].mode()[0])
            cat_df = dataset[x]
            #print(dataset[x])
            #ans= dataset[x].isnull().values.any()
            #print ans
    num_df = dataset[num_col]
    cat_df = dataset[cat_col]
    return num_df, cat_df
