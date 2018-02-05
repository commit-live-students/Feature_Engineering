# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import outlier_removal
from inspect import getargspec

ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
without_out = outlier_removal(housing_data)

class TestOutlier_removal(TestCase):
    def test_outlier_removal_args(self):
        # Input parameters tests
        args = getargspec(outlier_removal)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_outlier_removal_default(self):
        args = getargspec(outlier_removal)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
    def test_dataframe(self):
        self.assertIsInstance(without_out, pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(without_out)))

        # Return value tests
    def test_return_shape(self):
        self.assertEqual(without_out.shape, (1302, 5), "Return value shape does not match expected value")
