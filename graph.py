import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates



def plot_graph(currency, dates, openings, closings, highs, lows ):
    data = pd.DataFrame() 
    data["dates"]= dates
    data["openings"]= openings
    data["highs"]= highs
    data["lows"]= lows
    data["closings"]= closings


    plt.style.use('ggplot')

    # Extracting Data for plotting
    ohlc = data.loc[:, ['dates', 'openings', 'highs', 'lows', 'closings']]
    ohlc['dates'] = ohlc['dates'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)

    # Creating Subplots
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.015, colorup='green', colordown='red', alpha=0.8)

    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle('Candlestick Chart' + currency)

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    fig.tight_layout()

    plt.show()

'''
    plt.plot(dates,values)
    plt.title('Graph')
    plt.xlabel('Dates')
    plt.ylabel('Values')
    plt.show() '''