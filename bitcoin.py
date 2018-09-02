#!/usr/local/bin/python3
import json
import requests
import time

url = "http://coincap.io/history/1day/BTC"
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Host': 'coincap.io'}
r = requests.get(url, headers)

data = r.json()
price = data['price']

print(len(price))

money = 100000000
amount = 0

for i in range(7, len(price)):
    ptm = time.gmtime(price[i][0]/1000)
    avg = (price[i-7][1] + price[i-6][1] + price[i-5][1] + price[i-4][1] + price[i-3][1] + price[i-2][1] + price[i-1][1])/7
    if price[i][1] > avg and money > 0:
        print(ptm[0],ptm[1],ptm[2],ptm[3],ptm[4])
        amount = money/price[i][1]
        money = 0
        print("buy", amount, price[i][1], avg)
    elif price[i][1] < avg and money == 0:
        print(ptm[0],ptm[1],ptm[2],ptm[3],ptm[4])
        money = amount * price[i][1]
        amount = 0
        print("sell", amount, price[i][1], avg)

if money == 0:
    money = amount * price[287][1]
    amount = 0

print("final:", money, amount)

