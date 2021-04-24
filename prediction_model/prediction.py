# import tensorflow as tf
from binance.client import Client

def get_predictions(symbol,interval):
    from utils.StoplossThreads import client
    klines = client.get_historical_klines(symbol, interval, "1 Jan, 2015")
    values = [x[4] for x in klines]
    a = 0.7
    last_avg = 0
    for i in range(len(values)):
        t = values[i]
        last_avg = a*float(t) + (1-a)*last_avg
    return last_avg




