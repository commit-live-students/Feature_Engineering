# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    le = LabelEncoder()
    enc = OneHotEncoder(sparse=False)
    dataset.loc[dataset.loc[:,'GarageType'].isnull(),'GarageType'] = 'Attchd'
    dataset['GarageType'] = le.fit_transform(dataset['GarageType'])
    temp = enc.fit_transform(dataset['GarageType'].reshape(-1,1))
    dataset['LotShape'] = le.fit_transform(dataset['LotShape'])
    ans = dataset.join(pd.DataFrame(temp), how='left')
    return(ans)
