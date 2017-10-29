# %load q01_missing_value/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer
import numpy as np


# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
#housing_data.head()

# Write your code here:
def imputation(dataset):
    #seperating numerical and categorial
    numeric_feature= [a for a in range(len(dataset.dtypes)) if dataset.dtypes[a] in ['int64','float64']]
    #print(numeric_feature)
    numeric_data=dataset.iloc[:,numeric_feature]
    #print(numeric_data)
    fill_nan=Imputer(missing_values=np.nan,strategy='mean',axis=1)
    imputed_df=pd.DataFrame(fill_nan.fit_transform(numeric_data))
    #print(imputed_df.head())
    column_data= list(dataset.select_dtypes(include=['category','object']))
    #print(column_data)
    column_feature=dataset[column_data]
    #print(column_feature.head())
    column_feature['LotShape']=column_feature['LotShape'].fillna(column_feature['LotShape'].mode()[0])
    #print(column_feature['LotShape'])
    column_feature['GarageType']=column_feature['GarageType'].fillna(column_feature['GarageType'].mode()[0])
    #print(column_feature.head())
    return imputed_df,column_feature
# imp, imp1 =imputation(housing_data)
# print(type(imp))
# print(type(imp1))

# Return_val = imp.isnull().values.any()
# Return_val1 = imp1.isnull().values.any()

# print(Return_val)
# print(Return_val1)
