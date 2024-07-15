import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
fmp_api_key = os.getenv('FMP_API_KEY')

def request(version, endpoint, symbol=None, period=None):
    try:
        if symbol is None:
            raise ValueError("Ticker symbol is required.")
        
        period_str = f'&period={period}' if period and (period == 'quarterly' or period == 'annual') else ''
        
        url = f"https://financialmodelingprep.com/api/{version}/{endpoint}/{symbol}?apikey={fmp_api_key}{period_str}"
        print(f"Request URL: {url}")

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error occurred while processing {symbol}: {e}")
        return None


symbol = 'AAPL'
data_table = pd.DataFrame(request('v3', 'income-statement', symbol, 'annual'))

print(data_table.tail(len(data_table.index)))
if data_table is not None:
    data_table.set_index('date', inplace=True) 
    
    previous_revenue = None
    
    

    for index, row in data_table.iterrows():
        revenue_current = row['revenue']

        if previous_revenue is not None and previous_revenue != 0:
            revenue_change = (revenue_current - previous_revenue) / previous_revenue
            print(f"Date: {index}, Revenue: {revenue_current}, Revenue Change: {revenue_change:.2%}")
        else:
            print(f"Date: {index}, Revenue: {revenue_current}, Revenue Change: N/A")

        previous_revenue = revenue_current
else:
    print(f"No data fetched for symbol: {symbol}")
