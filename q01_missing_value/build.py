# Default imports
import pandas as pd

# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


def imputation(df):
    df = df[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
    numerical = ['int64','float64']
    categorical = ['object']

    df_numerical = df.select_dtypes(include=numerical)
    for column in df_numerical.columns:
        df_numerical[column].fillna(df_numerical[column].mean(),inplace=True)

    df_categorical = df.select_dtypes(include=categorical)
    for column in df_categorical.columns:
        df_categorical[column].fillna(df_categorical[column].mode()[0],inplace=True)

    return df_numerical,df_categorical
