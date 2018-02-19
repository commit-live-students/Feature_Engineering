# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder,LabelBinarizer,OneHotEncoder    

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(df):
    lablel_encoder = LabelEncoder()
    binary_encoder = LabelBinarizer()
    oneh_encoder=OneHotEncoder()
    df['LotShape']=lablel_encoder.fit_transform(df['LotShape'])
    df_dummies=pd.get_dummies(df['GarageType'], sparse=True)
    c_df=pd.concat([df,df_dummies],axis=1)
    return c_df
