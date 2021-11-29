import csv

def write_csv(currency, input_date, today, dates, prices):
    
    name=currency+'_from_'+str(input_date)+'_to_'+str(today)+'.csv'
    print(name)
    
    with open(name, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow(['Datetime', 'Price'])
    
        for i in range(0,len(dates)):
            writer.writerow([dates[i], prices[i]])