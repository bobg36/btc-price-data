# make sure to remove header, only data allowed in csv files
# data format
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

filename = input('Enter CSV File to print to PNG Chart: ')

xpixel = 2544
ypixel = 1142

cryptodata = pd.read_csv(filename)

print('reading file: ' + filename + "...")
with open(filename, newline='') as f:
    reader = csv.reader(f)
    lines = list(reader)

highest = 0
lowest = 999999
candles = []

print('getting high, low, open, close, highest, lowest out of the most recent 640 candles (640 candles fit nicely on this specific monitor 2560x1440)')
for line in lines[1:640]: #636?
    high = float(line[4])
    low = float(line[5])
    open = float(line[3])
    close = float(line[6])
    green = True
    if(close > open):
        green = True
    else:
        green = False
    if(high > highest):
        highest = high
    if(low < lowest):
        lowest = low
    candles.append([high, low, green, open, close])

print('generating candle coordinates')
height = highest-lowest
ypixel_list = []
for candle in candles:
    high = candle[0]
    low = candle[1]
    green = candle[2]
    open = candle[3]
    close = candle[4]
    highpercent = (highest-high)/height
    lowpercent = (highest-low)/height
    openpercent = (highest-open)/height
    closepercent = (highest-close)/height
    highpixel = highpercent*ypixel
    lowpixel = lowpercent*ypixel
    openpixel = openpercent*ypixel
    closepixel = closepercent*ypixel
    ypixel_list.append([highpixel, lowpixel, green, openpixel, closepixel])

ypixel_list.reverse()

#========================================
#putting the above data into a png

print('printing candles to png')
from posixpath import join
from PIL import Image

im = Image.open("2544x1142.png")
pixels = im.load()
pixel_list_counter = 0 
for i in range(1, 2544):
    for j in range(0, 1142):
        if(i % 4!=0): #every 4th column is blank
            high = ypixel_list[pixel_list_counter][0]
            low = ypixel_list[pixel_list_counter][1]
            green = ypixel_list[pixel_list_counter][2]
            open = ypixel_list[pixel_list_counter][3]
            close = ypixel_list[pixel_list_counter][4]

            if(i % 2 == 0):
                if(j > high and j < low):
                    if(green==True):
                        pixels[i, j] = (120, 150, 100)
                    else:  
                        pixels[i, j] = (180, 100, 100)
            else:
                if(j > open and j < close):
                    if(green==True):
                        pixels[i, j] = (120, 150, 100)
                    else:  
                        pixels[i, j] = (180, 100, 100)
                if(j > close and j < open):
                    if(green==True):
                        pixels[i, j] = (120, 150, 100)
                    else:  
                        pixels[i, j] = (180, 100, 100)

    if(i % 4==0):
        pixel_list_counter = pixel_list_counter + 1
 
im.save("chart.png")
