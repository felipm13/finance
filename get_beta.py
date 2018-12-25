import pandas as pd
from scipy import stats

vale = pd.read_csv('VALE3.csv', parse_dates=True, index_col='Date',)
ibov = pd.read_csv('IBOV.csv', parse_dates=True, index_col='Date')

# joining the closing prices of the two datasets
monthly_prices = pd.concat([vale['Close'], ibov['Close']], axis=1)
monthly_prices.columns = ['VALE3', 'IBOV']

# check the head of the dataframe
#print(monthly_prices.head())

# calculate monthly returns
monthly_returns = monthly_prices.pct_change(1)
clean_monthly_returns = monthly_returns.dropna(axis=0)  # drop first missing row
#print(clean_monthly_returns.head())


# split dependent and independent variable
X = clean_monthly_returns['IBOV']
y = clean_monthly_returns['VALE3']

slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)
print("Beta: ", slope)
