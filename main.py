#librerias

import pandas as pd
import matplotlib.pyplot as plt
import ta
import yfinance as yf
import os
import sys
import pathlib as Path
from  dotenv import load_dotenv

load_dotenv()


from binance import BinanceClass
from telegram import send_message
from custom_strategies import *

class DummyStrategy(Indicators):
    def __init__(self, letter="BTC-USD"):
        super().__init__()

        self.buy_price=0
        self.letter = letter
        self.position = False
        self.interval = "15m"
        self.period = "1d"
        self.data = self.load_data()
        self.buy_msg = ""

        self.RRR = 1.6
        self.STOP_AMOUNT = 735


    def load_data(self):
        df = yf.download(
            self.letter,
            period=self.period,
            interval=self.interval,
            progress=False
        )
        return df
    


    def strategy(self):
        self.data = load_data()
        last = self.get_last()

        #look for conditions
        if not self.position:
            #conditions
            condA = last > BUY_VALUE

            
            if condA:
              self.stop_level, self.profit_level = self.get_sl_tp()
              msg = f"Buying {self.letter}!, taking profit = {round(self.profit_level, 2)}, buy price = {round(last, 2)}" 
              self.buy_msg = msg
              self.buy()
            else:
                print("waiting conditions...")

        else:
            if last > self.profit_level or last < self.stop_level:
                self.close()
            else:
                print("waiting tp / sl")
        
    def get_sl_tp(self):
        buy_price = self.get_last()
        stop_level = buy_price - self.STOP_AMOUNT
        profit_level = self_RRR*(buy_price - stop_level)+buy_price
        return stop_level, profit_level
    
    @threaded
    def run_strategy(self):
        while True:
            try:
                self.strategy()
                time.sleep(4)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(5)
                

class DummyStrategy_notif_binance(DummyStrategy):
    def __init__(self, letter="BTC-USD"):
        super().__init__(letter=letter)
        self.position = False
        self.buy_msg = ""
        self.binance = BinanceClass()
        self.telegram = send_message()
        self.letter = letter

    def buy(self):
        msg = self.buy_msg
        self.telegram = send_message(msg)
        self.binance.real_order("BUY",asset=ASSET)
        self.position = True
    
    def close(self):
        self.telegram=send_message("Closing position")
        self.binance.real_order("SELL",asset=ASSET)
        self.position = False



if __name__ == "__main__":
    BUY_VALUE = 0.5
    STOP_AMOUNT = 0.2
    ASSET = "KNC"
    strategy = DummyStrategy_notif_binance(f'{ASSET}-USDT')
    strategy.run_strategy()
