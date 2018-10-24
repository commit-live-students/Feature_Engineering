# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    #label encoding
    le = LabelEncoder()
    dataset['LotShape'] = le.fit_transform(dataset['LotShape'])

    #Binary encoding
    Bin = pd.get_dummies(dataset['GarageType'])

    return pd.concat([dataset,Bin],axis=1)
