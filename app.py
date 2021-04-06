from flask import Flask 
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from models.User import User
from resources.User import RegisterUser, UserLogin, RefreshLogin, UpdatePassword, ForgotPassword
from resources.Prediction import Predict
from threading import Thread 
import urllib.request
import time

data = None

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "somesecretcode"
jwt = JWTManager(app)
api = Api(app)

class Pnomics(Thread):
    def run(self):
        i=0
        while(i!=500):
            global data
            url = "https://api.nomics.com/v1/currencies/ticker?key=9e4daddd8f3bf33f45eeba5fe9021b2f&ids=BTC,ETH&interval=1d,30d&convert=USD&per-page=100&page=1"
            try:
                data = eval(urllib.request.urlopen(url).read())
            except:
                pass
            i+=1
            time.sleep(10)


# t1 = Pnomics()
# t1.start()

class Exchange(Resource):
    
    @jwt_required()
    def get(self):
        return data


class Item(Resource):

    @jwt_required()
    def get(self):
        return {'name': 'daksh'}

api.add_resource(RegisterUser, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(RefreshLogin, '/reauth')
api.add_resource(Item, '/item')
api.add_resource(UpdatePassword, '/password/change')
api.add_resource(Predict,'/predict')
api.add_resource(ForgotPassword,'/password/get_new')
if __name__ == '__main__':
    app.run(debug = True)

