from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.Watchlist import Watchlist

all_symbols = {'BTCUSDT', 'ETHUSDT', 'ETHBTC', 'LTCBTC', 'LTCUSDT','XRPBTC', 'XRPBNB', 'LTCBNB', 'BNBBTC','BNBETH','XRPETH','LTCETH','BNBUSDT'}

class get_watchlist(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type = str,
        required = True
    )
    @jwt_required()
    def get(self):
        data = self.parser.parse_args()
        email = data['email']
        mail = get_jwt_identity()
        if mail!=email:
            return {'error':"Invalid token"}, 401
        result = Watchlist.get_all_symbol(email)
        if result == None:
            return {'error':'some error occurred'}, 500
        else:
            return {'watchlist':result}, 200

class add_symbol_to_watchlist(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type = str,
        required = True
    )

    @jwt_required()
    def post(self, symbol):
        data = self.parser.parse_args()
        email = data['email']
        mail = get_jwt_identity()
        if mail!=email:
            return {'error':"Invalid token"}, 401
        if symbol not in all_symbols:
            return {
                'error':"Invalid symbol"
            }, 400
        result = Watchlist.add_symbol(email,symbol)
        if result == 1:
            return {'message':'symbol added to watchlist'}, 201
        elif result == 2:
            return {'message': 'symbol already exist in watchlist'}, 409
        elif result == -1:
            return {'error':'some error while adding symbol to watchlist occurred'}

class remove_symbol_from_watchlist(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type = str,
        required = True
    )

    @jwt_required()
    def delete(self,symbol):
        data = self.parser.parse_args()
        email = data['email']
        mail = get_jwt_identity()
        if mail!=email:
            return {'error':"Invalid token"}, 401

        result = Watchlist.remove_symbol(email,symbol)
        if result == 1:
            return {'message':'symbol removed from watchlist'}, 201
        elif result == 2:
            return {'message': 'symbol doesnt exist in watchlist'}, 404
        elif result == -1:
            return {'error':'some error while removing symbol from watchlist occurred'}


