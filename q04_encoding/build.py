# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    LE = LabelEncoder()
    housing_data['LotShape'] = LE.fit_transform(housing_data['LotShape'])
    df =  pd.get_dummies(housing_data[['GarageType']])
    df = housing_data.join(df)
    return df
