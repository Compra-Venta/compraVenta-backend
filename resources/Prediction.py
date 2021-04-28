from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from prediction_model import prediction
all_symbols = {'BTCUSDT', 'ETHUSDT', 'ETHBTC', 'LTCBTC', 'LTCUSDT','XRPBTC', 'XRPBNB', 'LTCBNB', 'BNBBTC','BNBETH','XRPETH','LTCETH','BNBUSDT','XRPUSDT'}
class Predict(Resource):
    def get(self):
        symbol = request.args.get('symbol')
        interval = request.args.get('time')
        if symbol not in all_symbols:
        	return {"error":"Invalid Symbol"}, 400
        if interval not in {"1d", "3d", "1w"}:
        	return {"error":"Invalid time interval"}, 400
        
        p = prediction.get_predictions(symbol, interval)

        if p != None:
            return {'prediction':p}, 200
        else:
            return {'error':'An error occurred'}, 500
