# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:


def encoding(dataset):
    df = dataset.copy()
    label_encoder = LabelEncoder()
    df['LotShape'] = label_encoder.fit_transform(df['LotShape'])
    return pd.concat(
        [df,pd.get_dummies(df['GarageType'])],
        axis=1
    )
