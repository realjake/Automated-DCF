import requests
from dotenv import load_dotenv
import os
import pandas as pd
from finvizfinance.quote import *
import yfinance as yf
import numpy as np
import matplotlib as plt


# Load environment variables from .env file
load_dotenv()


class DCF:
    def __init__(self, ticker, api_key): 
        self.ticker = ticker
        self.api_key = api_key
        

   
        
    def cashflows(self):


    def wacc(self):


    def equity(self):
        try:
            stock = yf.Ticker(self.ticker)
            non_current_assets = stock.quarterly_balance_sheet.loc['Total Non Current Assets'].iloc[0]
            net_liabilities = stock.quarterly_balance_sheet.loc['Total Liabilities Net Minority Interest'].iloc[0]
            cash = stock.quarterly_balance_sheet.loc['Cash Cash Equivalents And Short Term Investments'].iloc[0]
            shares_outstanding = stock.quarterly_balance_sheet.loc['Ordinary Shares Number'].iloc[0]
        except Exception as e:
            print(f"Error occurred while processing {self.ticker}: {e}")
            return None
        
    Revenues
Growth Rate

Operating Income
Operating Margin

Tax Rate


EBIT (1-t)


Reinvestment
% OF NOPAT

FCFF

Cost of Equity
Cost of Debt
AT Cost of Debt
Cost of Capital



    


    # List of stock symbols
    symbols = [
        "AMZN", "CRM", "UNH", "META", "ULTA", "GOOG", "MA", "INTU", "SPGI", "DPZ",
        "MSFT", "WM", "V", "EXP", "S", "ADBE", "AMAT", "CMG", "TXRH", "MELI", 
        "META", "NVDA", "VRTX", "EVVTY", "CRWD", "KO", "ADSK", "DHI", "PYPL", 
        "PLTR", "CCJ", "HAL"
    ]

    # Loop through each symbol and fetch ratings
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/analyst-estimates/{symbol}?apikey={api_key}"



        try:
            # Make the request to API
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                data = response.json()

                # Check if data is a list (handle special cases)
                if isinstance(data, list):
                    # Example of handling if data is a list:
                    if len(data) > 0:
                        rating_data = data[0].get('rating')
                        print(f"Rating for {symbol}: {rating_data}")
                    else:
                        print(f"No rating data found for {symbol}")
                elif isinstance(data, dict):
                    # Example of handling if data is a dictionary:
                    rating_data = data.get('rating')
                    if rating_data:
                        print(f"Rating for {symbol}: {rating_data}")
                    else:
                        print(f"No rating data found for {symbol}")
                else:
                    print(f"Unexpected data format received for {symbol}")

            else:
                # Print an error message if request was not successful
                print(f"Error: Status Code {response.status_code}")
                # You might want to print response.text for more details

        except requests.exceptions.RequestException as e:
            # Handle any exception that occurred during the request
            print(f"Request error: {e}")

        except json.JSONDecodeError as e:
            # Handle JSON decoding errors
            print(f"JSON decoding error: {e}")



    api_key = os.getenv('API_KEY')
    if api_key is None:
        raise ValueError("API_KEY not found in environment variables. Please set it in your .env file.")
