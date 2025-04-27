import time, json, os, pandas

from binance.client import Client
from globals import BINANCE_API_KEY, BINANCE_API_SECRET

class BinanceClass():
    def __init__(self):
        api_key=BINANCE_API_KEY
        api_secret=BINANCE_API_SECRET
        self.client = Client(api_key, api_secret)


    def get_env_verify(self):
        var = os.get_env(var)
        assert var is not None, f'{var} is not set in the environment variables.'

    def get_account(self):
        account = self.client.get_account()
        arr = [x for x in self.client.get_account()['balances'] if float(x['free']) > 0]
        df = pandas.DataFrame(arr)
        return df
    
    def test_order(self):
        try:
            order = self.client.create_test_order(
                symbol='BTCUSDT',
                side='BUY',
                type='MARKET',
                quantity=0.001,
            )
            print("Test order successful")
        except Exception as e:
            print(f"Test order failed: {e}")

    def real_order(self, side="SELL", asset="BTC"):
        try:
            symbol = f'{asset}USDT'
            if side =="BUY":
                usdt = self.get_asset("USDT")
                price = float(self.client.get_symbol_ticker(symbol=f'{asset}USDT')['price'])
                qtty = usdt/price
                qtty = round(qtty, 8)
                qtty = int(qtty)
                order = self.client.order_market_buy(
                    symbol=symbol,
                    quantity=qtty
                )
            elif side =="SELL":
                qtty_btc=self.get_asset(asset)
                price = float(self.client.get_symbol_ticker(symbol=f'{asset}USDT')['price'])
                qtty_dolar = qtty_btc*price
                qtty = round(qtty_dolar, 6)
                order = self.client.order_market_sell(
                    symbol=symbol,
                    quantity=qtty
                )
            else:
                raise ValueError("Invalid order side. Use 'BUY' or 'SELL'.")
            return order
        except Exception as e: 
            print(f"Error placing order: {e}")
            return e
