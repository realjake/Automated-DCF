import pandas as pd
import requests
from dotenv import load_dotenv
import numpy as np

import os

load_dotenv()
fmp_api_key = os.getenv('FMP_API_KEY')

def request(symbol, version=None, endpoint=None, period=None, exceptions=None):
    try:
        if symbol is None:
            raise ValueError("Ticker symbol is required.")
        if exceptions is not None:
            url = exceptions
        else:
            if version is None or endpoint is None:
                raise ValueError("Both version and endpoint are required if exceptions URL is not provided.")
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

symbol = 'AAPL'
data_table = pd.DataFrame(request(symbol, 'v3', 'income-statement', 'annual'))

tax_rates = data_table['incomeTaxExpense'] / data_table['incomeBeforeTax']
        
average_tax_rate = np.mean(tax_rates)

print(average_tax_rate)

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


symbol = 'AAPL'

fmp_url = f'https://financialmodelingprep.com/api/v4/historical/shares_float?symbol={symbol}&apikey={fmp_api_key}'

increasing_share_count = pd.DataFrame(request(symbol, exceptions=fmp_url))
# Ensure the 'date' column is in datetime format

print(increasing_share_count)
increasing_share_count['date'] = pd.to_datetime(increasing_share_count['date'])
# Sort the DataFrame by date
increasing_share_count = increasing_share_count.sort_values('date')
# Extract share counts for the dates a year apart
start_date = increasing_share_count['date'].min()
end_date = start_date + pd.DateOffset(years=1)
# Get the closest available data for start_date and end_date
start_share_count = increasing_share_count.loc[increasing_share_count['date'] <= start_date, 'outstandingShares'].iloc[-1]
end_share_count = increasing_share_count.loc[increasing_share_count['date'] <= end_date, 'outstandingShares'].iloc[-1]
# Calculate the percentage change
percentage_change = ((end_share_count - start_share_count) / start_share_count) * 100
print(f"The share count changed by {percentage_change:.2f}% over the year.")



