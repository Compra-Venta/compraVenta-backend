from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from models.User import User

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

    parser.add_argument('balance',
                        type = float,
                        required = True
                        )
    def post(self):
        data = self.parser.parse_args()
        email = data['email']
        password = data['password']
        name = data['name']
        age = data['age']
        country = data['country']
        balance = data['balance']
        _user, _id = User.find_by_email(email)
        if _user == None:
            user = User(email,password, name, age, country, balance)
            if user.insert():
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
            return {"message": "Email id not found"}, 404
        else:
            if result.password != password:
                return {"message": "invalid credentials"}, 401 
            else:
                access_token = create_access_token(identity = _id,fresh = True)
                refresh_token = create_refresh_token(_id)
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
        new_password = data['new_password']
        password = data['password']
        user, _id = User.find_by_email(email)
        if(user == None):
            return {"error":"User does not exists"}, 400
        if user.password != password:
            return {"error": "Invalid credentials"}, 400
        try:
            done = user.update_password(new_password, _id)
            if done:
                return {"message": "Password changed successfully."}, 200
            else:
                return {"error": "Some error occured"}, 500
        except:
            return {"error": "Some error occured"}, 500