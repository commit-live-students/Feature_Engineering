# Default imports
from scipy.stats import skew
import pandas as pd
import numpy as np

ny_housing = pd.read_csv('data/train.csv')

def skewness_sqrt(data):
#     plt.subplot(2,2,1)
#     sns.distplot(data['SalePrice'])
#     plt.subplot(2,2,2)
#     sns.distplot(data['GrLivArea'])
    data['sk_SalePrice']=data['SalePrice']**0.5
    data['sk_GrLivArea']=data['GrLivArea']**0.5
#     print(skew(data['SalePrice']),skew(data['GrLivArea']))
#     plt.subplot(2,2,3)
#     sns.distplot(data['sk_SalePrice'])
#     plt.subplot(2,2,4)
#     sns.distplot(data['sk_GrLivArea'])
#     plt.show()
#     data['skl_SalePrice']=np.log(data['SalePrice'])
#     data['skl_GrLivArea']=np.log(data['GrLivArea'])
#     print(skew(data['SalePrice']),skew(data['GrLivArea']))
#     plt.subplot(2,2,3)
#     sns.distplot(data['skl_SalePrice'])
#     plt.subplot(2,2,4)
#     sns.distplot(data['skl_GrLivArea'])
#     plt.show()
#     print(skew(data['skl_SalePrice']),skew(data['skl_GrLivArea']))


    return skew(data['sk_GrLivArea']),skew(data['sk_SalePrice'])

# Write your Solution Here:
