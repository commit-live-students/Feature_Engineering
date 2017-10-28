# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation (dataset):
    df = dataset.copy()
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df1 = df.select_dtypes(include=numerics)
    imp_mean = Imputer(missing_values = 'NaN', strategy = 'mean')
    for col in df1:
        imp_mean.fit(df1[[col]])
        df1[col] = imp_mean.transform(df1[[col]])
    df2 = df.select_dtypes(exclude=numerics)
    for col in df2:
        df2[col] = df2[col].fillna(df2[col].mode()[0])
    return df1,df2
# Write your code here:
