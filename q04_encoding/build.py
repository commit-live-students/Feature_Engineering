# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OneHotEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    data = housing_data.copy()
    encoder = LabelEncoder()
    binary = LabelBinarizer()
    on_hot = OneHotEncoder()
    data['LotShape'] = encoder.fit_transform(data['LotShape'])
    datasets_dummies = pd.get_dummies(data['GarageType'])
    d_df = pd.concat([data, datasets_dummies], axis=1)
    return d_df.shape


print encoding(housing_data)# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OneHotEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(housing_data):
    data = housing_data.copy()
    encoder = LabelEncoder()
    binary = LabelBinarizer()
    on_hot = OneHotEncoder()
    data['LotShape'] = encoder.fit_transform(data['LotShape'])
    datasets_dummies = pd.get_dummies(data['GarageType'])
    d_df = pd.concat([data, datasets_dummies], axis=1)
    return d_df


print encoding(housing_data)
