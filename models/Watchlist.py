import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class Watchlist():

    @classmethod 
    def reset_account(cls,email):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-watchlist-collection']
        try:
            collection.update_one({'email':email},{'$set':{'watchlist':[]}})
            client.close()
            return 1
        except:
            client.close()
            return -1

    @classmethod
    def create_user_watchlist(cls,email):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-watchlist-collection']

        post = {
            'email':email,
            'watchlist':[]
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


    @classmethod
    def add_symbol(cls,email,symbol):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-watchlist-collection']
        try:
        	result = collection.find_one({'email':email})
        except:
        	return -1
        	
        if result is None:
        	return -1
        	
        wl = list(result['watchlist'])
        if symbol not in wl:
        	try:
        		collection.update_one({'email':email},{'$push':{'watchlist':symbol}})
        		client.close()
        		return 1
        	except:
        		client.close()
        		return -1
        else:
            client.close()
            return 2

    @classmethod
    def remove_symbol(cls, email, symbol):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-watchlist-collection']
        try:

        	result = collection.find_one({'email':email})
        except:
        	return -1

        if result is None:
        	return -1
        
        wl = list(result['watchlist'])
        if symbol in wl:
            try:
                collection.update_one({'email':email},{'$pull':{'watchlist':symbol}})
                client.close()
                return 1
            except:
                client.close()
                return -1
        else:
            client.close()
            return 2

    @classmethod
    def get_all_symbol(cls, email):
        try:
            client = MongoClient('localhost', 27017)
            db = client['test-user-db-compra-venta']
            collection = db['test-watchlist-collection']

            result = collection.find_one({'email':email})
            wl = list(result['watchlist'])
            return wl
        except:
            return None
