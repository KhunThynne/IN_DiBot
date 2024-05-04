"""
Trading-Technical-Indicators (tti) python library

File name: test_indicator_performance.py
    tti.indicators package, _performance.py module unit tests.
"""

import unittest
import tti.indicators
from test_indicators_common import TestIndicatorsCommon

import pandas as pd
import re


class TestPerformance(unittest.TestCase, TestIndicatorsCommon):

    indicator = tti.indicators.Performance

    ti_data_rows = [0, 1]

    df = pd.read_csv('./data/sample_data.csv', parse_dates=True, index_col=0)

    indicator_input_arguments = {'mode': 'LONG', 'target': 0.05}

    indicator_other_input_arguments = [{'mode': 'SHORT', 'target': -0.05}]

    indicator_minimum_required_data = 1

    mandatory_arguments_missing_cases = []

    required_input_data_columns = ['close']

    arguments_wrong_type = [
        {'input_data': 'No_DataFrame'},
        {'input_data': df, 'target': 'no_numeric'},
        {'input_data': df, 'mode': 1},
        {'input_data': df, 'fill_missing_values': 'no_boolean'}
    ]

    arguments_wrong_value = [
        {'input_data': df, 'mode': 'not_valid', 'target': 0.1},
        {'input_data': df, 'mode': 'LONG', 'target': -0.1},
        {'input_data': df, 'mode': 'SHORT', 'target': 0.1}
    ]

    graph_file_name = '_'.join(
        x.lower() for x in re.findall('[A-Z][^A-Z]*', str(
            indicator).split('.')[-1][:-2]))

    graph_file_name = './figures/test_' + graph_file_name + '.png'

    indicator_test_data_file_name = '_'.join(
        x.lower() for x in re.findall('[A-Z][^A-Z]*', str(
            indicator).split('.')[-1][:-2]))

    indicator_test_data_file_name = \
        './data/test_' + indicator_test_data_file_name + '_on_sample_data.csv'

    assertRaises = unittest.TestCase.assertRaises
    assertEqual = unittest.TestCase.assertEqual
    assertIn = unittest.TestCase.assertIn
    subTest = unittest.TestCase.subTest


if __name__ == '__main__':
    unittest.main()
