from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.Wallet_model import Wallet


class get_wallet(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',type=str,required=True)
	def get(self):
		data=self.parser.parse_arge()
		email=data['email']
		wallet,_id=Wallet1.get_wallet(email)
		if wallet is None:
			return {"error","Wallet of this user doesn't exist"},400
		else:
			return {

				'email':wallet.email,
				'balance':wallet.balance,
				'fixed_balance':wallet.fixed_balance
			},200


class get_wallet_currency(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',type=str,required=True)
	parser.add_argument('coin',type=str,required=True)
	
	def get(self):
		data=self.parser.parse_arge()
		email=data['email']
		coin=data['coin']
		currency,_id=Wallet1.get_wallet(email)
		if currency is None:
			return {"error","Wallet of this user doesn't exist"},400
		else:
			return {

				'email':currency.email,
				'currency':currency.balance.coin
			},200

