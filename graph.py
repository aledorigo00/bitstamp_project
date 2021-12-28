'''this module is used to contain the functions needed to plot
    the data retreived from the API
'''
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates


def plot_candlestick_graph(
           currency, dates, openings, closings, highs, lows, width):
    '''this function is supposed to plot the graph representing the trend
        of a currency pair. It uses candlestick type of graph which best fits
        our purpose of analyzing a financial instrument
    '''

    # create a dataframe and assign each vector to a column
    ohlc_data = pd.DataFrame()
    ohlc_data["dates"] = dates
    ohlc_data["openings"] = openings
    ohlc_data["highs"] = highs
    ohlc_data["lows"] = lows
    ohlc_data["closings"] = closings

    plt.style.use('ggplot')

    # Adjusting formats for plotting
    ohlc_data['dates'] = ohlc_data['dates'].apply(mpl_dates.date2num)
    data = ohlc_data.astype(float)

    # Creating Subplots
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc_data.values, width=width,
                     colorup='green', colordown='red', alpha=0.8)

    # Inserting legend image at the top-right of the graph
    im = plt.imread('candlestick.png')
    newax = fig.add_axes([0.8, 0.8, 0.2, 0.2], anchor='SE', zorder=0)
    newax.imshow(im)
    newax.axis('off')

    # create the graph title with the parameter passed
    crypto = currency[:3]
    fiat = currency[3:]
    fig.suptitle('Candlestick Chart for: ' +
                 crypto.upper() + " " + fiat.upper())

    # Setting labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Price in ' + fiat.upper())

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    # set graph full screen
    plt.get_current_fig_manager().full_screen_toggle()
    plt.show()
