import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class Wallet:
    def __init__(self,email,balance_data):
        self.email = email
        self.balance_data = balance_data
    
    def insert(self):
        email = self.email
        balance_data = self.balance_data

        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection_wallet = db['test-wallet-collection']
        post = {
            "email": email,
            "balance_data" : balance_data
        }
        try:
            collection_wallet.insert_one(post)
            return True
        except:
            return False

    @classmethod
    def find_by_email(cls,email):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection_wallet = db['test-wallet-collection']

        result = collection_wallet.find_one({"email":email})
        if result != None:
            # result is dict
            return cls(result['email'],result['balance_data']), result['_id']
        else:
            return None, None

    @classmethod
    def find_by_email_and_currency(cls,email,currency):

        return result['balance_data'].get(currency, None)

    @classmethod
    def reset_wallet(cls,email):
        new_balance_data = {
            "USD":1000000.000000
        }
        collection_wallet.update({'email':email},{"$set":{"balance_data":new_balance_data}})

    @classmethod
    def transaction(cls,base_asset, quote_asset, )



# 5BTC 
# 20LTC 


#################################################

# {
#     "email":"dfj;dlf@fdlkf",
#     "balance_data":{
#         "USD": 10000000.0000000
#     }
# }

# wallet_obj = Wallet(email,balance_data)

# wallet_obj.insert()

# {
#     "email" : "dakdhf@dfdk"
# }

# find_by_email(email)
