import yfinance as yf
import pandas as pd
import requests


print(yf.download("^FVX")["Adj Close"].iloc[-1])





def request(version, endpoint, ticker=None, period=None):
        try:
            if ticker is None:
                ticker_symbol = symbol  
            else:
                ticker_symbol = ticker

            period_str = f'period={period}&' if period and (period == 'quarterly' or period == 'annual') else ''

            url = f"https://financialmodelingprep.com/api/{version}/{endpoint}/{ticker_symbol}?{period_str}apikey={api_key}"
            print(f"Request URL: {url}") 

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                return data
            
        except Exception as e:
            print(f"Error occurred while processing {ticker_symbol}: {response.status_code} {e}")
            return None



segmented_revenue = pd.DataFrame(request('v4', 'revenue-geographic-segmentation'))

version = 'v4'
endpoint = 'market_risk_premium'

market_risk_premiums = request(version, endpoint)
