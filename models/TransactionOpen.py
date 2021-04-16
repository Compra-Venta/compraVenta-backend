import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from models.Wallet_model import Wallet
from models.OrderStoploss import OrderSL

class TransactionOpen:
    def __init__(self):
        pass

    @classmethod
    def create_open_transaction_history(cls,email):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-open-collection']
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
    def insert_stoploss(cls, email, base, quote, b_amount, date, time, order_type, side, stop):
        price = stop
        if side == 'BUY':
            q_amount = price * b_amount
            if Wallet.check_balance(email, quote, q_amount):
                # Wallet.decrease_balance_currency_amt(email, quote, q_amount)
                # Wallet.increase_fixed_balance_currency_amt(email, quote, q_amount)
                Wallet.do_wallet_updation(email, quote, quote, -q_amount, q_amount, 'balance', 'fixed_balance')
                id_ = TransactionOpen.insert(email, base, quote, b_amount, date, time, order_type, side, price)
                return id_, "Order placed successfully"
            else:
                return None, 'Not enough balance' 
        else:
            if Wallet.check_balance(email, base, b_amount):
                q_amount = price*b_amount
                # Wallet.decrease_balance_currency_amt(email, base, b_amount)
                # Wallet.increase_fixed_balance_currency_amt(email, base, b_amount)
                Wallet.do_wallet_updation(email, base, base, -b_amount, b_amount, 'balance', 'fixed_balance')
                id_ = TransactionOpen.insert(email, base, quote, b_amount, date, time, order_type, side, price)
                return id_, "Order placed successfully"
            else:
                return None, 'Not enough balance'
    
    @classmethod
    def insert(cls, email, base, quote, b_amount, date, time, order_type, side, price, id_ = 'default-thread'):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-open-collection']
        order = OrderSL(email, base, quote, date, time, order_type, side, b_amount, price)
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
            from utils.StoplossThreads import startStoplossThread
            collection.update_one({'email':email},{'$push':{'transaction_list':transaction_element}})
            startStoplossThread(order, id_)
            client.close()
            return id_
        except:
            client.close()
            return None 
        
    @classmethod
    def update(cls, email, base, quote, b_amount, date, time, order_type, side, price, id_):
        pass

    @classmethod
    def delete(cls, email, id_, completed = False):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-open-collection']
        try:
            if not completed:
                from utils.StoplossThreads import stopStoplossThread
                stopStoplossThread(id_)
            collection.update_one({'email':email},{'$pull':{'transaction_list':{'order_id':id_}}})
            client.close()
            return True, f"Stoploss order with order id {id_} cancelled."
        except:
            client.close()
            return False, "Not able to delete the order"

    @classmethod
    def get_all_open_transactions(cls, email):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-open-collection']
        result = None
        try:
            result = collection.find_one({'email':email})
            client.close()
        except Exception as e:
            client.close()
            msg = str(e)

        if result is not None:  
            return result['transaction_list'], "successfully retrieved all transactions"
        else:
            return None, msg


    @classmethod
    def get_transactions_by_symbol(cls,email, symbol):
        client = MongoClient('localhost', 27017)
        db = client['test-user-db-compra-venta']
        collection = db['test-transaction-open-collection']
        result = None

        try:
            result = collection.find_one({'email':email})
            if result == None:
                return None
            transaction_list = result['transaction_list']
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
        collection = db['test-transaction-open-collection']
        # close all running thread
        try:
            result = collection.update_one({'email':email}, {'$set',{'transaction_list':[]}})
            client.close()
            return result.matched_count > 0
        except:
            return False





        
    


