from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.Wallet_model import Wallet
<<<<<<< HEAD
from flask_jwt_extended import jwt_required, get_jwt_identity

all_coins = {'BTC','ETH','LTC','BNB','USDT','XRP'}
=======

>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173

class get_wallet(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',type=str,required=True)
<<<<<<< HEAD

	@jwt_required()
	def get(self):
		data=self.parser.parse_args()
		email=data['email']
		mail = get_jwt_identity()
		if mail!=email:
			return {'error':"Invalid token"}, 401

		wallet, code = Wallet.get_wallet(email)
		if wallet is None:
			return {"error":"User doesn't exist"}, 400
		else:
			return {
				'email':wallet.email,
				'balance': wallet.balance,
				'fixed_balance': wallet.fixed_balance
			}, 200
=======
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
>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173


class get_wallet_currency(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',type=str,required=True)
<<<<<<< HEAD
	
	@jwt_required()
	def get(self, coin):
		data=self.parser.parse_args()
		email=data['email']

		mail = get_jwt_identity()
		if mail!=email:
			return {'error':"Invalid token"}, 401

		if coin not in all_coins:
			return {
				'error':"Invalid coin"
			}, 400
		balance, fixed_balance, code = Wallet.get_wallet_currency(email, coin)
		if balance is None:
			return {"error":"User doesn't exist"},404
		else:
			return {
				'coin': coin,
				'balance': balance,
				'fixed_balance': fixed_balance

			}, 200
=======
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

>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173
