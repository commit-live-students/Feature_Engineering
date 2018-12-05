# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    
    #Label Encoding for LotShape.
    label_encoder = LabelEncoder()
    dataset['LotShape_Label'] = label_encoder.fit_transform(dataset['LotShape'])

    #One Hot Encoding for GarageType
    One_Hot_Encoding_Columns = pd.get_dummies(dataset['GarageType'], drop_first=True)
    
    #Concatenating the encoding columns to actual dataframe.
    dataset = pd.concat([dataset, One_Hot_Encoding_Columns],axis=1)
    
    return dataset


#Call to the actual function.
encoding(housing_data)


