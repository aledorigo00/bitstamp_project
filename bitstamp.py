import requests
import json


def get_price(currency):
    bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'
    r = requests.get(bitstamp_URL % currency)
    price = float(json.loads(r.text)['last'])
    return price