# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def encoding(data):

    lablel_encoder = LabelEncoder()
    label_binarizer = LabelBinarizer()
    data['LotShape'] = lablel_encoder.fit_transform(data['GarageType'])
    #x = label_binarizer.fit_transform([])
    data = pd.get_dummies(data, columns=["LotShape"])

    return data
