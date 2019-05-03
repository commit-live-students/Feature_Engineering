# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


def encoding(housing_data):

    df=housing_data.copy()
    lablel_encoder = LabelEncoder()
    df['Lotshape'] = lablel_encoder.fit_transform(df['LotShape'])
    df1 = pd.get_dummies(df['GarageType'],drop_first=True)
    result = pd.concat([df, df1], axis=1)
    return result
