# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder, LabelBinarizer
from matplotlib import pyplot as plt
import seaborn as sns

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Write your code here:

def encoding(dataset):
    data = dataset.copy()
    labelencoder = LabelEncoder()
    data.LotShape = labelencoder.fit_transform(data.LotShape)
    data.GarageType = data.GarageType.fillna('0')
    lb_bin = LabelBinarizer()
    lb_results = lb_bin.fit_transform(data.GarageType)
    data = data.join(pd.DataFrame(lb_results, columns=lb_bin.classes_))
    data.drop(['GarageType'],axis = 1, inplace=True)
    return data


