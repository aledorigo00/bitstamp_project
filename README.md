# Bitstamp Project

## Project description
The bitstamp_project is an intuitive and easy-to-use software that performs
some analysis regarding financial instruments.
In this specific case, the software allows users to retrieve information about
three main cryptocurrencies, namely Bitcoin(BTC), Ethereum(ETH) and
Ripple(XRP).
The APIs integrated in our project are “ticker” and “ohlc” from Bitstamp
(https://www.bitstamp.net/api/)

## How to run and install the project
### Step 0.
If you haven’t done it yet, install git on your computer.

### Step 1.
Clone the repository using the command git clone followed by the link of
the project’s repository (https://github.com/aledorigo00/bitstamp_project.git).

### Step 2.
To successfully run our program, you need some additional libraries.
You should use the command ```pip install library_name``` to install them.
Libraries:
- ```json``` (for interpreting files from APIs)
- ```requests``` (for http communication)
- ```pandas``` (for data analysis and manipulation)
- ```numpy``` (for comprehensive mathematical functions)
- ```matplotlib``` (for visualization)
- ```mplfinance``` (for candlestick graph)
- ```csv``` (for reading and writing .csv files)

You are now ready to run the program.

## How to use the software
Our software provides three main different applications

### Current Price
You can check the current price in dollars or euros of cryptocurrencies.
When inserting the acronym of the desired crypto and currency as inputs,
the program outputs the corresponding current price.

Command example: ```python main.py btc usd```

List of cryptocurrencies: 
             btc, eth, xrp, ltc, bch, pax, xlm,
             link, omg, usdc, aave, bat, uma, knc, mkr, zrx,
             algo, audio, crv, snx, uni, yfi, comp, grt, usdt,
             eurt, matic, sushi, chz, enj, hbar, alpha, axs,
             ftt, sand, storj, ada, fet, rgt, skl, cel, slp,
             sxp, sgb, dydx, ftm, amp, gala, perp

List of fiat currencies: usd, eur

### Visualize cryptocurrencies trend
It is possible to check and visualize the price trend of cryptocurrencies
after thecrypto and currency names. The program will output the candlestick
graph of the trend.

Command example: ```python main.py btc usd -d 27/11/2021```

### CSV price value list
To Create a list in CSV format of all the price values recorded by
cryptocurrencies starting from a given period the user has to input
```-d dd/mm/yyyy -c``` and the program will output a .csv file with the 
cryptocurrency’s trend from the chosen date to the present date.

Command example: ```python main.py btc usd -d 27/11/2021 -c```


## Test (how to run)
Our software integrates a test suite to control that everything works fine.
To run the test suite type: ```python -m unittest -v -b tests/test_main.py```

## How to contribute to the project
If you find bugs and errors or you want to submit a request for improvements,
please open an issue in our github repository. You can find the repository of
our project at the following link:
https://github.com/aledorigo00/bitstamp_project.git

## License
GPL - 3.0 License https://www.gnu.org/licenses/gpl-3.0.html


## Credit
Alessandro Dorigo - https://github.com/aledorigo00,
Marco Signora - https://github.com/MarcoSignora,
Fabio Toffolo - https://github.com/FabioToffy
