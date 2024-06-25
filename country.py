
import requests
import pandas as pd


url = 'https://financialmodelingprep.com/api/v4/market_risk_premium?apikey=1df5bacad305390341e32447587dd342'
response = requests.get(url)
if response.status_code == 200:
                data = pd.DataFrame(response.json())
else:
    exit(1)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(data.set_index('country'))