import schedule
import time
import datetime

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

from threading import Thread as th
from ta.utils import dropna
from contextlib import suppress

import ta # for tech analysis
import threading

# Threaded function snippet, for multiple strategies running at once.
def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper


class Indicators(object):
    def __init__(self):
        self.data = None
    
    def cseries(self, arr):
        return pd.Series(arr)
    
    def get_last(self, data=None, window=2):
        
        if data is None:
            data = self.data.Close
            
        return data[-window]
    
    def get_rsi(self):
        close = self.data.Close
        return ta.momentum.RSIIndicator(close).rsi()
    
    def get_macd(self):
        close = self.data.Close
        macd = ta.trend.MACD(close).macd()
        return macd
    
class RSIstrategy(Indicators):
    def __init__(self, letter='BTC-USD'):
        super().__init__()
        # basic parameters
        self.buy_price = 0
        self.letter = letter
        self.position = False
        self.interval = '15m'
        self.period = '1d'
        self.stop_level, self.profit_level = 1, 1
        
        # custom parameters
        self.RRR            = 1.6
        self.STOP_AMOUNT    = 735
        
        self.rsi_value = 30
        self.stop_price = 190000
        
    def load_data(self):
        df = yf.download(
            self.letter,
            period = self.period,
            interval = self.interval,
            progress = False
            )
        return df
    
    def strategy(self):
        # load data
        self.data = self.load_data()
        last = self.get_last()
        
        # look for conditions
        if not self.position:
            last_rsi = self.get_last(data=self.get_rsi())
            
            # conditions
            condA = last_rsi < self.rsi_value
            condB = last < self.stop_price
            
            print(last_rsi, last)
            if condA and condB:   
                self.buy()
                self.stop_level, self.profit_level = self.get_sl_tp()
                msg = f"stop_level = {self.stop_level} \n\
                    profit_level = {self.profit_level}"
                print(msg)
            else:
                print('waiting conditions...')
                
        # look for exits
        else:
            if last > self.profit_level or last < self.stop_level: # exit conditions
                self.close()
            else:
                print('waiting tp / sl')

    def buy(self):
        print('buy')
        self.buy_price = self.get_last()
        self.position = True
    
    def close(self):
        print('closing position')
        self.position = False
        
    def get_sl_tp(self):
        stop_level = self.buy_price - self.STOP_AMOUNT
        profit_level = self.RRR*(self.buy_price-stop_level)+self.buy_price
        return stop_level, profit_level
    
    @threaded
    def run_strategy(self):
        while True:
            try:
                self.strategy()
                time.sleep(4)
            except Exception as e:
                print(e)
                

