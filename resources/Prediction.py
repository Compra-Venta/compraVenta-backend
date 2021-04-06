from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from prediction_model import prediction

class Predict(Resource):
    def get(self):
        symbol = request.args.get('symbol')
        prediction_time = request.args.get('time')
        if(prediction_time == '1d'):
            interval = '1d'
        
        data = [[   231.19   ,    212.74   ,    223.69   ,    222.61   , 20221.253  ],
                [   256.49   ,    222.62   ,    222.62   ,    247.33   , 63293.12934],
                [   253.4    ,    233.56   ,    247.33   ,    238.77   , 71369.27484],
                [   240.     ,    219.38   ,    238.89   ,    233.     , 78182.30493],
                [   250.99   ,    230.     ,    233.04   ,    240.54   , 65010.14465],
                [   315.     ,    238.73   ,    240.95   ,    275.28   , 100812.2137 ],
                [   287.     ,    262.     ,    276.24   ,    269.01   , 43811.61108],
                [   271.82   ,    212.74   ,    269.01   ,    252.65   , 76256.97086],
                [   257.64   ,    228.24   ,    252.49   ,    244.48   , 53921.90417],
                [   248.99   ,    225.05   ,    244.56   ,    247.63   , 70931.30085]]
        
        p = prediction.get_predictions(data, symbol, interval)

        if p != None:
            return {'prediciton':p}, 200
        else:
            return {'error':'an error occurred'}, 500