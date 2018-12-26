import datetime
import pandas_datareader as pd_dr
import pandas as pd
import numpy as np

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2018,12,19)

data = pd.DataFrame()

random_selection=["MGLU3.csv","BBDC4.csv","PETR4.csv","VALE3.csv"]
for item in random_selection:
    data[item] = pd.read_csv(item, parse_dates=True, index_col='Date',)['Adj Close']

daily_simple_returns = data.pct_change()

annual_returns = daily_simple_returns.mean() * 250

num_assets = len(random_selection)

weights = np.random.random(num_assets)
weights = weights / sum(weights)

port_returns_expected = np.sum(weights * annual_returns)

print(str(round(port_returns_expected * 100, 2)) + '%')
