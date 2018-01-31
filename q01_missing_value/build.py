# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def imputation(dataset):
    housing_data=dataset.iloc[:,:-1]
    df2=housing_data[list(housing_data._get_numeric_data().columns)]
    df3=housing_data[list(set(housing_data.columns)-set(housing_data._get_numeric_data().columns))]
    df=df2.copy()
    df["MasVnrArea"] = df["MasVnrArea"].fillna(df["MasVnrArea"].mean())
    df["GrLivArea"] = df["GrLivArea"].fillna(df["GrLivArea"].mean())
    dfc=df3.copy() #mandatory as else  get error value is trying to be set on a copu
    for column in dfc.columns:
        dfc[column].fillna(dfc[column].mode()[0], inplace=True)
    #dfc.isnull().values.any() validation shd return false
    return df, dfc

imputation(dataset=housing_data)
