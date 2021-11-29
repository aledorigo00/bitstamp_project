import argparse #imported argparse module
from datetime import time #imported time module
from datetime import datetime, timezone
from datetime import date
from datetime import timedelta
import matplotlib.pyplot as plt

#import modules to fetch information from a public API 
from bitstamp import get_time_series_oneday
from bitstamp import get_time_series_30min
from bitstamp import get_time_series_3hours


#Here we add the arguments that the users can input, namely crypto currency, 
#fiat currency and the optional argument date
parser = argparse.ArgumentParser()
parser.add_argument("crypto", help="Type crypto ticker (btc, eth)")
parser.add_argument("fiat", help="Type fiat ticker (eur, usd)")
parser.add_argument('-d',"--date", help="Type date dd/mm/yyyy")
args = parser.parse_args()




#check if the optional argument date is flagged or not
if args.date is not None:
	
	#split the input string into year, month and day
	day=int(args.date.split('/')[0])
	month=int(args.date.split('/')[1])
	year=int(args.date.split('/')[2])

	#create a date from inputs to check the length of the search period
	input_date = date( year, month, day)
	print(input_date)
	#create a datetime from the data entered by the user and convert to 
	#the Unix timestamp format required by the API
	dt = datetime( year, month, day, 00, 00, 00, tzinfo=timezone.utc )
	input_timestamp = int( dt.timestamp() )
	print(input_timestamp)

	'''
	gather today's date and calculate the date of one week ago for 
	choosing the right frequence of datapoint:
	- if time span is one day, datapoint every 30 minutes
	- if time span is within one week, datapoint every 3 hours
	-if timestamp is over one week, datapoint every day
	'''
	today = date.today()
	week_ago = today - timedelta(days=7)

	if input_date == today:
		
		#execute the function
		dates,values = get_time_series_30min(input_timestamp,'btceur')
			
		plt.plot(dates,values)
		plt.title('Graph')
		plt.xlabel('Dates')
		plt.ylabel('Values')
		plt.show()

	elif input_date >= week_ago:

		#execute the function
		dates,values = get_time_series_3hours(input_timestamp,'btceur')
			
		plt.plot(dates,values)
		plt.title('Graph')
		plt.xlabel('Dates')
		plt.ylabel('Values')
		plt.show()

	else:

		#execute the function
		dates,values = get_time_series_oneday(input_timestamp,'btceur')
			
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
