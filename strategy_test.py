import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from strategy import signals
from stocks import data


class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.signal = signals.loc[ticker]
        self.stock_data = data.loc[ticker]

    initial_capital = 3000

    num_of_stock = 30  # how much stock we buy at each order

    def execute_strategy(self):
        positions = pd.DataFrame(index=self.signal.index).fillna(0.0)

        positions["stock"] = Stock.num_of_stock * self.signal["signals"]
        portfolio = positions.multiply(self.stock_data["Open"], axis=0)

        pos_diff = positions.diff()
        portfolio["holdings"] = (positions.multiply(self.stock_data['Open'], axis=0)).sum(axis=1)
        portfolio['cash'] = Stock.initial_capital - (pos_diff.multiply(self.stock_data['Open'], axis=0))\
            .sum(axis=1).cumsum()
        portfolio['total'] = portfolio['cash'] + portfolio['holdings']
        portfolio['returns'] = portfolio['total'].pct_change()
        return portfolio

    def get_sharpe(self):  # Sharpe Ratio is a measure of performance vs. risk, the bigger the better
        returns = self.execute_strategy()
        returns = returns["returns"]
        sharpe_ratio = np.sqrt(252) * (returns.mean() / returns.std())
        sharpe_ratio = sharpe_ratio.round(4)
        return sharpe_ratio

    def plot_holdings(self):  # shows holdings for a stock, and when we buy/sell it
        portfolio = self.execute_strategy()
        # signal = signals.loc[self.ticker, :]
        fig = plt.figure()

        ax1 = fig.add_subplot(111, ylabel='Portfolio value')

        portfolio['total'].plot(ax=ax1, lw=2.)

        ax1.plot(portfolio.loc[self.signal.positions == 1.0].index,
                 portfolio.total[self.signal.positions == 1.0],
                 '^', markersize=10, color='m')
        ax1.plot(portfolio.loc[self.signal.positions == -1.0].index,
                 portfolio.total[self.signal.positions == -1.0],
                 'v', markersize=10, color='k')
        plt.suptitle(f"Portfolio Value for {self.ticker}")
        plt.title(f"Sharpe Ratio: {self.get_sharpe()}", size="small")
        plt.show()
