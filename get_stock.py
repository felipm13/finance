import datetime
import pandas_datareader as pd_dr

vale = "VALE3.SA"
petr = "PETR4.SA"
bbdc = "BBDC4.SA"
mglu = "MGLU3.SA"
ibov = "^BVSP"

start = datetime.datetime(2015,1,1)
end = datetime.datetime(2018,12,19)

print("Getting data from VALE3...")
data = pd_dr.get_data_yahoo(vale, start, end)
data.to_csv("VALE3.csv")

print("Getting data from PETR4...")
data = pd_dr.get_data_yahoo(petr, start, end)
data.to_csv("PETR4.csv")

print("Getting data from BBDC4...")
data = pd_dr.get_data_yahoo(bbdc, start, end)
data.to_csv("BBDC4.csv")

print("Getting data from MGLU3...")
data = pd_dr.get_data_yahoo(mglu, start, end)
data.to_csv("MGLU3.csv")

print("Getting data from IBOVESPA...")
data = pd_dr.get_data_yahoo(ibov, start, end)
data.to_csv("IBOV.csv")
