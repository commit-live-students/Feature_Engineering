# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
print(housing_data)

# Write your code here:
def encoding(housing_data):
    housing_data=pd.get_dummies(housing_data, drop_first=True)
    return housing_data
    

encoding(housing_data)



