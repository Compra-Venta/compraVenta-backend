from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.TransactionClosed import TransactionClosed

class PlaceOrder(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',
		type=str,
		required=True)
	parser.add_argument('pair',
		type=str,
		required=True)
	parser.add_argument('b_amount',
		type=str,
		required=True)
	parser.add_argument('q_amount',
		type=str,
		required=True)
	parser.add_argument('date',
		type=str,
		required=True)
	parser.add_argument('time',
		type=str,
		required=True)
	parser.add_argument('order_type',
		type=str,
		required=True)
	parser.add_argument('side',
		type=str,
		required=True)

	def post(self):
		data=self.parser.parse_arge()
		pair=data['pair']
		b_amount=data['b_amount']
		q_amount=data['q_amount']
		date=data['date']
		time=data['time']
		order_type=data['order_type']
		side=data['side']

		transaction_record=TransactionClosed()
		if transaction_record.insert(email,pair,q_amount,b_amount,date,time,order_tupe,side):
			return {'message':'Transaction detail added successfully'},200
		else:
			return {'message':'Some error occured'},404




class get_all_transactions(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',
		type=str,
		required=True)

	def get(self):
		data=self.parser.parse_arge()
		email=data['email']
		get_trans=TransactionClosed()
		if get_trans.get_all_transactions(email):
			return {

				'all transactions':get_trans.transaction_list
			}
		else:
			return {'message':'error occured'}


class get_all_transactions_by_date(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',
		type=str,
		required=True)
	parser.add_argument('date',
		type=str,
		required=True)

	def get(self):
		data=self.parser.parse_arge()
		email=data['email']
		date=data['date']
		get_trans=TransactionClosed()
		if get_trans.get_all_transactions_by_date(email,date):
			return {

				'all transactions':get_trans.transaction_list
			}
		else:
			return {'message':'error occured'}



class get_all_transactions_by_symbol(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',
		type=str,
		required=True)
	parser.add_argument('symbol',
		type=str,
		required=True)

	def get(self):
		data=self.parser.parse_arge()
		email=data['email']
		symbol=data['symbol']
		get_trans=TransactionClosed()
		if get_trans.get_all_transactions_by_symbol(email,symbol):
			return {

				'all transactions':get_trans.transaction_list
			}
		else:
			return {'message':'error occured'}


