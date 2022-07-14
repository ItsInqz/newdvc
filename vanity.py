import requests
import os
import threading
from colorama import Fore
import time
import ctypes

# ========================================
# cmd 

cmd = 'mode 50,30'
os.system(cmd)
ctypes.windll.kernel32.SetConsoleTitleW("vanity checker | craigslol#0001 - modified by Inqz#9999")

# ========================================
# files

Codes = open('vanitys.txt', 'r').read().split('\n')
_2CharCodes = open('2chars.txt', 'r').read().split('\n')
proxies = open('proxies.txt', 'r').read().split('\n')
available = open('available.txt', 'w')

# ========================================
# code

def vanityNormal():
    for v in Codes:
        r = requests.get(f'https://discord.com/api/v9/invites/{v}',proxies={'http' : 'http://' + 'proxy'})
        if r.status_code == 200:
            print(f'          vanity taken | {v}')
        if r.status_code == 404:
            print(f'          vanity available | {v}')
            available.write(f'{v}\n')

def vanity2Char():
    for v in _2CharCodes:
        r = requests.get(f'https://discord.com/api/v9/invites/{v}',proxies={'http' : 'http://' + 'proxy'})
        if r.status_code == 200:
            print(f'          vanity taken | {v}')
        if r.status_code == 404:
            print(f'          vanity available | {v}')
            available.write(f'{v}\n')

# ========================================
# threads
programEnded = False


while programEnded == False:
    print("Choose which mode you would like to run.")
    themode = input("1. Normal\n2. 2-CHAR")
    if themode == 1:
        print("You have chosen mode: Normal")       
        thread = threading.Thread(target=vanityNormal)
        thread.start()
        programEnded == True
        print("Thank you for using Discord Vanity Checker written by craigslol#0001 - modified by Inqz#9999")
    elif themode == 2:
        print("You have chosen mode: 2-CHAR")
        thread = threading.Thread(target=vanity2Char)
        thread.start()
        programEnded == True
        print("Thank you for using Discord Vanity Checker written by craigslol#0001 - modified by Inqz#9999")
    else:
        pass


