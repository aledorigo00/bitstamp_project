'''This module is used to perform operations related to CSV files.
    Specifically, it contains a function to write a CSV file from
    OHLC data'''
import csv
import os


def write_csv(crypto, fiat, input_date, today, dates, prices):
    '''This functions takes as inputs the arrays coming from
    the API and writes the csv in the current directory
    '''
    # give a significant name to the generated file and print it to
    # the user together with the path in order to be easily identified
    name = crypto+fiat+'_from_'+str(input_date)+'_to_'+str(today)+'.csv'
    print('"'+name+'" has been saved in ' +
          os.path.dirname(os.path.abspath(__file__)))

    with open(name, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow(['Datetime', 'Price'])

        for i in range(0, len(dates)):
            writer.writerow([dates[i], prices[i]])
