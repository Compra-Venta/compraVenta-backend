import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class User:
        def __init__(self,email, password, name, age, country, balance):
                self.email = email
                self.password = password 
                self.name = name
                self.age = age 
                self.country = country
                self.balance = balance
        
        @classmethod
        def find_by_email(cls, email):
                #method to return a User object on None querying from database
                client = MongoClient('localhost', 27017)
                db = client['test-user-db-compra-venta']
                collection = db['test-user-collection']

                result = collection.find_one({'email': email})
                client.close()
                if result:
                        return cls(result['email'], result['password'], result['name'], result['age'], result['country'], result['balance']), str(result['_id'])
                else:
                        return None, None

        
        def insert(self):
                #method to insert in the database
                client = MongoClient('localhost', 27017)
                db = client['test-user-db-compra-venta']
                collection = db['test-user-collection']

                post = {
                        "email": self.email,
                        "password": self.password,
                        "name": self.name,
                        "age": self.age,
                        "country": self.country,
                        "balance": self.balance
                }

                try:
                        if collection.insert_one(post) == None:
                                client.close()
                                return False
                        else:
                                client.close()
                                return True
                except:
                        client.close()
                        return False

        def update_password(self, new_password, _id):

                client = MongoClient('localhost', 27017)
                db = client['test-user-db-compra-venta']
                collection = db['test-user-collection']

                myquery = {"email": self.email}

                new_values = {"$set": {"password": new_password}}
                try: 
                        collection.update_one(myquery, new_values)       
                        client.close()
                        return True
                except:
                        client.close()
                        return False
                

