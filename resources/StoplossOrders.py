from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required
from models.TransactionOpen import TransactionOpen

class StoplossOrder(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(
			'email',
			type = str,
			required = True
		)
	parser.add_argument(
			'base',
			type = str,
			required = True
		)
	parser.add_argument(
			'quote',
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
			'side',
			type = str,
			required = True
		)
	parser.add_argument(
			'b_amount',
			type = float,
			required = True
		)
	parser.add_argument(
			'stop',
			type = float,
			required = True
		)

	parser_del = reqparse.RequestParser()
	parser_del.add_argument(
			'email',
			required =True,
			type = str
		)

	parser_del.add_argument(
			'order_id',
			required =True,
			type = str
		)

	parser_update = reqparse.RequestParser()
	parser_update.add_argument(
			'email',
			type = str,
			required = True
		)
	parser_update.add_argument(
			'base',
			type = str,
			required = True
		)
	parser_update.add_argument(
			'quote',
			type = str,
			required = True
		)
	parser_update.add_argument(
			'date',
			type = str,
			required = True
		)
	parser_update.add_argument(
			'time',
			type = str,
			required = True
		)
	parser_update.add_argument(
			'side',
			type = str,
			required = True
		)
	parser_update.add_argument(
			'b_amount',
			type = float,
			required = True
		)
	parser_update.add_argument(
			'stop',
			type = float,
			required = True
		)
	parser_update.add_argument(
			'order_id',
			type = str,
			required = True
		)

	def post(self):
		data = self.parser.parse_args()
		email = data['email']
		base = data['base']
		quote = data['quote']
		date = data['date']
		time = data['time']
		order_type = 'SL'
		side = data['side']
		b_amount = data['b_amount']
		stop = data['stop']

		curr_price = None
		from utils.StoplossThreads import client
		info = client.get_symbol_ticker(symbol = (base+quote))
		curr_price = float(info['price'])
		
		if curr_price is None:
			return {
				'error': "internal server error"
			}, 500
		if side == 'BUY':
			if curr_price <= stop:
				order_type = 'SL'
			else:
				order_type = 'TP'
		else:
			if curr_price < stop:
				order_type = 'TP'
			else:
				order_type = 'SL'

		id_, msg = TransactionOpen.insert_stoploss(email, base, quote, b_amount, date, time, order_type, side, stop)
		if id_ is not None:
			return {
				'status':'successful',
				'order_id': id_
				}, 201
		else:
			return {
				'status':'failed',
				'message': msg
			}, 406

	def put(self):
		data = self.parser_update.parse_args()
		email = data['email']
		base = data['base']
		quote = data['quote']
		date = data['date']
		time = data['time']
		order_type = 'SL'
		side = data['side']
		b_amount = data['b_amount']
		stop = data['stop']
		id_ = data['order_id']
		done, msg = TransactionOpen.delete(email, id_)
		if done:
			
			d, m = TransactionOpen.insert(email, base, quote, b_amount, date, time, order_type, side, stop)
			if d:
				return {
					'status': 'successful',
					'message': 'Order updated successfully.'
				}, 200
			else:
				return {
					'status':'failed',
					'message':'Some internal error occurred.'
				}
		else:
			return {
				'status':'failed',
				'message': 'Not able to update the order'
			}, 406

		if done:
			return {
				'status':'successful',
				'message': msg
			}, 201
		else:
			return {
				'status':'failed',
				'message': msg
			}, 400



	def delete(self):
		data = self.parser_del.parse_args()
		email = data['email']
		id_ = data['order_id']

		done, msg = TransactionOpen.delete(email, id_)

		if done:
			return {
				'status':'successful',
				'message':msg
			}, 200
		else:
			return {
				'status': 'failed',
				'message': msg
			}, 400


class GetOpenOrders(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument(
			'email',
			type = str,
			required = True
		)

	def get(self):
		data = self.parser.parse_args()
		email = data['email']
		orders, msg = TransactionOpen.get_all_open_transactions(email)
		if orders is not None:
			return {
				'open': orders
			}, 200	
		else:
			return {
				'error': msg
			}, 400

