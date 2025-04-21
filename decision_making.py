#librerias -------------
import time, json, os
import pandas as pd
from binance.client import Client

class BinanceClass(object):
    def __init__(self):
        api_key = API_KEY #Insert your Binance API-Key
        secret =  SECRET  #Binance Secret.
        self.client = Client(api_key,secret)

    def get_env_verify(self, var):
        var = os.getenv()
        assert var is not None, f"var {var} is none"
        return var

    def get_account(self):
        '''Get assets info of values above 0'''
        arr = [x for x in self.client.get_account()["balances"] if float(x["free"]) > 0]
        df = pd.DataFrame.from_dict(arr).set_index("asset") 
        print(df)
        return df

    def test_order(self):
        test = self.client.create_test_order(symbol = "BTCUSDT", side ="BUY", type="MARKET", quoteOrderQty = 10)
        return test

    def get_asset(self, asset):
        df = self.get_account()
        try:
            result = df.loc[asset]["free"]
        except:
            result = 0
        return float(result)

    def round_down(self, amount, coin):
        amount = float(amount)
        info = self.client.futures_index_info(f"{coin}USDT")
        step_size = [
            float(_["stepSize"]) for _ in \
            info["filters"] if _["filterType"] == "LOT_SIZE"][0]
        amount // step_size * step_size
        return amount




def real_order(self, side="SELL", asset="BTC"):
    try:
        symbol = f"{asset}USDT"
        if side == "BUY":
            usdt  = self.get_asset("USDT")
            price = float(self.client.get_symbol_ticker(symbol=f"{asset}USDT")["price"])
            qtty = usdt/price
            qtty = round(0.09*qtty, 8)
            qtty = int(qtty)
            order = self.client.order_market_buy(
                symbol=symbol,
                quantity=qtty
            )
        elif side == "SELL":
            qtty_btc = self.get_asset(asset)
            price = float(self.client.get_symbol_ticker(symbol=f"{asset}USDT")["price"])
            qtty_dollar = qtty_btc * price
            qtty = round(qtty_dollar, 6) # dollar round to 6
            order = self.client.order_market_sell(
                symbol=symbol,
                quantity=qtty
            )
        else:
            raise ValueError('choice not possible')



        return order

    except Exception as e:
        print(e)
        return e

#test ----
binance = BinanceClass()
binance.get_account()
binance.test_order()
