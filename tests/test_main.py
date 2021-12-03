import unittest
import sys
import os

# add parent folder to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bitstamp import get_time_series_30min
from bitstamp import get_time_series_4hours
from bitstamp import get_time_series_12hours
from bitstamp import get_time_series_oneday


class TestTimeSeries30min(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, highs, lows = get_time_series_30min(1638057600, 'btceur')
        self.assertTrue((len(dates)==len(openings)==len(closings)==len(highs)==len(lows))!=0)

    # wrong values
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(get_time_series_30min("1638057600", 'btceur'), None)
        self.assertEqual(get_time_series_30min(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_time_series_30min("", ""), None)


class TestTimeSeries4hours(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, highs, lows = get_time_series_4hours(1638057600, 'btceur')
        self.assertTrue((len(dates)==len(openings)==len(closings)==len(highs)==len(lows))!=0)

    # wrong values
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(get_time_series_4hours("1638057600", 'btceur'), None)
        self.assertEqual(get_time_series_4hours(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_time_series_4hours("", ""), None)


class TestTimeSeries12hours(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, highs, lows = get_time_series_12hours(1638057600, 'btceur')
        self.assertTrue((len(dates)==len(openings)==len(closings)==len(highs)==len(lows))!=0)

    # wrong values
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(get_time_series_12hours("1638057600", 'btceur'), None)
        self.assertEqual(get_time_series_12hours(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_time_series_12hours("", ""), None)


class TestTimeSeriesOneday(unittest.TestCase):

    # valid values
    def test_valid_values(self):
        dates, openings, closings, highs, lows = get_time_series_oneday(1638057600, 'btceur')
        self.assertTrue((len(dates)==len(openings)==len(closings)==len(highs)==len(lows))!=0)

    # wrong values
    def test_wrong_values(self):
        # you should input wrong data
        self.assertEqual(get_time_series_oneday("1638057600", 'btceur'), None)
        self.assertEqual(get_time_series_oneday(0, 0), None)

    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(get_time_series_oneday("", ""), None)


if __name__ == '__main__':
    
    # basic test
    #unittest.main()

    # with more details
    unittest.main(verbosity=2)