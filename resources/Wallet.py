from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from models.Wallet import Wallet



class Wallet_resource(Resource):

	parser=reqparse.RequestParser()
	parser.add_argument('email',
						type=str,
						required=True
						)

"""	parser.add_argument('password',
						type=str,
						required=True
						)
"""


	

	@jwt_required()
	def get(self):

		data=self.parser.parse_args()
		email=data['email']
		ans,_id=Wallet.find_by_email(email)
		if ans ==None:
			return {'error':'Email id not valid'},404
		else:
			return{

				'wallet':ans
			}

class Wallet_currency(Resource):

	parser=reqparse.RequestParser()
	parser.add_argument('email',
					type=str,
					required=True
					)
	parser.add_argument('currency',
					type=str,
					required=True
					)


	@jwt_required()
	def get(self):
		data=self.parser.parse_args()
		email=data['email']
		currency=data['currency']
		ans=Wallet.find_by_email_and_cryptocurrency(email,currency)
		if ans ==None:
			return {
				'error':'Email not valid'
			},404
		else:

			return{
				'amount':ans
			}

