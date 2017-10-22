from scipy.stats import skew
import pandas as pd
import numpy as np

data = pd.read_csv('data/train.csv')


# Write code here:
def skewness_log(data):
    Saleprice_data = data['SalePrice']
    livArea_data = data['GrLivArea']
    unskew_saleprice = Saleprice_data.apply(np.log)   # Get the log of the data
    unskew_livarea = livArea_data.apply(np.log)
    skewmeasure = unskew_saleprice.skew()
    skewmeasure2 = unskew_livarea.skew()
    return round(skewmeasure2,5), round(skewmeasure,5)
