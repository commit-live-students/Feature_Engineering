# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(data):
    data_copy = data.copy()
    le = LabelEncoder()
    data_copy.LotShape = le.fit_transform(data_copy.LotShape)
    # We can actually drop the GarageType column as it is getting encoded,
    # but test case requires it
    df1 = pd.get_dummies(data_copy.GarageType, prefix="GarageType", prefix_sep="_")
    return pd.concat([data_copy, df1],axis=1)
