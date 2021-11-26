from bitstamp import get_price #import modules to fetch information from a public API 
import argparse #imported argparse module

#Here we add two arguments that the users can input, namely crypto and fiat
parser = argparse.ArgumentParser()
parser.add_argument("crypto", help="Type crypto ticker (btc, eth)")
parser.add_argument("fiat", help="Type fiat ticker (eur, usd)")
parser.add_argument('-d',"--date", help="Type date dd/mm/yyyy")
args = parser.parse_args()


#The case in which the fiat selection is eur
if args.fiat == 'eur':

	#if the typed coin is btc, then return the price of btc in euro.
	
	if args.crypto == "btc":
		to_print = get_price("btceur")

	#Instead if the typed coin is eth, then return the price of eth in euro.
	elif args.crypto == "eth":
		to_print = get_price("etheur")


#The case in which the fiat selection is usd		
else:

	#if the typed coin is btc, then return the price of btc in dollars.
	if args.crypto == "btc":
		to_print = get_price("btcusd")

	#Instead if the typed coin is eth, then return the price of eth in euro.
	elif args.crypto == "eth":
		to_print = get_price("ethusd")

print(to_print)
