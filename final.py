import sys
import os
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from custom_strategies import RSIstrategy
from telegramcorregido import Telegram_Mensaje
from decision_making import BinanceClass

class RSIstrategy_notif_binance(RSIstrategy):
    def __init__(self):
        super().__init__()
        self.position = False
        self.binance = BinanceClass()
        self.telegram = Telegram_Mensaje()

    def buy(self):
        self.telegram.send_telegram("buy")
        self.binance.real_order("BUY")
        self.position=True

    def close(self):
        self.telegram.send_telegram("sell")
        self.binance.real_order("sell")
        self.position = False


if __name__ == "__main__":
    strategy = RSIstrategy_notif_binance()
    strategy.run_strategy()
