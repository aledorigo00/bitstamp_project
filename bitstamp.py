import requests
import json
from datetime import datetime


def get_price(currency):
    '''
    This function returns the price of a crypto/fiar currency pair at the moment.
    It takes as input the currency pair.
    '''
    bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'
    r = requests.get(bitstamp_URL % currency)
    price = float(json.loads(r.text)['last'])
    return price

def read_ohlc_data(response):
    '''This function takes as input the http response, dives through the data dictionary
    and builds two vectors, one for dates and one for prices, to be returned
    '''
    total = json.loads(response.text)
    data=total['data']
    ohlc=data['ohlc']
    
    dates = []
    values = []
    for point in ohlc:
        dates.append(datetime.fromtimestamp(int(point['timestamp'])))
        values.append(float(point['close']))

    return dates, values

def get_time_series_30min(start, currency): 
    '''This functions returns the price time serie every 30 minutes of a currency pair, 
    taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)'''
    time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
    r = requests.get(time_series_URL, params={'start':start, 'step':1800, 'limit':1000})
    dates, values = read_ohlc_data(r)
    return dates, values


def get_time_series_4hours(start, currency):
    '''This functions returns the price time serie every 4 hours of a currency pair, 
    taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)'''
    time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
    r = requests.get(time_series_URL, params={'start':start, 'step':14400, 'limit':1000})
    dates, values = read_ohlc_data(r)
    return dates, values


def get_time_series_12hours(start, currency): 
    '''This functions returns the price time serie every 12 hours of a currency pair, 
    taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)'''
    time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
    r = requests.get(time_series_URL, params={'start':start, 'step':43200, 'limit':1000})
    dates, values = read_ohlc_data(r)
    return dates, values


def get_time_series_oneday(start, currency):
    '''This functions returns the price time serie every day of a currency pair, 
    taking as input two parameters:  
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)'''
    time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
    r = requests.get(time_series_URL, params={'start':start, 'step':86400, 'limit':1000})
    dates, values = read_ohlc_data(r)
    return dates, values

