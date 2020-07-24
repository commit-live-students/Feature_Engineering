# %load q02_outlier_removal/build.py
# Default imports
import pandas as pd
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns
from scipy import stats
#For some Statistics
from scipy.stats import norm, skew
from sklearn.preprocessing import Imputer
# Data
ny_housing = pd.read_csv('data/train.csv')

# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
housing_data_num = ny_housing[['MasVnrArea', 'GrLivArea', 'SalePrice']]
num_cols=housing_data_num.head(0)
housing_data['GarageType'] = housing_data['GarageType'].fillna(housing_data['GarageType'].mode()[0])
quant_list=[]
# Write your code here:
def outlier_removal(housing_data):
    for i in num_cols:
        quant_list.append([i,housing_data[i].quantile(0.95)])
    for j in quant_list:
        housing_data=housing_data.drop(housing_data[(housing_data[j[0]]>j[1])].index)
    return housing_data
        
    
    
    
outlier_removal(housing_data)
    


