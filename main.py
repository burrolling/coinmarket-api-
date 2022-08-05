from secrets import api_key
import requests
from yomama import yomama
import time
headers = {"X-CMC_PRO_API_KEY": api_key, "Accepts": "application/json"}
parameters = {"start": "1", "limit": 5, "convert": "USD"}
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

def cryptocurrency():
    global btc_price, btc_daily_change, eth_daily_change, eth_price, coin
    json = requests.get(url, params=parameters, headers=headers).json()
    coin = json["data"]
    btc_price = json["data"][0]["quote"]["USD"]["price"]
    btc_daily_change = json["data"][0]["quote"]["USD"]["percent_change_24h"]
    eth_price = json["data"][1]["quote"]["USD"]["price"]
    eth_daily_change = json["data"][1]["quote"]["USD"]["percent_change_24h"]
    return btc_price, eth_price
def display_crypto():
    print(
        f"btc price: {btc_price} btc daily change: {btc_daily_change}\neth price: {eth_price} eth daily change: {eth_daily_change}"
    )
previous = None
current = None
while True:
    current = cryptocurrency()[0]
    display_crypto()
    if previous == None:
        previous = current
        time.sleep(10)
        continue
    if previous < current:
        print('gud')
    else: 
        jokes = yomama()
        for i in jokes:
            print(i)
    time.sleep(45)

    
    