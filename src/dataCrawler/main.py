import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from os import getenv

"""
Just a small scratchpad to checkout the API calls and test the project structure
"""
# get all tickers
# https://github.com/shilewenuw/get_all_tickers

ticker: str = getenv("TICKER", "AAPL")
ticker_data: yf.Ticker = yf.Ticker(ticker)

# get stock info
info = ticker_data.info
print(info)

# print(msft.recommendations)
# TODO: Foreign currencies?
# get historical market data
hist: pd.DataFrame = ticker_data.history(period="max")
# print(hist)
oldest = hist.iloc[[0]]
print(oldest)
most_recent = hist.iloc[[-1]]
# 'Open', 'High', 'Low', 'Close'
# print(most_recent.keys())

print("Stock Ticker:", ticker)
print("Current Price:", info['bid'], info['currentPrice'], info['regularMarketPrice'])
print("52 Week Price Range:", info['fiftyTwoWeekLow'], info['fiftyTwoWeekHigh'])
print("Analyst Target Mean Price: "
      + "low(" + str(info['targetLowPrice']) + ") "
      + "mean(" + str(info['targetMeanPrice']) + ") "
      + "median(" + str(info['targetMedianPrice']) + ") "
      + "high(" + str(info['targetHighPrice']) + ")")
print("P/E Ration:", info['currentPrice']/info['forwardEps'], info['forwardPE'], info['trailingPE'])
print("YTD Stock Gain:", info['ytdReturn'])
print("RO1Week:")
print("RO1Month:")
print("RO3Month:")
print("RO1Year:")
print("T Asses V. T Liabilities (up):", info['totalAssets'])  # Asses/Liabilities
print("Estimated Revenue Growth Last Year (up):")
print("Estimated Revenue Growth Forecast this year (up):")
print("Net Income Margin:", "profitMargins("+str(info['profitMargins'])+")")
print("Levered Free Cash Flow (up):", "FCF("+str(info['freeCashflow'])+")")
print("Cost Basis:")
# Manual IV Calculation:
# https://docs.google.com/spreadsheets/d/1OD-vYzsqfCLfsr0qzMojlMw0mXiaezxCsMrxfMQ5c0w/edit#gid=713559401
# Sector PE:
# http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/pedata.html
# https://fullratio.com/stocks
print("Cash-to-Debt:")
print("Equity-to-Asset:")
print("Debt-to-EBITDA:")
print("Piotroski F-Score:")
print("Altman Z-Score:")
print("Beneish M-Score:")
exit(0)

# show actions (dividends, splits)
print(ticker_data.actions)

# show dividends
print(ticker_data.dividends)

# show splits
print(ticker_data.splits)

# show financials
print(ticker_data.financials)
print(ticker_data.quarterly_financials)

# show major holders
print(ticker_data.major_holders)

# show institutional holders
print(ticker_data.institutional_holders)

# show balance sheet
print(ticker_data.balance_sheet)
print(ticker_data.quarterly_balance_sheet)

# show cashflow
print(ticker_data.cashflow)
print(ticker_data.quarterly_cashflow)

# show earnings
print(ticker_data.earnings)
print(ticker_data.quarterly_earnings)

# show sustainability
print(ticker_data.sustainability)

# show analysts recommendations
print(ticker_data.recommendations)

# show next event (earnings, etc)
print(ticker_data.calendar)

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
print(ticker_data.isin)

# show options expirations
print(ticker_data.options)

# get option chain for specific expiration
opt = ticker_data.option_chain('2021-07-16')
# data available via: opt.calls, opt.puts
print(opt)
