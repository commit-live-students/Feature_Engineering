from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')
def skewness_log(data):
#     plt.subplot(2,2,1)
#     sns.distplot(data['SalePrice']);
#     plt.subplot(2,2,2)
#     sns.distplot(data['GrLivArea'])

#     print(skew(data['SalePrice']),skew(data['GrLivArea']))
# #     plt.show()

    df =data.copy()
    df['SalePrice'] = np.log(df['SalePrice'])
    df['GrLivArea'] = np.log(df['GrLivArea'])
#     plt.subplot(2,2,3)
#     sns.distplot(df['SalePrice']);
#     plt.subplot(2,2,4)
#     sns.distplot(df['GrLivArea'])
#     plt.show()

#     print(skew(df['SalePrice']),skew(df['GrLivArea']))





    return skew(df['GrLivArea']),skew(df['SalePrice'])

# Write code here:
