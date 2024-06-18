import requests
from dotenv import load_dotenv
import os
from finvizfinance.quote import *
import yfinance as yf
import numpy as np
import time

# Load environment variables from .env file
load_dotenv()

class DCF:
    def __init__(self, symbol, api_key): 
        self.symbol = symbol
        self.api_key = api_key
        self.yf_finance = yf.Ticker(self.symbol) 

    def request(self, version, endpoint, ticker=None):
        try:
             
            if ticker is None:
                ticker_symbol = self.symbol  

            else:
                ticker_symbol = ticker

            url = f"https://financialmodelingprep.com/api/{version}/{endpoint}{ticker_symbol}?apikey={self.api_key}"

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                return data
            
        except Exception as e:
            print(f"Error occurred while processing {self.ticker}: {e}")
            return None
    

    def timeframe(self):
        # Finding "appropiate" time frame of the DCF
        ten_year_dcf = 0
        five_year_dcf = 0

        # If the company operates in an industry with high volatility or rapid change, long-term projections may be highly uncertain and less reliable.
        
        standard deviation
        Revenue Growth Variability
        Industry Beta
        External Factors
        stock_data = yf.download(self.ticker, period='5y', interval='1d')
        stock_returns = stock_data['Close'].pct_change().dropna()
        stock_volatility = np.std(stock_returns)
        
    
        revenue_volatility = np.std(self.revenue_growth_history)
        
        if stock_volatility > market_volatility * 1.5 or revenue_volatility > industry_revenue_volatility * 1.5 or self.industry_beta > 1.2:
            

        # Startups or early-stage companies with unpredictable growth trajectories often have less reliable forecasts beyond 5 years.


        # Industries with shorter business cycles (e.g., technology, fashion) might not benefit from a longer-term projection since market conditions can change drastically over a decade.


        # If there's insufficient historical data to make credible long-term forecasts, a shorter horizon might be more appropriate.


        # Mature companies with stable and predictable cash flows might not need a longer projection period. The stable nature of their business can be adequately captured in a 5-year model, and the terminal value can account for subsequent periods.
        

        # Industries prone to significant regulatory or technological changes may find it challenging to predict beyond 5 years.

        if self.ticker == 






        # 10 Year
        # Companies in mature and stable industries with predictable growth patterns can benefit from a longer-term projection.
        # Companies with long-term capital investments and infrastructure projects, such as utilities or real estate, may require a longer projection period to accurately reflect their cash flows.
        # Industries with long product development and life cycles (e.g., pharmaceuticals, aerospace) might need a longer DCF period to capture the return on their investments.
        # High-growth companies that are expected to scale significantly over a decade may require a longer projection period to capture the expected expansion in their cash flows.
        

        
        if ten_year_dcf < five_year_dcf:
            print("5-year DCF is more appropriate due to high volatility.")
            total_timeframe = 5
        else:
            print("10-year DCF is more appropriate due to stable conditions.")
            total_timeframe = 10



    def discounted_cashflows(self):

        # Analyst Estimates
        version = 'v3'
        endpoint = 'analyst-estimates'

        estimate_data = self.request(version, endpoint)

        current_year = time.localtime().tm_year
        indexed_year = current_year

        # Checking to see length of estimates
        for entry in estimate_data:
        
            if indexed_year in entry['date']:
                indexed_year + 1
            else:
                analyst_timeframe = indexed_year - current_year
                print(f'Total Years of Analyst Estimation = {(analyst_timeframe)}')
        
    
        if indexed_year - current_year < 5:
            print(f'Calculating / estimating next {analyst_timeframe - total_timeframe}')

        else:

            






        # Financials for Reinvestment Analysis
        # (Net Capex + Change in Net Working Capital) / (Net Operating Profit After Taxes)
        
        
        # ROE method of growth estimation

        # 



        for year in years:
            ebit_average = data.get('estimatedEbitAvg')

            reinvestment_rate = 

            reinvestment = np.mean(reinvestment_rate)   

        for values in ebit_average:
            fcff_discounted =  values - reinvestment

            

    def wacc(self, risk_free_rate):
        
            # Calculation of market cap weighted industry unlevered beta
            version = 'v4'
            endpoint = 'stock_peers'
            peer_list = self.request(version, endpoint).get('peersList')



            market_cap = {}
            beta = {}



            for company in peer_list:
                version = 'v3'
                endpoint = 'profile'
                try:
                    company_data = self.request(version, endpoint, company)
                    beta[company] = company_data.get('beta')
                    market_cap[company] = company_data.get('mktCap')
                except:
                    continue  # If there is an error, skip this company
                


            # Filter out companies that don't have both beta and market cap
            market_cap = {company: cap for company, cap in market_cap.items() if company in beta and cap is not None and beta[company] is not None}



            # Calculate total market capitalization
            total_market_cap = sum(market_cap.values())



            weighted_beta_sum = 0



            for company, cap in market_cap.items():
                weight = cap / total_market_cap
                weighted_beta_sum += weight * beta[company]

    


            debt = self.yf_finance.balance_sheet.loc[]
            equity = 



            debt_to_equity_ratio = debt / equity



            cost_of_debt = 0.05     
        


            # grab equity risk premiums for segmented revenue streams
            version = 'v4'
            endpoint = 'market_risk_premium'



            market_risk_premiums = self.requests(version, endpoint)



            # grab segmented revenue streams
            version = 'v4'
            endpoint = 'revenue-geographic-segmentation'



            segmented_revenue = self.requests(version, endpoint)



            equity_risk_premium =
    


            cost_of_equity = risk_free_rate + beta * equity_risk_premium



            # Calculate WACC
            equity_weight = 1 / (1 + debt_to_equity_ratio)
            debt_weight = debt_to_equity_ratio / (1 + debt_to_equity_ratio)
            wacc = (equity_weight * cost_of_equity) + (debt_weight * cost_of_debt * (1 - 0.21))  # Assuming 21% tax rate
            


            return wacc

    def terminal(self):
        final_year = 
        terminal_fcff = (discounted_fcff[final_year] * (1 + growth_rate) /((wacc[final_year])^final_year))
        return value



    def fair_value(self):
        try:
            
            terminal_fcff = 
            
            non_current_assets = self.yf_finance.stock.quarterly_balance_sheet.loc['Total Non Current Assets'].iloc[0]
            net_liabilities = self.yf_finance.quarterly_balance_sheet.loc['Total Liabilities Net Minority Interest'].iloc[0]
            cash = self.yf_finance.quarterly_balance_sheet.loc['Cash Cash Equivalents And Short Term Investments'].iloc[0]
            shares_outstanding = self.yf_finance.quarterly_balance_sheet.loc['Ordinary Shares Number'].iloc[0]

            equity_value = sum(fcff_discounted) + terminal_fcff + non_current_assets + cash - net_liabilities 
            fair_value = equity_value / shares_outstanding
            return fair_value

        except Exception as e:
            print(f"Error occurred while processing {self.ticker}: {e}")
            return None
        


    def assumptions(self):
        print(f'Expected Ebit Margins == {ebit_margins}')



    api_key = os.getenv('API_KEY')
    if api_key is None:
        raise ValueError("API_KEY not found in environment variables. Please set it in your .env file. You can buy a subscription at Financial Modeling Prep")
    


if __name__ == "__main__":
    start_time = time.time()
    DCF = DCF() 
    ratios = updater.get_ratios()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")