import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from models.Wallet_model import Wallet

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
    def insert_market(cls, email, base, quote, b_amount, date, time, order_type, side):
        price = 1 #getLivePrice(base+quote)
        if side == 'BUY':
            q_amount = price*b_amount
            if Wallet.check_balance(email, quote, q_amount):
                Wallet.decrease_balance_currency_amt(email, quote, q_amount)
                Wallet.increase_balance_currency_amt(email, base, b_amount)
                id_ = TransactionClosed.insert(email, base, quote, b_amount, date, time, order_type, side, price)
                return id_, "Order placed successfully"
            else:
                return None, 'Not enough balance' 
        else:
            if Wallet.check_balance(email, base, b_amount):
                q_amount = price*b_amount
                Wallet.decrease_balance_currency_amt(email, base, b_amount)
                Wallet.increase_balance_currency_amt(email, quote, q_amount)
                id_ = TransactionClosed.insert(email, base, quote, b_amount, date, time, order_type, side, price)
                return id_, "Order placed successfully"
            else:
                return None, 'Not enough balance'
    

    @classmethod
    def insert(cls, email, base, quote, b_amount, date, time, order_type, side, price):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']

        id_ = '12dasgfdg'
        transaction_element = {
            'order_id':id_,
            'base' : base,
            'quote':quote,
            'b_amount' : b_amount,
            'price': price,
            'date' : date,
            'time' : time,
            'order_type' : order_type,
            'side' : side
        }

        try:
            collection.update_one({'email':email},{'$push':{'transaction_list':transaction_element}})
            client.close()
            return id_
        except:
            client.close()
            return None 
        


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
                if d['base'] == symbol or d['quote']==symbol:
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
            result = collection.update_one({'email':email}, {'$set',{'transaction_list':[]}})
            client.close()
            return result.matched_count > 0
        except:
            return False





        
    


