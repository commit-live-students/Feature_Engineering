# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
import numpy as np
def encoding(df):
    le = LabelEncoder()
    df.loc[:,'LotShape'] = le.fit_transform(df['LotShape'])
    df.loc[:,'GarageType'] = np.where(df['GarageType'].isnull(), 0, 1)

    ls = pd.get_dummies(housing_data['LotShape'], prefix='Lot')
    gt = pd.get_dummies(housing_data['GarageType'], prefix='GarageType')

    frames = [housing_data, ls, gt]
    f = pd.concat(frames, axis=1)

    # s = pd.get_dummies(housing_data, columns=['LotShape', 'GarageType'], drop_first=False)
    return f

# d = encoding(housing_data)
# print type(d)
# print d.shape
