

import time
from bitstamp import get_price
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("crypto", help="Type crypto ticker (btc, eth)")
parser.add_argument("fiat", help="Type fiat ticker (eur, usd)")
args = parser.parse_args()

if args.fiat == 'eur':
	if args.crypto == "btc":
		to_print = get_price("btceur")
	elif args.crypto == "eth":
		to_print = get_price("etheur")
else:
	if args.crypto == "btc":
		to_print = get_price("btcusd")
	elif args.crypto == "eth":
		to_print = get_price("ethusd")

print(to_print)
'''
timeseries_eur=[]
timeseries_dollar=[]


for n in range(0,10):
	eur=get_price("btceur")
	timeseries_eur.append(eur)
	print("Last bitcoin price in EUR is: {}".format(eur))
	dollar=get_price("btcusd")
	timeseries_dollar.append(dollar)
	print("Last bitcoin price in $ is: {}".format(dollar))
	time.sleep(1)


print(timeseries_dollar)
'''
