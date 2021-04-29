import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from models.Wallet_model import Wallet
from utils.UniqueString import generate_unique_string
from utils.config import db_url
class TransactionClosed:
    def __init__(self):
        pass

    @classmethod
    def create_transaction_history(cls,email):
        client = MongoClient(db_url)
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
        from utils.StoplossThreads import client
        price = None
        try:
            info = client.get_symbol_ticker(symbol = (base+quote))
            price = round(float(info['price']),8)
        except:
            return None, "Internal server error."

        if price is None:
            return None, "Internal server error."
            
        if side == 'BUY':
            q_amount = round(price*b_amount,8)
            if Wallet.check_balance(email, quote, q_amount):
                # Wallet.decrease_balance_currency_amt(email, quote, q_amount)
                # Wallet.increase_balance_currency_amt(email, base, b_amount)
                Wallet.do_wallet_updation(email, base, quote, b_amount, -q_amount,'balance', 'balance')
                id_ = TransactionClosed.insert(email, base, quote, b_amount, date, time, order_type, side, price)
                return id_, "Order placed successfully"
            else:
                return None, 'Not enough balance' 
        else:
            if Wallet.check_balance(email, base, b_amount):
                q_amount = round(price*b_amount,8)
                # Wallet.decrease_balance_currency_amt(email, base, b_amount)
                # Wallet.increase_balance_currency_amt(email, quote, q_amount)
                Wallet.do_wallet_updation(email, base, quote, -b_amount, q_amount,'balance', 'balance')
                id_ = TransactionClosed.insert(email, base, quote, b_amount, date, time, order_type, side, price)
                return id_, "Order placed successfully"
            else:
                return None, 'Not enough balance'
    

    @classmethod
    def insert(cls, email, base, quote, b_amount, date, time, order_type, side, price):
        client = MongoClient(db_url)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']

        id_ = generate_unique_string(email)
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
        client = MongoClient(db_url)
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
        client = MongoClient(db_url)
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
        client = MongoClient(db_url)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-closed-collection']
        try:
            collection.update_one({'email':email}, {'$set':{'transaction_list':[]}})
            client.close()
            return True
        except:
        	client.close()
        	return False





        
    
