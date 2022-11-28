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
                #print(row[0])
                tickers_rics[i] = row[0]
                i += 1

with open('NYSEtickers.csv', newline = '') as csvfile:
        tickers_reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
        for row in tickers_reader:
                #print(row[0])
                tickers_rics[i] = row[0]
                i += 1

with open('AMEXtickers.csv', newline = '') as csvfile:
        tickers_reader = csv.reader(csvfile, delimiter = ' ', quotechar = '|')
        for row in tickers_reader:
                #print(row[0])
                tickers_rics[i] = row[0]
                i += 1


starttime = time.time()

while True:
        for x in tickers_rics:
                news_headlines = ek.get_news_headlines(x, 1)
                print(x)
                print("Most recent news headline:", news_headlines.loc[:, "text"])
                print('\n')
                time.sleep(.1)