import datetime
import pandas_datareader as pd_dr

vale = "VALE3.SA"
ibov = "^BVSP"

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2018,12,19)

print("Getting data from VALE3...")
data = pd_dr.get_data_yahoo(vale, start, end)
data.to_csv("VALE3.csv")

print("Getting data from IBOVESPA...")
data = pd_dr.get_data_yahoo(ibov, start, end)
data.to_csv("IBOV.csv")
