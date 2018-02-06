# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation (dataset):
    target_col='SalePrice'
    df = dataset.copy()
    cat_columns =df.select_dtypes(include=['object'])
    num_columns =df.select_dtypes(include=['float64','int64'])
    df1 = pd.DataFrame()
    df2=pd.DataFrame()

    for col in num_columns:
        if (col != target_col):
            df1[col] = df[col].fillna(df[col].mean())

    for col in cat_columns:
            df2[col] = df[col].fillna(df[col].max())

    return (df1,df2)

#df1,df2 = imputation (housing_data)
#print df1.describe(include='all')
#print df2.describe(include='all')
