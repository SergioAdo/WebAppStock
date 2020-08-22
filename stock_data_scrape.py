import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start= dt.datetime(2010,1,1)
end = dt.datetime(2020,8,22)

dfAMZ= web.DataReader('AMZN', 'yahoo', start, end)
dfAMZ.to_csv('amazon.csv')
dfGG= web.DataReader('GOOG', 'yahoo', start, end)
dfGG.to_csv('google.csv')
dfCAC= web.DataReader('CACLV.PA', 'yahoo', start, end)
dfCAC.to_csv('cac40.csv')
dfTSLA= web.DataReader('TSLA', 'yahoo', start, end)
dfTSLA.to_csv('tesla.csv')
dfCA= web.DataReader('ACA.PA', 'yahoo', start, end)
dfCA.to_csv('cagricole.csv')