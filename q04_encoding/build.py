# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')


# Write your code here:
def encoding(ny_housing):
    housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
    ny_housing['GarageType'].fillna('Not Available', inplace = True)

    lbl = LabelEncoder()
    ny_housing['LotShape'] = lbl.fit_transform(ny_housing['LotShape'])
    return ny_housing

encoding(ny_housing)





