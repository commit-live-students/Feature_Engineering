# Default imports
import pandas as pd
from sklearn.preprocessing import Imputer
# Data loading
ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]


# Write your code here:
# Default imports
#import pandas as pd


# Data loading
#ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables along with target variable from the dataset fot the Cleaning and Preprocessing.
#housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

def imputation(df):
    categorical=df.loc[:,['LotShape','GarageType']]
    numeric=df.loc[:,['MasVnrArea','GrLivArea','SalePrice']]
    numericheader=list(numeric)

    imp_mean = Imputer(missing_values = 'NaN', strategy='mean')

    for i in numericheader:
        imp_mean.fit(numeric[[i]])
        numeric[i] = imp_mean.transform(numeric[[i]])
    #print(numeric)

    categorical['LotShape']=categorical.loc[:,'LotShape'].fillna(categorical.loc[:,'LotShape'].mode()[0])
    #print categorical

    categorical['GarageType']=categorical.loc[:,'GarageType'].fillna(categorical.loc[:,'GarageType'].mode()[0])
    #print categorical
    return numeric,categorical
