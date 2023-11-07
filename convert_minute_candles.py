timeframe = input('input timeframe in minutes to generate csv from 1m candles: ')
timeframe = int(timeframe)

filename = "Binance_BTCUSDT_minute.csv"

# crypto data fields, note: 0th line is str, only use 1st line onwards
# 0 - unix time
# 1 - date time
# 2 - crypto/usdt
# 3 - open
# 4 - high
# 5 - low
# 6 - close
# 7 - volume crypto
# 8 - volume usd
# 9 - trade count

from os import close, pardir
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import time



print('reading minute data')
#reading in data
cryptodata = pd.read_csv(filename)

with open(filename, newline='') as f:
    reader = csv.reader(f)
    lines = list(reader)

#5 min
#640*5 = 3200

lines.reverse()
line_5min = []
count = 0
tempcount = 0
modlist = []
while tempcount < timeframe:
    modlist.append(tempcount)
    tempcount = tempcount + 1
unix = 0
date = 0
symbol = 0
open_0 = 0
high_0 = 0
low_0 = 99999999999
vol_btc = 0
vol_usdt = 0
tradecount = 0
lastlines = 640*timeframe
print('converting to ' + str(timeframe) + ' minutes timeframe')
for line in lines[-timeframe*640:]:#640*timeframe
    date_temp = line[1]
    minute = date_temp[14:16]
    min = int(minute)
    mod = min % 5
    if(min % timeframe == 0):
        unix = line[0]          #final
        date = line[1]          #final
        symbol = line[2]        #final
        open_0 = float(line[3]) #final
        high_0 = float(line[4])
        low_0 = float(line[5])
        vol_btc = float(line[7])
        vol_usdt = float(line[8])
        tradecount = float(line[9])
    for num in modlist[1:timeframe]:
        curr_high = float(line[4])
        curr_low = float(line[5])
        curr_vol_btc = float(line[7])
        curr_vol_usdt = float(line[8])
        curr_tradecount = float(line[9])
        if(min % timeframe == num):
            if(high_0 < curr_high):
                high_0 = curr_high
            if(low_0 > curr_low):
                low_0 = curr_low
            vol_btc = vol_btc + curr_vol_btc
            vol_usdt = vol_usdt + curr_vol_usdt
            tradecount = tradecount + curr_tradecount
    if(min % timeframe == timeframe-1):
        close_0 = line[6]
        line_5min.append([unix, date, symbol, open_0, high_0, low_0, close_0, vol_btc, vol_usdt, tradecount])
    
line_5min.reverse()

filename = 'Crypto_Output'+str(timeframe)+'minute.csv'
file2 = 'w+'
f1 = open(filename, file2)
# f1.write('unix,date,symbol,open,high,low,close,Volume BTC,Volume USDT,tradecount\n')
for line in line_5min:
    for col in line:
        f1.write(str(col) + ",")
    f1.write("\n")
f1.close()

print('finished writing to Binance_BTC_USDT_'+str(timeframe)+'minute.csv')
