import argparse #imported argparse module
import time #imported time module
from datetime import datetime, timezone, date, timedelta
import matplotlib.pyplot as plt

#import modules to fetch information from a public API 
from bitstamp import get_price 
from bitstamp import get_time_series_oneday


#Here we add the arguments that the users can input, namely crypto currency, 
#fiat currency and the optional argument date
parser = argparse.ArgumentParser()
parser.add_argument("crypto", help="Type crypto ticker (btc, eth)")
parser.add_argument("fiat", help="Type fiat ticker (eur, usd)")
parser.add_argument('-d',"--date", help="Type date dd/mm/yyyy")
args = parser.parse_args()


#check if the optional argument date is flagged or not
if args.date is not None:
	today = date.today()
	week_ago = today - date.timedelta(days=7)
	

	if args.date == today:
		#split the input string into year, month and day
		day=int(args.date.split('/')[0])
		month=int(args.date.split('/')[1])
		year=int(args.date.split('/')[2])

		#create a datetime from the data entered by the user and convert to 
		#the Unix timestamp format required by the API
		dt = datetime( year, month, day, 00, 00, 00, tzinfo=timezone.utc )
		timestamp = int( dt.timestamp() )

		#execute the function
		dates,values = get_time_series_oneday(timestamp,'btceur')
			
		plt.plot(dates,values)
		plt.title('Graph')
		plt.xlabel('Dates')
		plt.ylabel('Values')
		plt.show()

	else:
		day=int(args.date.split('/')[0])
		month=int(args.date.split('/')[1])
		year=int(args.date.split('/')[2])

		#create a datetime from the data entered by the user and convert to 
		#the Unix timestamp format required by the API
		dt = datetime( year, month, day, 00, 00, 00, tzinfo=timezone.utc )
		timestamp = int( dt.timestamp() )

		#execute the function
		dates,values = get_time_series_oneday(timestamp,'btceur')
			
		plt.plot(dates,values)
		plt.title('Graph')
		plt.xlabel('Dates')
		plt.ylabel('Values')
		plt.show()


else:
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




	print(to_print) #print the result
