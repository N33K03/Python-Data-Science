import pycoingecko
import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
id = 'bitcoin'
us_currency = 'USD'
days = 30
bitcoin_data = cg.get_coin_market_chart_by_id(id, us_currency, days) # gets data on Bitcoin in USD from the past 30 days
bitcoin_price_data = bitcoin_data['prices']

data = pd.DataFrame(bitcoin_price_data, columns = ['TimeStamp','Price'])  # puts data into data frame
data['Date'] = pd.to_datetime(data['TimeStamp'], unit = 'ms')
print(data)