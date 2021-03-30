from binance.client import Client
import csv
client = Client("ohLjrUNYCSGejwTcHBJJlAn2Gxi8CREIfNLIblJIKVPYJlgciBcJTc5AIQAuqK5I",
                "yQWiR5UK2ZdfgtPELgrJwRQexyQK4Z65iH4U9X1evWsRWoPH4D2gwNXnTsCfY5ad")

data = client.get_historical_klines('LTCUSDT',Client.KLINE_INTERVAL_1DAY,"1 Jan, 2018","28 Mar, 2021")

with open('ethbtc-1d.csv','w',newline='') as file:
    fieldnames = ['timestamp','high','low','open','close','volume']
    writer = csv.DictWriter(file, fieldnames = fieldnames)

    writer.writeheader()
    for l in data:
        writer.writerow({'timestamp':l[0],'high':l[2],'low':l[3],'open':l[1], 'close':l[4], 'volume':l[5]})
