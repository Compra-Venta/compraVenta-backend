from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.TransactionClosed import TransactionClosed

class MarketOrder(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',
		type=str,
		required=True)
	parser.add_argument('base',
		type=str,
		required=True)
	parser.add_argument('quote',
		type=str,
		required=True)
	parser.add_argument('b_amount',
		type=float,
		required=True)
	parser.add_argument('date',
		type=str,
		required=True)
	parser.add_argument('time',
		type=str,
		required=True)
	parser.add_argument('side',
		type=str,
		required=True)

	def post(self):
		data=self.parser.parse_args()
		email = data['email']
		base=data['base']
		quote=data['quote']
		b_amount=data['b_amount']
		date=data['date']
		time=data['time']
		order_type=str('M')
		side=data['side']

		# id_ ="daksh"
		# msg = "temp id"
		id_, msg = TransactionClosed.insert_market(email,base,quote,b_amount,date,time,order_type,side)
		if id_:
			return {'status':'successful', 'order_id':id_}, 200
		else:
			return {'status':'failed', 'msg':msg},500




class get_all_transactions(Resource):

	parser=reqparse.RequestParser()
	parser.add_argument('email',
		type=str,
		required=True)

	def get(self):
		data=self.parser.parse_args()
		email=data['email']
		transactions= TransactionClosed.get_all_transactions(email)
		if transactions is None:
			return {'error':'Transaction does not exists'},400
			
		else:
			return {'transactions':transactions},200
			

class get_all_transactions_by_symbol(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',
		type=str,
		required=True)

	def get(self, coin):
		data=self.parser.parse_args()
		email=data['email']
		transactions=TransactionClosed.get_transactions_by_symbol(email,coin)
		if transactions is None:
			return {'error':'Transaction does not exists'}, 400
		else:
			return {'transactions':transactions}, 200


