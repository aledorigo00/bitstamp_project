'''This module is used to perform tests on the key functions of our program,
    namely the ones which communicate with the API and could in some cases
    throw an error.
    To execute use: python3 -m unittest -v -b tests/test_main.py
'''
import unittest
import sys
import os
from bitstamp import get_step_30min, get_step_4hours, get_step_12hours
from bitstamp import get_step_oneday, get_step_3days

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestTimeSeries30min(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, max, min = get_step_30min(
            1638057600, 'btceur')
        self.assertTrue((len(dates) == len(openings) == len(
            closings) == len(max) == len(min)) != 0)

    # wrong values
    def test_wrong_values(self):
        self.assertEqual(get_step_30min("1638057600", 'btceur'), None)
        self.assertEqual(get_step_30min(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_step_30min("", ""), None)


class TestTimeSeries4hours(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, max, min = get_step_4hours(
            1638057600, 'btceur')
        self.assertTrue((len(dates) == len(openings) == len(
            closings) == len(max) == len(min)) != 0)

    # wrong values
    def test_wrong_values(self):
        self.assertEqual(get_step_4hours("1638057600", 'btceur'), None)
        self.assertEqual(get_step_4hours(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_step_4hours("", ""), None)


class TestTimeSeries12hours(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, max, min = get_step_12hours(
            1638057600, 'btceur')
        self.assertTrue((len(dates) == len(openings) == len(
            closings) == len(max) == len(min)) != 0)

    # wrong values
    def test_wrong_values(self):
        self.assertEqual(get_step_12hours("1638057600", 'btceur'), None)
        self.assertEqual(get_step_12hours(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_step_12hours("", ""), None)


class TestTimeSeriesOneday(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, max, min = get_step_oneday(
            1638057600, 'btceur')
        self.assertTrue((len(dates) == len(openings) == len(
            closings) == len(max) == len(min)) != 0)

    # wrong values
    def test_wrong_values(self):
        self.assertEqual(get_step_oneday("1638057600", 'btceur'), None)
        self.assertEqual(get_step_oneday(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_step_oneday("", ""), None)


class TestTimeSeries3days(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, max, min = get_step_3days(
            1638057600, 'btceur')
        self.assertTrue((len(dates) == len(openings) == len(
            closings) == len(max) == len(min)) != 0)

    # wrong values
    def test_wrong_values(self):
        self.assertEqual(get_step_3days("1638057600", 'btceur'), None)
        self.assertEqual(get_step_3days(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_step_3days("", ""), None)


if __name__ == '__main__':

    # test with details
    unittest.main(verbosity=2)
