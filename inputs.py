'''This module contains some classes which are needed to manage
    input arguments and to check their validity
'''
from datetime import datetime, date


class inputCrypto():

    # list of usable cryptocurrencies
    cryptos = ['btc', 'eth', 'xrp', 'ltc', 'bch', 'pax','xlm',
    'link','omg','usdc','aave','bat','uma','knc', 'mkr','zrx',
    'algo','audio','crv','snx','uni','yfi','comp','grt','usdt',
    'eurt','matic','sushi','chz','enj','hbar','alpha','axs',
    'ftt','sand','storj','ada','fet','rgt','skl','cel','slp',
    'sxp','sgb','dydx','ftm','amp','gala','perp']

    # constructor
    def __init__(self, crypto):
        self.crypto = crypto

    # validation of crypto inputs
    def valid(self):
        if self.crypto in self.cryptos:
            return True
        else:
            return False


class inputFiat():

    # list of usable fiat currencies
    fiats = ['eur', 'usd']

    # constructor
    def __init__(self, fiat):
        self.fiat = fiat
    # validation of fiat inputs
    def valid(self):
        if self.fiat in self.fiats:
            return True
        else:
            return False


class inputDate():
    # constructor
    def __init__(self, date):
        self.date = date

    # function that checks for the validity of the input date format
    def valid(self):
        try:
            if self.date != datetime.strptime(
                                self.date, "%d/%m/%Y").strftime("%d/%m/%Y"):
                raise ValueError
            return True
        except ValueError:
            return False

    # function to split the input string into year, month and day
    def split_date(self):
        self.day = int(self.date.split('/')[0])
        self.month = int(self.date.split('/')[1])
        self.year = int(self.date.split('/')[2])

        return self.year, self.month, self.day
