# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    label = LabelEncoder()
    dummies = pd.get_dummies(dataset.GarageType)
    dataset.drop('GarageType',axis=1,inplace=True)
    frames = [dummies, dataset]
    data_frame = pd.concat(frames,axis=1)
    data_frame['LotShape_Label'] = label.fit_transform(housing_data['LotShape'])
    
    return data_frame
    






