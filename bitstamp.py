import requests
import json


bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'

def get_price(currency=pair):
    r = requests.get(bitstamp_URL % currency)
    price = float(json.loads(r.text)['last'])
    return price


def get_info(currency=pair):
    info = {}
    r = requests.get(bitstamp_URL % currency)
    info[last_price] = float(json.loads(r.text)['last'])
    info[min24hours] = float(json.loads(r.text)['low'])
    info[max24hours] = float(json.loads(r.text)['high'])
    info[volume] = float(json.loads(r.text)['high'])
    return info


def get_time_series(s=start, e=end, currency=pair):
    bitstamp_URL = 'https://www.bitstamp.net/api/v2/ohlc/'+pair+'/'
    r = requests.get(bitstamp_URL, params={'start':start, 'end':end})
    timeserie = json.load(r.text)
    return timeserie