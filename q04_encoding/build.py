# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
def encoding(df):

    le = LabelEncoder()
    df['LotShape'] = le.fit_transform(df['LotShape'])
    df['GarageType'] = le.fit_transform(df['GarageType'])

    df1 = pd.get_dummies(df, columns = ['GarageType'])

    return df1

# Write your code here:
