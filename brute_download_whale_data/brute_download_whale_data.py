#on primary monitor, place chrome on left half

import os
import pyautogui
import time
from PIL import ImageGrab

start = 8690 #e.g if start at whale 3500, start should be 3499
end = 10000
small_sleep = 0.5

f = open("address_list_2021-06-29.txt", 'r')
address_lines = f.readlines()
bg_RGB = (17, 20, 3)

def alt_(key):
    pyautogui.keyDown('alt')
    time.sleep(0.1)
    pyautogui.press(key)
    time.sleep(0.1)
    pyautogui.keyUp('alt')


def ctrl_(key):
    pyautogui.keyDown('ctrl')
    time.sleep(0.1)
    pyautogui.press(key)
    time.sleep(0.1)
    pyautogui.keyUp('ctrl')

print('about to start downloading whale data, please prepare the following: ')
print('1. alt tab to chrome')
print('2. alt tab to blank notepad')
print('3. make sure save path is where the whale files are to go')
time.sleep(3)

for line in address_lines[start:end]:
    
    line = line.split(" === ")

    rank = line[0]
    address = line[1]
    btcval = line[2]
    btcval = btcval.replace('\n','')

    url = 'https://bitinfocharts.com/bitcoin/address/' + address + '-full'
    
    if(len(rank)==1):
        whale_name = 'whale000' + rank
    if(len(rank)==2):
        whale_name = 'whale00' + rank
    if(len(rank)==3):
        whale_name = 'whale0' + rank
    if(len(rank)==4):
        whale_name = 'whale' + rank
    if(len(rank)==5):
        whale_name = 'whale_last'

    alt_('d')
    time.sleep(small_sleep)
    pyautogui.write(url)
    time.sleep(small_sleep)
    pyautogui.press('enter')
    time.sleep(2.5)
    ctrl_('a')
    time.sleep(small_sleep)
    ctrl_('c')
    time.sleep(small_sleep)
    alt_('tab')
    time.sleep(small_sleep)
    ctrl_('v')
    time.sleep(small_sleep)
    ctrl_('s')
    time.sleep(small_sleep)
    pyautogui.write(whale_name)
    time.sleep(small_sleep)
    pyautogui.press('enter')
    time.sleep(0.1)
    ctrl_('n')
    time.sleep(0.1)
    alt_('tab')

    print(whale_name + ' saved')