# %load q04_encoding/build.py
# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(df):
    le = LabelEncoder()
    df['LotShape'] = le.fit_transform(df['LotShape'])
    
    df['GarageType']=df['GarageType'].fillna('0')
    label_binarizer=LabelBinarizer()
    lb_results = label_binarizer.fit_transform(df['GarageType'])
   
    df=df.join(pd.DataFrame(lb_results, columns=label_binarizer.classes_))
    df=df.drop(['GarageType'], axis=1)
    return(df)





