# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(df):

    columnsToEncode = list(df.select_dtypes(include=['category','object']))
    le = LabelEncoder()

    # Impute NAN values of categorical data
    df[columnsToEncode[1]] = df[columnsToEncode[1]].fillna("None")

    df[columnsToEncode[0]] = le.fit_transform(df[columnsToEncode[0]])
    df = pd.get_dummies(df, columns=[columnsToEncode[1]])

    return df
