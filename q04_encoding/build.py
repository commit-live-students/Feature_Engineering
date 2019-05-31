# %load q04_encoding/build.py
# Default imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, LabelBinarizer

from matplotlib import pyplot as plt
import seaborn as sns

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    df = dataset.copy()
    labelencoder = LabelEncoder()
    df.LotShape = labelencoder.fit_transform(df.LotShape)
    df.GarageType = df.GarageType.fillna('0')
    lb_bin = LabelBinarizer()
    lb_results = lb_bin.fit_transform(df.GarageType)
    df = df.join(pd.DataFrame(lb_results, columns=lb_bin.classes_))
    df.drop(['GarageType'],axis = 1, inplace=True)
    return df

encoding(dataset=housing_data).shape



