import time
from bitstamp import get_price

timeseries_eur=[]
timeseries_dollar=[]


for n in range(0,10):
	eur=get_price("btceur")
	timeseries_eur.append(eur)
	print("Last bitcoin price in EUR is: {}".format(eur))
	dollar=get_price("btcusd")
	timeseries_dollar.append(dollar)
	print("Last bitcoin price in $ is: {}".format(dollar))
	time.sleep(1)


print(timeseries_dollar)
