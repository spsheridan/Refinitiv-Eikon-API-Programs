import eikon as ek
import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta
import csv

pd.set_option("display.max_colwidth", None)

ek.set_app_key('1570e54c9efc47f29920e5a30bf05ba073f0d1d4') 

tickers_rics = ['']*1000

i = 0

with open('NASDAQtickers.csv', newline = '') as csvfile:
        tickers_reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
        for row in tickers_reader:
                tickers_rics[i] = row[0]
                i += 1

with open('NYSEtickers.csv', newline = '') as csvfile:
        tickers_reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
        for row in tickers_reader:
                tickers_rics[i] = row[0]
                i += 1

with open('AMEXtickers.csv', newline = '') as csvfile:
        tickers_reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
        for row in tickers_reader:
                tickers_rics[i] = row[0]
                i += 1

a = 0
for a in range(len(tickers_rics)):
    print(tickers_rics[a])
    tickers_float = ek.get_data([tickers_rics[a]], ['TR.FreeFloat'])
    tickers_outstanding = ek.get_data([tickers_rics[a]], ['TR.Outstanding'])
    tickers_shortinterest = ek.get_data([tickers_rics[a]], ['TR.ShortInterest'])
    print(tickers_float)
