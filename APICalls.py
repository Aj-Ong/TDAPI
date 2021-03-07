import requests
import os
from dotenv import load_dotenv, find_dotenv
import datetime

def fetchlast24hours(ticker_symbol):
    load_dotenv(find_dotenv())
    
    TD_API_KEY = os.getenv('TD_API_KEY')
    BEARER_KEY = os.getenv('BEARER_KEY')
    
    TD_PRICE_URL = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory?apikey={}'.format('{}', TD_API_KEY)
    
    td_header = {
        "Authorization": 'Bearer {}'.format(BEARER_KEY)
    }
    
    apple_price_history = TD_PRICE_URL.format(ticker_symbol)
    apple_price_call = requests.get(apple_price_history, params={'apikey': TD_API_KEY, 'period':'1'})
    print(apple_price_call)
    data = apple_price_call.json()
    
    datelst = []
    openlst = []
    closelst = []
    highlst = []
    lowlst = []
    volumelst = []
    symbol = data['symbol']
    
    print(symbol)
    for items in data['candles']:
        datelst.append(datetime.datetime.fromtimestamp(items['datetime']/1000))
        openlst.append(items['open'])
        closelst.append(items['close'])
        highlst.append(items['high'])
        lowlst.append(items['low'])
        volumelst.append(items['volume'])
    
    return datelst, openlst, closelst, highlst, lowlst, volumelst, symbol