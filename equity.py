import yfinance as yf


ticker = 'META'

yf_finance = yf.Ticker(ticker) 




non_current_assets = yf_finance.quarterly_balance_sheet.loc['Total Non Current Assets'].iloc[0]
net_liabilities = yf_finance.quarterly_balance_sheet.loc['Total Liabilities Net Minority Interest'].iloc[0]
cash = yf_finance.quarterly_balance_sheet.loc['Cash Cash Equivalents And Short Term Investments'].iloc[0]
shares_outstanding = yf_finance.quarterly_balance_sheet.loc['Ordinary Shares Number'].iloc[0]

print(f' Non Current Assets == {non_current_assets}')
print(f' Net Liabilities == {net_liabilities}')
print(f' CASH == {cash}')
print(f' Share Count == {shares_outstanding}')