import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates




def plot_graph_30min(currency, dates, openings, closings, highs, lows ):
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
    
    # Inserting legend image at the top-right of the graph
    im = plt.imread('candlestick.png') # insert local path of the image.
    newax = fig.add_axes([0.8,0.8,0.2,0.2], anchor='SE', zorder=0)
    newax.imshow(im)
    newax.axis('off')

    

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    plt.show()




def plot_graph_4hours(currency, dates, openings, closings, highs, lows ):
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

    candlestick_ohlc(ax, ohlc.values, width=0.1, colorup='green', colordown='red', alpha=0.8)

    # Inserting legend image at the top-right of the graph
    im = plt.imread('candlestick.png') # insert local path of the image.
    newax = fig.add_axes([0.8,0.8,0.2,0.2], anchor='SE', zorder=0)
    newax.imshow(im)
    newax.axis('off')

    crypto= currency[:3]
    fiat= currency[3:]
    fig.suptitle('Candlestick Chart for: ' + crypto.upper() + " " + fiat.upper())

    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price in ' + fiat)

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    plt.show()




def plot_graph_12hours(currency, dates, openings, closings, highs, lows ):
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

    candlestick_ohlc(ax, ohlc.values, width=0.3, colorup='green', colordown='red', alpha=0.8)

    # Inserting legend image at the top-right of the graph
    im = plt.imread('candlestick.png') # insert local path of the image.
    newax = fig.add_axes([0.8,0.8,0.2,0.2], anchor='SE', zorder=0)
    newax.imshow(im)
    newax.axis('off')

    crypto= currency[:3]
    fiat= currency[3:]
    fig.suptitle('Candlestick Chart for: ' + crypto.upper() + " " + fiat.upper())

    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price in ' + fiat)

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    plt.show()





def plot_graph_oneday(currency, dates, openings, closings, highs, lows ):
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

    candlestick_ohlc(ax, ohlc.values, width=0.5, colorup='green', colordown='red', alpha=0.8)

    # Inserting legend image at the top-right of the graph
    im = plt.imread('candlestick.png') # insert local path of the image.
    newax = fig.add_axes([0.8,0.8,0.2,0.2], anchor='SE', zorder=0)
    newax.imshow(im)
    newax.axis('off')

    crypto= currency[:3]
    fiat= currency[3:]
    fig.suptitle('Candlestick Chart for: ' + crypto.upper() + " " + fiat.upper())

    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price in ' + fiat)

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    plt.show()
