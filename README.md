# Trading-bots with Binance and Telegram
This project is a Python-based automated trading algorithm designed to operate on the Binance platform. It communicates in real-time with the user via Telegram, providing trading alerts, system updates, and visual analysis reports.

The algorithm combines data analysis techniques and financial automation, with the potential to be extended into full machine learning applications for decision-making.

This bot is capable of:

- Fetching real-time and historical asset prices (e.g., BTC-USD) via Yahoo Finance (yfinance).

- Executing real buy/sell orders on Binance via its API.

- Sending notifications about trading actions through Telegram.

- Running automatically in periodic monitoring loops.

This bot is structured as a development template, making it easy to extend with new indicators, risk management systems, or even other machine learning modules.

# Structure:
main.py: Main file to run the trading bot.

globals.py: for general constants. Load credentials or whatever you feel useful.

binance.py: Module for handling Binance API.

telegram.py: Module for sending messages via Telegram.

custom_strategies.py: Contains custom indicators and strategy definitions.

Not included but a nice to add: 

backtesting: the backtesting library is useful for the testing and performance's visualization of different strategies. It is not included in the script but it's an available library. For more information visit their website or read their docummentary.

# Dependencies and Technologies
Binance API: For real-time market data access and trade execution on the user's account.

Telegram API: For interactive user communication, including notifications, charts, and commands.

yfinance: To retrieve and update historical financial data from Yahoo Finnance service.

pandas: For time-series data manipulation and analysis.

numpy: For efficient numerical computations.

matplotlib: For data visualization and graphical reporting.

# Program Flow

Data Fetching: The bot downloads recent price data of the chosen asset (e.g., "KNC-USDT") via yfinance.

Strategy Application: It evaluates buying or closing conditions based on simple price rules (BUY_VALUE, STOP_AMOUNT, and risk/reward ratio). <-- Custom strategies are welcomed, this bot present a quite simple and
basic strategy (buy if value reaches X, sell if reaches Y). 

Order Execution: If conditions are met, it places real orders on Binance (real_order) and sends notifications via Telegram (send_message).

Automatic Loop: The bot continuously runs, checking market conditions every 4 seconds. It may be important to add other features that may keep this bot running healthly, like CPU usage, some price warnings, etc.

# About...
This project is intended for educational and development purposes.

It should not be used with real funds without thorough backtesting and testing in paper trading or Binance testnet environments.

Additional error handling (e.g., fund verification, API connection checks) is recommended for production use.

Machine Learning techniques for strategies and backtesting library for performance visualization is currently in the works. Feel free to message me for any doubt or suggestion!
