'''This module contains some classes which are needed to manage
    input arguments and to check their validity
'''
from datetime import datetime, date


class inputCrypto():

    cryptos = ['btc', 'eth', 'xrp']

    def __init__(self, crypto):
        self.crypto = crypto

    def valid(self):
        if self.crypto in self.cryptos:
            return True
        else:
            return False


class inputFiat():

    fiats = ['eur', 'usd']

    def __init__(self, fiat):
        self.fiat = fiat

    def valid(self):
        if self.fiat in self.fiats:
            return True
        else:
            return False


class inputDate():

    def __init__(self, date):
        self.date = date

    # function that checks for the valid date input
    def valid(self):
        try:
            if self.date != datetime.strptime(
                                self.date, "%d/%m/%Y").strftime("%d/%m/%Y"):
                raise ValueError
            return True
        except ValueError:
            return False

    def split_date(self):
        # split the input string into year, month and day
        self.day = int(self.date.split('/')[0])
        self.month = int(self.date.split('/')[1])
        self.year = int(self.date.split('/')[2])

        return self.year, self.month, self.day
