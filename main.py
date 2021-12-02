#imported needed modules
import argparse 
from datetime import datetime, timezone 
from datetime import date
from datetime import timedelta
import pandas as pd
import sys

#import modules from bitstamp.py to fetch information from a public API 
from bitstamp import get_price
from bitstamp import get_time_series_30min
from bitstamp import get_time_series_4hours
from bitstamp import get_time_series_12hours
from bitstamp import get_time_series_oneday

#import modules from graph.py
from graph import plot_graph_30min
from graph import plot_graph_4hours 
from graph import plot_graph_12hours 
from graph import plot_graph_oneday

#import modules from csv.py
from functions import date_validation

#import modules from csv.py
from write_csv import write_csv


#function that checks for the valid date input
def date_validation(testdate):
    try:
        if testdate != datetime.strptime(testdate, "%d/%m/%Y").strftime("%d/%m/%Y"):
            raise ValueError
        return True
    except ValueError:
        return False

#Here we add the arguments that the users can input, namely crypto currency, 
#fiat currency and the optional argument date
parser = argparse.ArgumentParser()
parser.add_argument("crypto", help="Type crypto ticker (btc, eth)")
parser.add_argument("fiat", help="Type fiat ticker (eur, usd)")
parser.add_argument('-d',"--date", help="Type date dd/mm/yyyy")
parser.add_argument('-c',"--csv", action="store_true", help="Flag to save the result in csv format")
args = parser.parse_args()

cryptos=['btc', 'eth', 'xrp']
fiats=['eur', 'usd']

#check the validity of the inputs and create the currency pair from them
if args.crypto in cryptos and args.fiat in fiats:
	currency_pair=args.crypto+args.fiat
else:
	print('the arguments provided are not in our database')
	print('- for crypto you can use', cryptos)
	print('- for fiat you can use', fiats)
	sys.exit()


#check if the optional argument date is flagged or not
if args.date is not None:
	
	if validate(args.date):
		currency_pair=args.crypto+args.fiat
	else:
		print('the data provided is not in the correct format')
		print('The correct format is dd/mm/yyyy')
		sys.exit()

	#split the input string into year, month and day
	day=int(args.date.split('/')[0])
	month=int(args.date.split('/')[1])
	year=int(args.date.split('/')[2])

	#create a date from inputs to check the length of the search period
	input_date = date( year, month, day)

	#create a datetime from the data entered by the user and convert to 
	#the Unix timestamp format required by the API
	dt = datetime( year, month, day, 00, 00, 00, tzinfo=timezone.utc )
	input_timestamp = int( dt.timestamp() )
	print(input_timestamp)
	
	'''
	gather today's date and calculate the date of one week ago for 
	choosing the right frequence of datapoint:
	- if time span is within four days, datapoint every 30 minutes
	- if time span is within two weeks, datapoint every 4 hours
	- if time span is within one month, datapoint every 12 hours	
	- if timestamp is over one month, datapoint every day
	'''
	today = date.today()
	four_days_ago = today - timedelta(days=4)
	two_weeks_ago = today - timedelta(days=14)
	one_month_ago = today - timedelta(days=30)

	if input_date >= four_days_ago:
		#execute the function
		dates, openings, closings, highs, lows = get_time_series_30min(input_timestamp, currency_pair)
		
		if args.csv:
			#create a csv file and write it on the folder
			write_csv(currency_pair, input_date, today, dates, closings)
		else:
			#Plot the graph	
			plot_graph_30min(currency_pair, dates, openings, closings, highs, lows)

	elif input_date >= two_weeks_ago:

		#execute the function
		dates, openings, closings, highs, lows = get_time_series_4hours(input_timestamp, currency_pair)
			
		if args.csv:
			#create a csv file and write it on the folder
			write_csv(currency_pair, input_date, today, dates, closings)
		else:
			#Plot the graph	
			plot_graph_4hours(currency_pair, dates, openings, closings, highs, lows)

	elif input_date >= one_month_ago:

		#execute the function
		dates, openings, closings, highs, lows = get_time_series_12hours(input_timestamp, currency_pair)
			
		if args.csv:
			#create a csv file and write it on the folder
			write_csv(currency_pair, input_date, today, dates, closings)
		else:
			#Plot the graph	
			plot_graph_12hours(currency_pair, dates, openings, closings, highs, lows)

	else:

		#execute the function
		dates, openings, closings, highs, lows = get_time_series_oneday(input_timestamp, currency_pair)
			
		if args.csv:
			#create a csv file and write it on the folder
			write_csv(currency_pair, input_date, today, dates, closings)
		else:
			#Plot the graph	
			plot_graph_oneday(currency_pair, dates, openings, closings, highs, lows)

else:

	print(get_price(currency_pair))