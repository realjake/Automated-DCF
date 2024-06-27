import yfinance as yf
import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
fmp_api_key = os.getenv('FMP_API_KEY')

def request(version, endpoint, ticker=None, period=None):
        try:
            if ticker is None:
                ticker_symbol = symbol  
            else:
                ticker_symbol = ticker

            period_str = f'period={period}&' if period and (period == 'quarterly' or period == 'annual') else ''

            url = f"https://financialmodelingprep.com/api/{version}/{endpoint}/{ticker_symbol}?{period_str}apikey={fmp_api_key}"
            print(f"Request URL: {url}") 

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                return data
            
        except Exception as e:
            print(f"Error occurred while processing {ticker_symbol}: {response.status_code} {e}")
            return None


symbol = 'AAPL'


data_table = pd.DataFrame(request('v3', 'income-statement', symbol, 'annual'))

data_table.set_index('date', inplace=True)
previous_revenue = None

data_table = data_table.tail(0)
print(data_table)


for index, row in data_table.index[:20]():
    revenue_current = row['revenue']
    
    if previous_revenue is not None:
        revenue_change = (revenue_current - previous_revenue) / previous_revenue
        print(f"Date: {index}, Revenue: {revenue_current}, Revenue Change: {revenue_change:.2%}")
    else:
        print(f"Date: {index}, Revenue: {revenue_current}, Revenue Change: N/A")
    
    previous_revenue = revenue_current
