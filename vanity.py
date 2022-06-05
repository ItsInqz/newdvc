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
ctypes.windll.kernel32.SetConsoleTitleW("vantiy checker | craigslol#0001")

# ========================================
# files

Codes = open('vanitys.txt', 'r').read().split('\n')
proxies = open('proxies.txt', 'r').read().split('\n')
available = open('available.txt', 'w')

# ========================================
# code

def vanity():
    for v in Codes:
        r = requests.get(f'https://discord.com/api/v9/invites/{v}',proxies={'http' : 'http://' + 'proxy'})
        if r.status_code == 200:
            print(f'          vanity taken | {v}')
        if r.status_code == 404:
            print(f'          vanity available | {v}')
            available.write(f'{v}\n')

# ========================================
# threads

thread = threading.Thread(target=vanity)
thread.start()
