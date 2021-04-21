from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from utils.encryption import key, encrypt_password, decrypt_password
from models.User import User
from models.Watchlist import Watchlist 
from models.Wallet_model import Wallet
from models.TransactionClosed import TransactionClosed
from models.TransactionOpen import TransactionOpen
from utils.recovery_email import send_recovery_email
from utils.password_generator import generate_password
from utils.blacklist import BLACKLIST
from flask_jwt_extended import get_jwt
from flask_jwt_extended import JWTManager
from utils import blocklist
from datetime import timedelta


ACCESS_EXPIRES = timedelta(hours=1)

class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type = str,
                        required = True
                        )

    parser.add_argument('password',
                        type = str,
                        required = True
                        )
    parser.add_argument('name',
                        type = str,
                        required = True
                        )

    parser.add_argument('age',
                        type = int,
                        required = True
                        )

    parser.add_argument('country',
                        type = str,
                        required = True
                        )

    parser.add_argument('PhoneNo',
                        type = int,
                        required = True
                        )
    def post(self):
        data = self.parser.parse_args()
        email = data['email']
        password = encrypt_password(data['password'])
        name = data['name']
        age = data['age']
        country = data['country']
        balance = data['PhoneNo']
        _user, _id = User.find_by_email(email)
        if _user == None:
            user = User(email,password, name, age, country, balance)
            if user.insert():
                Watchlist.create_user_watchlist(email)
                Wallet.make_user_wallet(email)
                TransactionClosed.create_transaction_history(email)
                TransactionOpen.create_open_transaction_history(email)
                return {"message": "registered successfully"}, 200
            else:
                return {"message": "an error occurred"}, 500
        else:
            return {"message": "Email ID already registered"}, 409


class UserLogin(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type = str,
                        required = True
                        )

    parser.add_argument('password',
                        type = str,
                        required = True
                        )

    def post(self):
        data = self.parser.parse_args()
        email = data['email']
        password = data['password']
        result, _id = User.find_by_email(email)
        if  result == None:
            return {"error": "Email id not found"}, 404
        else:
            if decrypt_password(result.password) != password:
                return {"error": "invalid credentials"}, 401 
            else:
                access_token = create_access_token(identity = result.email,fresh = True)
                refresh_token = create_refresh_token(result.email)
                return {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }, 200
        

class RefreshLogin(Resource):
    @jwt_required(refresh = True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity = current_user, fresh = False)
        return {'access_token':new_token}, 200

class UpdatePassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type = str,
                        required = True
                        )
    parser.add_argument('password',
                        type = str,
                        required = True
                        )

    parser.add_argument('new_password',
                        type = str,
                        required = True
                        )
    @jwt_required()
    def post(self):
        data = self.parser.parse_args()
        email = data['email']

        mail = get_jwt_identity()
        if mail!=email:
            return {"error":"Invalid token"}, 401

        new_password = encrypt_password(data['new_password'])
        password = (data['password'])
        user, _id = User.find_by_email(email)

        if(user == None):
            return {"error":"User does not exists"}, 404
        if decrypt_password(user.password) != password:
            return {"error": "Invalid credentials"}, 401
        try:
            done = user.update_password(new_password, _id)
            if done:
                return {"message": "Password changed successfully."}, 200
            else:
                return {"error": "Some error occured"}, 500
        except:
            return {"error": "Some error occured"}, 500

class ForgotPassword(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type = str,
                        required = True
                        )

    def put(self):
        data = self.parser.parse_args()
        email = data['email']
        new_password = generate_password()
        encrypted_pass = encrypt_password(new_password)
        user, _id = User.find_by_email(email)
        if(user == None):
            return {"error":"User does not exists"}, 404
        try:
            done = user.update_password(encrypted_pass, _id)
            if done:
                send_recovery_email(email, user.name, new_password)
                return {"message": "Password changed successfully."}, 200
            else:
                return {"error": "Some error occured"}, 500
        except:
            return {"error": "Some error occured"}, 500


class Profile(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type = str,
                        required = True
                        )
    @jwt_required()
    def get(self):
        data = self.parser.parse_args()
        email = data['email']
        mail = get_jwt_identity()
        if mail!=email:
            return {"error":"Invalid token"}, 401

        user, _id = User.find_by_email(email)
        if(user == None):
            return {"error":"User does not exists"}, 404
        else:
            return {
            	"user_id":_id,
                "email":user.email,
                "name":user.name,
                "age":user.age,
                "country":user.country,
                "PhoneNo":user.PhoneNo
            }, 200


class UserLogout(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',
						type=str,
						required=True
						)
	@jwt_required()
	def post(self):
        	data = self.parser.parse_args()
        	email = data['email']
        	mail = get_jwt_identity()
        	if mail!=email: return {"error":"Invalid token"}, 401;
        	jti = get_jwt()['jti']
        	blocklist.jwt_redis_blocklist.set(jti, "", ex = ACCESS_EXPIRES)
        	return {"msg":"Access token revoked"}, 200
		 
		 

