import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class TransactionClosed:
    def __init__(self):
        pass

    @classmethod
    def create_transaction_history(cls,email):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']
        post = {
            'email':email,
            'transaction_list' : []
        }
        try:
            collection.insert_one(post)
        except:
            pass 

        if(collection.find_one({'email':email}) == None):
            client.close()
            return False
        
        client.close()
        return True

    @classmethod
    def insert(self, email, pair, q_amount, b_amount, date, time, order_type, side):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']

        transaction_element = {
            'pair' : pair,
            'q_amount' : q_amount,
            'b_amount' : b_amount,
            'date' : date,
            'time' : time,
            'order_type' : order_type,
            'side' : side
        }
        try:
            result = collection.update_one({'email':email},{'$push':{'transaction_list':transaction_element}})
            client.close()
            return result.modified_one > 0
        except:
            client.close()
            return False 
        


    @classmethod
    def get_all_transactions(cls, email):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']
        result = None
        try:
            result = collection.find_one({'email':email})
            client.close()
        except:
            client.close()
            pass

        if result != None:  
            return list(result['transaction_list'])
        else:
            return None

    @classmethod
    def get_transactions_by_date(cls,email, date):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']
        result = None

        try:
            result = collection.find_one({'email':email})
            if result == None:
                return None
            transaction_list = list(result['transaction_list'])
            client.close()
            found = False
            start = -1
            end = -1
            for i,d in enumerate(transaction_list):
                if found:
                    if d['date'] > date:
                        end = i
                        break
                else:
                    if d['date'] == date:
                        found = True
                        start = i
            if found and start > 0:
                return transaction_list[start:end]
            else:
                return []
                
        except:
            client.close()
            return None

    @classmethod
    def get_transactions_by_symbol(cls,email, symbol):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']
        result = None

        try:
            result = collection.find_one({'email':email})
            if result == None:
                return None
            transaction_list = list(result['transaction_list'])
            client.close()
            ans = []
            for d in transaction_list:
                if d['pair'] == symbol:
                    ans.append(d)
            return ans
                
        except:
            client.close()
            return None

    @classmethod
    def reset_account(cls,email):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']
        try:
            result = collection.update_one({'email':email},{'$set',{'transaction_list':[]}})
            client.close()
            return result.matched_count > 0
        except:
            return False





        
    


