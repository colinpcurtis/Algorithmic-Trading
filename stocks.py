import datetime
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix


def get_tickers(tickers: list, start, end):  # creates dataframe for every stock, pulls data from yahoo finance
    def get_data(ticker):
        return pdr.get_data_yahoo(ticker, start=start, end=end)

    datas = map(get_data, tickers)
    return pd.concat(datas, keys=tickers, names=["Ticker", "Date"])


data = get_tickers(["OCUL", "BBDC", "EVRI", "TRMLF", "IFSPF", "NGM", "EPD", "CHNG", "PINE", "CGEN", "HARP", "GOSS",
                    "BCEL", "ARCC", "AUPH", "TELA", "COHU", "RCM", "KNSA"],
                   start=datetime.datetime(2019, 1, 1), end=datetime.datetime.now())
data = data.fillna(0).round(4)


def display_plot(ticker: str, column: str):  # displays a line plot for stock and specified attribute
    data.loc[ticker, column].plot(grid=True)
    plt.title(f"{ticker} - {column}")
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.show()


def get_pct_chng():  # gets daily percent change for each stock
    daily_close = data[["Adj Close"]].reset_index().pivot("Date", "Ticker", "Adj Close")
    daily_pct_change = daily_close.pct_change().fillna(0)
    return daily_pct_change


daily_change_pct = get_pct_chng()


def plot_daily_pct_change():  # plots a histogram of daily percent change, notice the normal distribution
    daily_change_pct.hist(bins=int(np.ceil(np.sqrt(len(daily_change_pct.index)))), sharex=True, figsize=(12, 8))
    plt.suptitle("Percent Change Histogram for Stocks")
    plt.show()


def plot_scatter_matrix():  # plots a matrix of scatter plots of one stock's pct. change against another
    scatter_matrix(daily_change_pct, diagonal="kde", alpha=.5, figsize=(12, 8))  # diagonal estimates distribution
    plt.suptitle("Scatter Matrix for Daily Percent Change")
    # plt.rcParams.update({'font.size': 10})
    plt.show()


def historical_volatility(min_periods):  # plots rolling volatility for every stock on the same graph
    vol = daily_change_pct.rolling(min_periods).std() * np.sqrt(min_periods)
    vol.plot(figsize=(10, 8))
    plt.title("Rolling Volatility Measure for Stocks")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.show()


def plot_volatility(ticker: str, period1: int, period2: int, period3: int):
    # plots rolling volatility with 3 different timescales for a single stock
    vol1 = daily_change_pct.loc[:, ticker].rolling(period1).std() * np.sqrt(period1)
    vol1.fillna(0)
    vol1.plot(figsize=(6, 6), label=f"{period1}")
    vol2 = daily_change_pct.loc[:, ticker].rolling(period2).std() * np.sqrt(period2)
    vol2.fillna(0)
    vol2.plot(figsize=(6, 6), label=f"{period2}")
    vol3 = daily_change_pct.loc[:, ticker].rolling(period3).std() * np.sqrt(period3)
    vol3.fillna(0)
    vol3.plot(figsize=(6, 6), label=f"{period3}")
    plt.title(f"Rolling Volatility for {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.legend()
    plt.show()


def volatility_histogram(min_periods):
    bins = int(np.ceil(np.sqrt(len(daily_change_pct.index))))
    vol = daily_change_pct.rolling(min_periods).std() * np.sqrt(min_periods)
    vol.hist(bins=bins, sharex=True, figsize=(12, 8))
    plt.suptitle("Volatility Histogram for Stocks")
    plt.show()
