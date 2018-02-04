# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(dataset):
    dataset = dataset.copy()
    #dataset['GarageType']=  LabelEncoder().fit_transform(dataset['GarageType'])
    #dataset=pd.concat([dataset, pd.get_dummies(dataset['LotShape'])], axis=1);
    #dataset= dataset.drop(['LotShape'], axis=1)
    dataset['LotShape']=  LabelEncoder().fit_transform(dataset['LotShape'])
    dataset=pd.concat([dataset, pd.get_dummies(dataset['GarageType'])], axis=1);
    return dataset

#print encoding(housing_data).head()
