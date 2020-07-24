# %load q01_missing_value/build.py
# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(df):
    num_features = [a for a in range(len(df.dtypes)) if df.dtypes[a] in ['int64', 'float64']]
    num_data = df.iloc[:,num_features]
    num_data.fillna(num_data.mean(), inplace = True)
    
    cat_features = df.columns.difference(df.columns[num_features])
    cat_data = df.loc[:,cat_features]
    for column in list(cat_features):
        cat_data[column].fillna(cat_data[column].mode()[0], inplace=True)

    return num_data, cat_data
x,y = imputation(housing_data)
y.isnull().sum()


