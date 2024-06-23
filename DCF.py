from finvizfinance.quote import *
from dotenv import load_dotenv
import statsmodels.api as sm
import yfinance as yf
import numpy as np
import requests
import time
import os

class DiscountedCashFlows:
    def __init__(self, symbol, api_key): 
        self.symbol = symbol
        self.api_key = api_key
        self.yf_finance = yf.Ticker(self.symbol) 

    def request(self, version, endpoint, ticker=None, period=None):
        try:
            if ticker is None:
                ticker_symbol = self.symbol  
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
    
    def stock_data(self):

        # This function creates global variables that can be reused throughout the program.
        global profile 
        profile = 
        global balance_sheet_df = 


    def industry_beta(self):

        # Industry Beta
        market_caps = []
        industry_betas = []
        peer_list = []

        # Grab Company Peers
        peer_list = self.request('v4', 'stock_peers')
        peer_list_df = pd.DataFrame(peer_list)
        peer_list = peer_list_df.loc['peersList']

        for stock in peer_list:

            # Grab levered beta
            data = self.request('v3', 'profile', stock)
            data_df = pd.DataFrame(data)    
            beta = data_df.loc['beta']

            # Grab quarterly balance sheet
            balance_sheet = self.request('v3', 'balance-sheet-statement', stock, 'quarterly')
            balance_sheet_df = pd.DataFrame(balance_sheet)
            
            # Grab quarterly income statment
            income_statement = self.request('v3', 'income-statement', stock, 'quarterly')
            income_statement_df = pd.DataFrame(income_statement)

            # Tax, Debt & Equity info
            tax_rate = income_statement_df.loc['incomeBeforeTaxRatio']
            debt = balance_sheet_df.loc['totalDebt']
            equity = balance_sheet_df.loc['totalEquity']

            # Unlever the beta
            beta_unlevered = beta / (1 + (1-tax_rate) * (debt / equity ))
            mkt_cap = data_df.loc['mktCap']
            industry_betas.append(beta_unlevered)
            market_caps.append(mkt_cap)


        # Calculate unlevered industry beta
        unlevered_industry_beta = sum(beta * cap for beta, cap in zip(industry_betas, market_caps))

        return unlevered_industry_beta


    def reinvestment_rate(self):

        # Grab weighted average reinvestment rate + historical reinvestment rate


        pass

    def timeframe(self):

        # Finding "appropiate" time frame of the DCF
        # Startup / Hyper Growth / Self-Funding / Operating Leverage / Capital Return / Decline
        ten_year_dcf = 0
        five_year_dcf = 0
        
        # Revenue Growth Variability 
        income_statement = self.request('v3', 'income-statement', self.ticker, 'quarterly')
        income_statement_df = pd.DataFrame(income_statement).set_index('date')
        income_statement_df['revenue'] = income_statement_df['revenue'].astype(float)

        revenue_growth_list = []
        for i in range(1, len(income_statement_df.index[:10])):
            current_revenue = income_statement_df.iloc[i]['revenue']
            previous_revenue = income_statement_df.iloc[i-1]['revenue']
            rev_growth = (current_revenue - previous_revenue) / previous_revenue
    
            revenue_growth_list.append(rev_growth)

        revenue_growth_series = pd.Series(revenue_growth_list)
        revenue_growth_variability = revenue_growth_series.std()

        print(f'Revenue Growth Variablity = {revenue_growth_variability}')

        # If the company operates in an industry with high volatility or rapid change, long-term projections may be highly uncertain and less reliable.
        if self.industry_beta() > 1.5:
            five_year_dcf += 1

        # Startups or early-stage companies with unpredictable growth trajectories often have less reliable forecasts beyond 5 years.
        stock_lifetime = 
        if stock_lifetime < 5:
            five_year_dcf += 1


        # If there's insufficient historical data to make credible long-term forecasts, a shorter horizon might be more appropriate.


        # Mature companies with stable and predictable cash flows might not need a longer projection period. The stable nature of their business can be adequately captured in a 5-year model, and the terminal value can account for subsequent periods.
        

        # Industries prone to significant regulatory or technological changes may find it challenging to predict beyond 5 years.


        # Company in decline (lower Revenue / Gross Profit / Operating Profit / Net Profit / Increasing Share Count)

        # 10 Year
        # Companies in mature and stable industries with predictable growth patterns can benefit from a longer-term projection.
        # Companies with long-term capital investments and infrastructure projects, such as utilities or real estate, may require a longer projection period to accurately reflect their cash flows.
        # Industries with long product development and life cycles (e.g., pharmaceuticals, aerospace) might need a longer DCF period to capture the return on their investments.
        # High-growth companies that are expected to scale significantly over a decade may require a longer projection period to capture the expected expansion in their cash flows.
        global timeframe
            
        if ten_year_dcf < five_year_dcf:
            print("5-year DCF is more appropriate due to high volatility.")
            timeframe = '5'
            return timeframe
        else:
            print("10-year DCF is more appropriate due to stable conditions.")
            timeframe = '10'
            return timeframe


    

    def wacc(self, risk_free_rate):
            
            # Grab segmented revenue streams
            segmented_revenue = self.request('v4', 'revenue-geographic-segmentation')

            # Grab equity risk premiums for segmented revenue streams
            version = 'v4'
            endpoint = 'market_risk_premium'

            market_risk_premiums = self.request(version, endpoint)

            country_list = segmented_revenue.loc[]

            for countries in country_list:
                market_risk_premiums.loc[countries]



           

            equity_risk_premium = weight * revenue_stream       

            cost_of_equity = risk_free_rate + beta * equity_risk_premium

            # Calculate WACC & Relever beta
            equity_weight = 1 / (1 + debt_to_equity_ratio)
            debt_weight = debt_to_equity_ratio / (1 + debt_to_equity_ratio)
            wacc = (equity_weight * cost_of_equity) + (debt_weight * cost_of_debt * (1 - 0.21))  # Assuming 21% tax rate
            
            wacc_list = 
            


            return wacc_list
    

    def discounted_cashflows(self):

            # Analyst Estimates
            version = 'v3'
            endpoint = 'analyst-estimates'

            estimate_data = self.request(version, endpoint)
            estimate_data = pd.DataFrame(estimate_data).set_index('date')
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
                print(f'Calculating / estimating next {analyst_timeframe - self.timeframe}')

            else:
                # Financials for Reinvestment Analysis
                # (Net Capex + Change in Net Working Capital) / (Net Operating Profit After Taxes)

                # ROE method of growth estimation


                # EBIT estimate
                # Reinvestment Rate * Return on Capital


                pass
            
            fcff_discounted = []

            for year in analyst_timeframe:
                ebit_average = estimate_data.loc['estimatedEbitAvg'][year]

                reinvestment_rate = 

                reinvestment = np.mean(reinvestment_rate)   


            for values in ebit_average:
                fcff = (values - reinvestment) * (1 + wacc[values])

                fcff_discounted.append(fcff)


            global final_year_fcff
            final_year_fcff = fcff_discounted[-1]

            return fcff_discounted

    def terminal(self):
        final_year_fcff = 
        terminal_value = (ebit (1-tax_rate) (1-reinvestment_rate)) / (cost_of_capital - expected_growth)
        terminal_fcff = (discounted_fcff[final_year] * (1 + growth_rate) /((wacc[final_year])^final_year))
        return value

    def assumptions(self):
        print(f'Expected Ebit Margins == {ebit_margins}')
        print(f'Expected Rev Growth == {rev_growth}')
        print(f'Expected Tax Rate == {tax_rate}')
        print(f'Expected FCFF == {fcff}')


    def fair_value(self):
        try:
            self.stock_data
            self.industry_beta
            self.reinvestment_rate
            self.timeframe
            self.wacc
            self.terminal
            self.assumptions

            terminal_fcff = 
            
            non_current_assets = self.yf_finance.quarterly_balance_sheet.loc['Total Non Current Assets'].iloc[0]
            net_liabilities = self.yf_finance.quarterly_balance_sheet.loc['Total Liabilities Net Minority Interest'].iloc[0]
            cash = self.yf_finance.quarterly_balance_sheet.loc['Cash Cash Equivalents And Short Term Investments'].iloc[0]
            shares_outstanding = self.yf_finance.quarterly_balance_sheet.loc['Ordinary Shares Number'].iloc[0]

            equity_value = sum(self.discounted_cashflows) + terminal_fcff + non_current_assets + cash - net_liabilities 
            fair_value = equity_value / shares_outstanding

            current_market_cap = profile.loc['mktCap'] 
            percentage_difference = (current_market_cap - fair_value) / current_market_cap
            print("The percentage difference between the current market cap and the fair value is: %.2f%%" % (percentage_difference * 100))
            return fair_value

        except Exception as e:
            print(f"Error occurred while processing {self.ticker}: {e}")
            return None
        




if __name__ == "__main__":
    start_time = time.time()

    load_dotenv()

    ticker = 'AMZN'

    api_key = os.getenv('API_KEY')
    
    if api_key is None:
        raise ValueError("API_KEY not found in environment variables. Please set it in your .env file. You can buy a subscription at Financial Modeling Prep")
    
    DCF = DiscountedCashFlows(ticker, api_key) 

    fair_value = DiscountedCashFlows.fair_value

    print(f'Based on estimates, the fair value for {ticker} = {fair_value}')
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")