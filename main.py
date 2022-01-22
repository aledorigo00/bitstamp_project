'''this module is the one which the user must execute in order
    to use the software. It manages all the functioning of our program
'''
import argparse
from datetime import datetime, timezone, date, timedelta
import sys

# import modules from bitstamp.py to fetch information from a public API
from bitstamp import get_price, get_step_30min, get_step_4hours
from bitstamp import get_step_12hours, get_step_oneday, get_step_3days

# import modules from graph.py
from graph import plot_candlestick_graph

# import modules from csv.py
from write_csv import write_csv

# import the classes for each input
from inputs import inputCrypto, inputFiat, inputDate

# Here we add the arguments that the users can input, namely crypto currency,
# fiat currency and the optional argument date
parser = argparse.ArgumentParser()
parser.add_argument(
    "crypto", help="Type crypto ticker in lower case (btc, eth, xrp)")
parser.add_argument("fiat", help="Type fiat ticker in lower case (eur, usd)")
parser.add_argument(
    '-d',
    "--date",
    help="Type starting date of the search period in this format dd/mm/yyyy")
parser.add_argument('-c', "--csv", action="store_true",
                    help="Flag to save the result in csv format")
args = parser.parse_args()

# create the objects of inputs with the respective class
crypto_obj = inputCrypto(args.crypto)
fiat_obj = inputFiat(args.fiat)

# check the validity of the inputs with the class method.
# if they're valid, we create the currency pair from them,
# otherwise we print an error and exit the program
if crypto_obj.valid() and fiat_obj.valid():
    currency_pair = crypto_obj.crypto + fiat_obj.fiat
else:
    print('The argument provided are not in our database')
    # retrieve the valid values
    print('- for crypto you can use', inputCrypto.cryptos)
    # retrieve the valid values
    print('- for fiat you can use', inputFiat.fiats)
    sys.exit()


# check if the optional argument date is empty or not
if args.date is not None:

    # create the date object from its class
    date_obj = inputDate(args.date)

    # check the validity of the input date by using the class method.
    # if it is valid, we proceed with the split, otherwise
    # we print an error and exit the program
    if not date_obj.valid():
        print('The data provided is not in the correct format.')
        print('The correct format is dd/mm/yyyy.')
        sys.exit()

    # split the input string into year, month and day
    year, month, day = date_obj.split_date()

    # create a date from inputs to check the length of the search period
    input_date = date(year, month, day)

    # create a datetime from the data entered by the user and convert to
    # the Unix timestamp format required by the API
    dt = datetime(year, month, day, 00, 00, 00, tzinfo=timezone.utc)
    input_timestamp = int(dt.timestamp())

    # gather today's date and calculate the dates of some key points
    # in past time to choose the frequence of datapoints in order to
    # always obrain a readable graph:
    # - if time span is within 4 days, datapoint every 30 minutes
    # - if time span is within 2 weeks, datapoint every 4 hours
    # - if time span is within 2 months, datapoint every 12 hours
    # - if time span is within 6 months, datapoint every one day
    # - if time span is over 6 months, datapoint every 3 days
    today = date.today()
    four_days_ago = today - timedelta(days=4)
    two_weeks_ago = today - timedelta(days=14)
    two_month_ago = today - timedelta(days=62)
    six_month_ago = today - timedelta(days=183)
    one_year_ago = today - timedelta(days=365)

    # check corner inputs to guarantee perfect funcioning of the program
    if input_date < one_year_ago:
        print('Sorry, the date you entered is too far.')
        print('You can choose a starting date up to one year from now.')
        sys.exit()
    elif input_date > today:
        print('Sorry, the date you entered is beyond today.')
        print('Of course, you cannot choose a starting date which is '
              'beyond today.')
        sys.exit()

    # this section compares the date entered by the user with the key
    # past points defined before and executes the time-related function
    if input_date >= four_days_ago:
        # execute the function
        dates, openings, closings, max, min = get_step_30min(
            input_timestamp, currency_pair)

        if args.csv:
            # create a csv file and write it on the folder
            write_csv(currency_pair, input_date, today, dates, closings)
        else:
            # set the right candles width and plot the graph
            width = 0.015
            plot_candlestick_graph(currency_pair, dates,
                                   openings, closings, max, min, width)

    elif input_date >= two_weeks_ago:

        # execute the function
        dates, openings, closings, max, min = get_step_4hours(
            input_timestamp, currency_pair)

        if args.csv:
            # create a csv file and write it on the folder
            write_csv(currency_pair, input_date, today, dates, closings)
        else:
            # set the right candles width and plot the graph
            width = 0.1
            plot_candlestick_graph(currency_pair, dates,
                                   openings, closings, max, min, width)

    elif input_date >= two_month_ago:

        # execute the function
        dates, openings, closings, max, min = get_step_12hours(
            input_timestamp, currency_pair)

        if args.csv:
            # create a csv file and write it on the folder
            write_csv(currency_pair, input_date, today, dates, closings)
        else:
            # set the right candles width and plot the graph
            width = 0.3
            plot_candlestick_graph(currency_pair, dates,
                                   openings, closings, max, min, width)

    elif input_date >= six_month_ago:

        # execute the function
        dates, openings, closings, max, min = get_step_oneday(
            input_timestamp, currency_pair)

        if args.csv:
            # create a csv file and write it on the folder
            write_csv(currency_pair, input_date, today, dates, closings)
        else:
            # set the right candles width and plot the graph
            width = 0.6
            plot_candlestick_graph(currency_pair, dates,
                                   openings, closings, max, min, width)

    else:

        # execute the function
        dates, openings, closings, max, min = get_step_3days(
            input_timestamp, currency_pair)

        if args.csv:
            # create a csv file and write it on the folder
            write_csv(currency_pair, input_date, today, dates, closings)
        else:
            # set the right candles width and plot the graph
            width = 2
            plot_candlestick_graph(currency_pair, dates,
                                   openings, closings, max, min, width)

else:
    # if none of the above, just print the current price
    print(get_price(currency_pair))
