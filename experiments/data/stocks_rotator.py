""" 
Use this file to create a new dataframe where each row is a day and each column is a stock price.
created = 12/14/2022
TODO: actually rotate these stocks lol
"""
import pandas as pd 
from pathlib import Path

STOCKS_PATH = Path('./experiments/data/sp500_stocks.csv').absolute()
print(STOCKS_PATH)
stocks = pd.read_csv(STOCKS_PATH, index_col=0,nrows=1000)

print(stocks.columns)
for symbol in stocks["Symbol"].unique():
    print(symbol)
    stock = pd.read_csv(f"./experiments/data/stocks/{symbol}.csv", index_col=0)
    stock = stock[["Adj Close"]]
    stock.columns = [symbol]
    stocks = stocks.join(stock, how="left")
    print(stocks.head())


