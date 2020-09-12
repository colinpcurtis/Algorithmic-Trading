from stocks import data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None


stocks = ["OCUL", "BBDC", "EVRI", "TRMLF", "IFSPF", "NGM", "EPD", "CHNG", "PINE", "CGEN", "HARP", "GOSS",
          "BCEL", "ARCC", "AUPH", "TELA", "COHU", "RCM", "KNSA"]

short = 2  # short and long term windows to compare
long = 5

signals = pd.DataFrame(index=data.index)
signals["signals"] = 0


signals["short avg"] = data["Open"].rolling(window=short, min_periods=1, center=False).mean()
signals["long avg"] = data["Open"].rolling(window=long, min_periods=1, center=False).mean()
signals["short vol"] = data["Open"].rolling(window=short, min_periods=1, center=False).std()
signals["long vol"] = data["Open"].rolling(window=long, min_periods=1, center=False).std()
# I initially also used volatility as part of the strategy, but that didn't seem to work as well.
# I kept the code here to continue doing tests with it
signals = signals.fillna(0)

signals["signals"][short:] = np.where((signals["short avg"][short:] > signals["long avg"][short:]), 1, 0)
signals = signals.fillna(0)

signals["positions"] = signals["signals"].diff()
signals = signals.fillna(0).round(4)
