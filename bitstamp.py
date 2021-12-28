''' API: https://www.bitstamp.net/api/#ohlc_data
    This module uses the aforementioned API to gather data from the bitstamp
    server. It has different function to fit every time period requested by
    the user
'''
import requests
import sys
import json
from datetime import datetime


def get_price(currency):
    ''' This function returns the price of a currency pair at the moment.
        It takes as input the currency pair.
    '''
    bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'
    # check the connection otherwise print an error message and stop the program       
    try:
        r = requests.get(bitstamp_URL % currency)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")
        sys.exit()
    else:
        price = float(json.loads(r.text)['last'])
        return price


def read_ohlc_data(response):
    ''' This function takes as input the http response, dives through the data dictionary
        and builds two vectors, one for dates and one for prices, to be returned
    '''
    total = json.loads(response.text)
    data=total['data']
    ohlc=data['ohlc']
    
    dates = []
    openings = []
    closings = []
    highs = []
    lows = []
    for point in ohlc:
        dates.append(datetime.fromtimestamp(int(point['timestamp'])))
        openings.append(float(point['open']))
        closings.append(float(point['close']))
        highs.append(float(point['high']))
        lows.append(float(point['low']))

    return dates, openings, closings, highs, lows

def get_step_30min(start, currency): 
    ''' This functions returns the price time serie every 30 minutes of a currency pair, 
        taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)
    '''

    if (type(start)!=int or type(currency)!=str):
        return None

    else:
        time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
        # check the connection otherwise print an error message and stop the program       
        try:
            r = requests.get(time_series_URL, params={'start':start, 'step':1800, 'limit':200})
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
            sys.exit()
        else: 
            dates, openings, closings, highs, lows = read_ohlc_data(r)
            return dates, openings, closings, highs, lows

def get_step_4hours(start, currency):
    ''' This functions returns the price time serie every 4 hours of a currency pair, 
        taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)
    '''

    if (type(start)!=int or type(currency)!=str):
        return None

    else:
        time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
        # check the connection otherwise print an error message and stop the program       
        try:
            r = requests.get(time_series_URL, params={'start':start, 'step':14400, 'limit':200})
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
            sys.exit()
        else:
            dates, openings, closings, highs, lows = read_ohlc_data(r)
            return dates, openings, closings, highs, lows


def get_step_12hours(start, currency): 
    ''' This functions returns the price time serie every 12 hours of a currency pair, 
        taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)
    '''

    if (type(start)!=int or type(currency)!=str):
        return None

    else:
        time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
        # check the connection otherwise print an error message and stop the program       
        try:
            r = requests.get(time_series_URL, params={'start':start, 'step':43200, 'limit':200})
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
            sys.exit()
        else:
            dates, openings, closings, highs, lows = read_ohlc_data(r)
            return dates, openings, closings, highs, lows


def get_step_oneday(start, currency):
    ''' This functions returns the price time serie every day of a currency pair, 
        taking as input two parameters:  
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)
    '''

    if (type(start)!=int or type(currency)!=str):
        return None
        
    else:
        time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
        # check the connection otherwise print an error message and stop the program       
        try:
            r = requests.get(time_series_URL, params={'start':start, 'step':86400, 'limit':185})
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
            sys.exit()
        else:
            dates, openings, closings, highs, lows = read_ohlc_data(r)
            return dates, openings, closings, highs, lows


def get_step_3days(start, currency):
    ''' This functions returns the price time serie every day of a currency pair, 
        taking as input two parameters:  
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)
    '''

    if (type(start)!=int or type(currency)!=str):
        return None
        
    else:
        time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
        # check the connection otherwise print an error message and stop the program       
        try:
            r = requests.get(time_series_URL, params={'start':start, 'step':259200, 'limit':185})
        except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
            sys.exit()
        else:
            dates, openings, closings, highs, lows = read_ohlc_data(r)
            return dates, openings, closings, highs, lows