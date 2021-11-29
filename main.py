#imported needed modules
import argparse 
from datetime import datetime, timezone 
from datetime import date
from datetime import timedelta

#import modules from bitstapm.py to fetch information from a public API 
from bitstamp import get_price
from bitstamp import get_time_series_30min
from bitstamp import get_time_series_4hours
from bitstamp import get_time_series_12hours
from bitstamp import get_time_series_oneday

#import modules from graph.py
from graph import plot_graph


#Here we add the arguments that the users can input, namely crypto currency, 
#fiat currency and the optional argument date
parser = argparse.ArgumentParser()
parser.add_argument("crypto", help="Type crypto ticker (btc, eth)")
parser.add_argument("fiat", help="Type fiat ticker (eur, usd)")
parser.add_argument('-d',"--date", help="Type date dd/mm/yyyy")
args = parser.parse_args()

#create the currency pair from user inputs
currency_pair=args.crypto+args.fiat


#check if the optional argument date is flagged or not
if args.date is not None:
	
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
		dates,values = get_time_series_30min(input_timestamp, currency_pair)
		
		#Plot the graph	
		plot_graph(dates, values)

	elif input_date >= two_weeks_ago:

		#execute the function
		dates,values = get_time_series_4hours(input_timestamp, currency_pair)
			
		#Plot the graph	
		plot_graph(dates, values)

	elif input_date >= one_month_ago:

		#execute the function
		dates,values = get_time_series_12hours(input_timestamp, currency_pair)
			
		#Plot the graph	
		plot_graph(dates, values)

	else:

		#execute the function
		dates,values = get_time_series_oneday(input_timestamp, currency_pair)
			
		#Plot the graph	
		plot_graph(dates, values)

else:

	print(get_price(currency_pair))