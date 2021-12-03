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
from bitstamp import get_time_series_3days

#import modules from graph.py
from graph import plot_graph_30min
from graph import plot_graph_4hours 
from graph import plot_graph_12hours 
from graph import plot_graph_oneday
from graph import plot_graph_3days

#import modules from csv.py
from write_csv import write_csv

#import the classes for each input
from inputs import inputCrypto
from inputs import inputFiat
from inputs import inputDate

#Here we add the arguments that the users can input, namely crypto currency, 
#fiat currency and the optional argument date
parser = argparse.ArgumentParser()
parser.add_argument("crypto", help="Type crypto ticker in lower case (btc, eth, xrp)")
parser.add_argument("fiat", help="Type fiat ticker in lower case (eur, usd)")
parser.add_argument('-d',"--date", help="Type starting date of the search period in this format dd/mm/yyyy")
parser.add_argument('-c',"--csv", action="store_true", help="Flag to save the result in csv format")
args = parser.parse_args()

#create the objects of inputs with the respective class
crypto_obj=inputCrypto(args.crypto)
fiat_obj=inputFiat(args.fiat)

''' check the validity of the inputs with the class method. 
	if they're valid, we create the currency pair from them, 
	otherwise we print an error and exit the program'''
if crypto_obj.valid() and fiat_obj.valid():
	currency_pair=crypto_obj.crypto + fiat_obj.fiat
else:
	print('The argument provided are not in our database')
	print('- for crypto you can use', inputCrypto.cryptos) #retrieve the valid values
	print('- for fiat you can use', inputFiat.fiats) #retrieve the valid values
	sys.exit()


#check if the optional argument date is empty or not
if args.date is not None:
	
	#create the date object from its class
	date_obj=inputDate(args.date)

	''' check the validity of the input date by using the class method.
		if it is valid, we proceed with the split, otherwise 
		we print an error and exit the program'''
	if not date_obj.valid():
		print('The data provided is not in the correct format.')
		print('The correct format is dd/mm/yyyy.')
		sys.exit()

	#split the input string into year, month and day
	year, month, day=date_obj.split_date()

	#create a date from inputs to check the length of the search period
	input_date = date(year, month, day)

	#create a datetime from the data entered by the user and convert to 
	#the Unix timestamp format required by the API
	dt = datetime( year, month, day, 00, 00, 00, tzinfo=timezone.utc )
	input_timestamp = int( dt.timestamp() )
	
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
	two_month_ago = today - timedelta(days=62)
	six_month_ago = today - timedelta(days=183)
	one_year_ago = today - timedelta(days=365)

	if input_date<one_year_ago:
		print('Sorry, the date you entered is too far.')
		print('You can choose a starting date up to one year from now.')
		sys.exit()
	elif input_date>today:
		print('Sorry, the date you entered is beyond today.')
		print('Of course, you cannot choose a starting date which is beyond today.')
		sys.exit()

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

	elif input_date >= two_month_ago:

		#execute the function
		dates, openings, closings, highs, lows = get_time_series_12hours(input_timestamp, currency_pair)
			
		if args.csv:
			#create a csv file and write it on the folder
			write_csv(currency_pair, input_date, today, dates, closings)
		else:
			#Plot the graph	
			plot_graph_12hours(currency_pair, dates, openings, closings, highs, lows)

	elif input_date >= six_month_ago:

		#execute the function
		dates, openings, closings, highs, lows = get_time_series_oneday(input_timestamp, currency_pair)
			
		if args.csv:
			#create a csv file and write it on the folder
			write_csv(currency_pair, input_date, today, dates, closings)
		else:
			#Plot the graph	
			plot_graph_oneday(currency_pair, dates, openings, closings, highs, lows)

	else:

		#execute the function
		dates, openings, closings, highs, lows = get_time_series_3days(input_timestamp, currency_pair)
			
		if args.csv:
			#create a csv file and write it on the folder
			write_csv(currency_pair, input_date, today, dates, closings)
		else:
			#Plot the graph	
			plot_graph_3days(currency_pair, dates, openings, closings, highs, lows)

else:

	print(get_price(currency_pair))