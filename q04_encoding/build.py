# Default imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
def encoding(df):
    cat_col = df.select_dtypes(include=['category','object']).columns
    le = LabelEncoder()
    df[cat_col[0]] = le.fit_transform(df[cat_col[0]])
    df=pd.concat([df, pd.get_dummies(df['GarageType'])], axis=1);
    return df
