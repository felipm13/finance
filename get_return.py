import pandas as pd

vale = pd.read_csv('VALE3.csv', parse_dates=True, index_col='Date',)
daily_simple_returns = vale['Adj Close'].pct_change()
annual_returns = daily_simple_returns.mean() * 252
print(annual_returns)
