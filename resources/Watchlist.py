from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from models.Watchlist import Watchlist

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
    parser.add_argument(
        'symbol',
        type = str,
        required = True
    )

    @jwt_required()
    def post(self):
        data = self.parser.parse_args()
        email = data['email']
        symbol = data['symbol']
        result = Watchlist.add_symbol(email,symbol)
        if result == 1:
            return {'message':'symbol added to watchlist'}, 201
        elif result == 2:
            return {'message': 'symbol already exist in watchlist'}, 400
        elif result == -1:
            return {'error':'some error while adding symbol to watchlist occurred'}

class remove_symbol_from_watchlist(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type = str,
        required = True
    )
    parser.add_argument(
        'symbol',
        type = str,
        required = True
    )

    @jwt_required()
    def delete(self):
        data = self.parser.parse_args()
        email = data['email']
        symbol = data['symbol']
        result = Watchlist.remove_symbol(email,symbol)
        if result == 1:
            return {'message':'symbol removed from watchlist'}, 201
        elif result == 2:
            return {'message': 'symbol doesnt exist in watchlist'}, 400
        elif result == -1:
            return {'error':'some error while removing symbol from watchlist occurred'}


