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


def get_time_series_30min(start, currency):
    '''
    This functions returns the time series of a crypto/fiat currency pair
    prices, taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)
    '''
    time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
    r = requests.get(time_series_URL, params={'start':start, 'step':1800, 'limit':1000})
    total = json.loads(r.text)
    data=total['data']
    ohlc=data['ohlc']
    
    dates = []
    values = []
    for point in ohlc:
        dates.append(datetime.fromtimestamp(int(point['timestamp'])))
        values.append(float(point['close']))
    return dates, values


def get_time_series_3hours(start, currency):
    '''
    This functions returns the time series of a crypto/fiat currency pair
    prices, taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)
    '''
    time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
    r = requests.get(time_series_URL, params={'start':start, 'step':10800, 'limit':1000})
    total = json.loads(r.text)
    data=total['data']
    ohlc=data['ohlc']
    
    dates = []
    values = []
    for point in ohlc:
        dates.append(datetime.fromtimestamp(int(point['timestamp'])))
        values.append(float(point['close']))
    return dates, values


def get_time_series_oneday(start, currency):
    '''
    This functions returns the time series of a crypto/fiat currency pair
    prices, taking as input two parameters: 
        - start: the timestamp that indicates the beginning of the searching period
        - currency: the currency pair to be retreived (e.g. btceur, ethusd)
    '''
    time_series_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+currency+'/'
    r = requests.get(time_series_URL, params={'start':start, 'step':86400, 'limit':1000})
    total = json.loads(r.text)
    data=total['data']
    ohlc=data['ohlc']
    
    dates = []
    values = []
    for point in ohlc:
        dates.append(datetime.fromtimestamp(int(point['timestamp'])))
        values.append(float(point['close']))
    
    return dates, values

