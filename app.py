from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from models.User import User
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "somesecretcode"
jwt = JWTManager(app)
api = Api(app)

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


class Item(Resource):

    @jwt_required()
    def get(self):
        return {'name': 'daksh'}

api.add_resource(RegisterUser, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(RefreshLogin, '/reauth')
api.add_resource(Item, '/item')

if __name__ == '__main__':
    app.run(debug = True)
