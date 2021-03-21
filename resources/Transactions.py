from flask import Flask 
from flask_restful import Resource, Api, reqparse, request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from models.User import User
from models.TransactionClosed import TransactionClosed


def is_transaction_possible(email,pair,order_type,side, q_amount, b_amount):
    return True

class TransactionList(Resource):

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
        transaction_list = TransactionClosed.get_all_transactions(email)
        if transaction_list:
            return {"transactions":transaction_list}, 200
        else:
            return {"error":"cant find the user"}, 400 
    

class TransactionByDate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type = str,
        required = True
    )

    @jwt_required()
    def get(self):
        d = self.parser.parse_args()
        email = d['email']
        data = request.args
        date = data['date']
        transaction_list = TransactionClosed.get_transactions_by_date(email,date)
        if transaction_list:
            return {'transactions':transaction_list}, 200
        else:
            return {'error':'some error'}, 400


class TransactionBySymbol(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type = str,
        required = True
    )
    
    @jwt_required()
    def get(self):
        d = self.parser.parse_args()
        email = d['email']
        data = request.args
        symbol = data['symbol']
        transaction_list = TransactionClosed.get_transactions_by_symbol(email,symbol)
        if transaction_list:
            return {'transactions':transaction_list}, 200
        else:
            return {'error':'some error'}, 400


class AddTransaction(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'email',
        type = str,
        required = True
    )
    parser.add_argument(
        'pair',
        type = str,
        required = True
    )
    parser.add_argument(
        'date',
        type = str,
        required = True
    )
    parser.add_argument(
        'time',
        type = str,
        required = True
    )
    parser.add_argument(
        'order_type',
        type = str,
        required = True
    )
    parser.add_argument(
        'side',
        type = str,
        required = True
    )
    parser.add_argument(
        'q_amount',
        type = float,
        required = True
    )
    parser.add_argument(
        'b_amount',
        type = float,
        required = True
    )

    @jwt_required()
    def post(self):
        data = self.parser.parse_args()
        email = data['email']
        pair = data['pair']
        date = data['date']
        time = data['time']
        order_type = data['time']
        side = data['side']
        q_amount = data['q_amount']
        b_amount = data['b_amount']

        if is_transaction_possible(email,pair,order_type,side, q_amount, b_amount):
            if Wallet.do_transaction(email,pair,order_type,side, q_amount, b_amount):
                if TransactionClosed.insert(email,pair,q_amount, b_amount, date,time, order_type, side):
                    return {"message":"transaction successful"}, 201
                else:
                    pass # write code to reverse wallet changes
            else:
                return {"error":"Internal Server Error"}, 500
        else:
            return {"error": "transaction failed"}, 400
