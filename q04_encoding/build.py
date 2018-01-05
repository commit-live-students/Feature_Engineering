# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    df = dataset[['LotShape', 'GarageType']]
    le = LabelEncoder()
    df['LotShape'] = le.fit_transform(df['LotShape'])
    return pd.concat([dataset, pd.get_dummies(dataset['GarageType'])],axis=1)
