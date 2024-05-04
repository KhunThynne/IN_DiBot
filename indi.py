from datetime import datetime,timedelta
import json
import os
import sys
from matplotlib import pyplot as plt
# from inter import Interface
from trading_technical_indicators.tti.indicators import MovingAverageConvergenceDivergence
import pandas as pd
from MQL_Five import initailize
from MQL_Five.order import Order
from time import sleep
from IPython.display import display, HTML
#Initailize
os.system('cls')
mt5 = initailize.initial_login()
symbol = "EURUSD"
#Dataset
# Trade_signal.request()
class ExportsDataset():
    def __init__(self,name,dataset,symbol,indicator,indicator_value) -> None:
        global MACD_return,result_Data,data
        self.name = name
        self.dataset = dataset
        self.symbol = symbol
        self.indicator = indicator
        self.indicator_value = indicator_value
        self.initial()
        self.exportfile()
    
    def initial(self)->None:
        os.makedirs(f"./dataset/{self.symbol}/indicators/{self.indicator}", exist_ok=True)
                  
    def exportfile(self) -> None:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        with open(f'dataset/{self.symbol}/Dataset_{date_time}.json', 'w') as f:
            f.write(self.dataset.to_json(orient="index"))
        #indicators
       
        with open(f'dataset/{self.symbol}/indicators/{self.indicator}/Dataset_{date_time}.json', 'w') as f:
            f.write(self.indicator_value.to_json(orient="index"))

def macd(): 
    global dataset,MACD_return,result_Data,data
    data = mt5.copy_rates_from("EURUSD",mt5.TIMEFRAME_M5,pd.Timestamp.now(), 1000)
    data = pd.DataFrame(data)
    data['date'] = pd.to_datetime(data['time'], unit='s')
    data.set_index('date', inplace=True)
    data['time'] = data.index.strftime('%H:%M:%S')
    MACD = MovingAverageConvergenceDivergence(input_data=data)
    MACD_return = MACD._calculateTi()   
    Signal = MACD.getTiSignal()  
    # data= data.join(MACD_return)
    return Signal 
def main():
    global data,MACD_return
    ### Ckeak symbol can subscribe
    if not mt5.symbol_select(symbol, True):
        print(f"Failed to subscribe to {symbol}, error code =", mt5.last_error())
        mt5.shutdown()
        quit()
    try:
        tick = mt5.symbol_info_tick(symbol)#Get tick event
        
        while True:
             
          
            sleep(0.01)

        # เช็คว่ามีการกดคีย์หรือไม่
            if tick:
                Signal = macd()
                signal =Signal[0]
                if signal != 'hold':
                    print(Signal[0])
                    lot = 0.1
                    point = mt5.symbol_info(symbol).point
                    price = mt5.symbol_info_tick(symbol).ask
                    deviation = 20
                    request = {
                        "action": mt5.TRADE_ACTION_DEAL,
                        "symbol": symbol,
                        "volume": lot,
                        "type":  mt5.ORDER_TYPE_BUY if signal == 'buy' else mt5.ORDER_TYPE_SELL,
                        "price": price,
                        "sl": price - 100 * point,
                        "tp": price + 100 * point,
                        "deviation": deviation,
                        "magic": 234000,
                        "comment": "python script open",
                        "type_time": mt5.ORDER_TIME_GTC,
                        "type_filling": mt5.ORDER_FILLING_RETURN,
                    }
                    result = mt5.order_send(request)
                    print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol,lot,price,deviation))
                    if result.retcode != mt5.TRADE_RETCODE_DONE:
                        print("2. order_send failed, \nretcode={}".format(result.retcode))
             
    except KeyboardInterrupt as e:
        ExportsDataset('data',data,symbol,"macd",indicator_value=MACD_return)
        print("Script interrupted by user.")
        quit()
    except AttributeError as e:
        print(f"Error:  {e}")
    mt5.shutdown()


main()