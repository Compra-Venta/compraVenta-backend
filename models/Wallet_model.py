import pymongo
from pymongo import MongoClient
#from bson.objectid import objectid

class Wallet:

	def __init__(self,email,balance,fixed_balance):

		self.email=email
		self.balance=balance
		self.fixed_balance=fixed_balance


	@classmethod
	def check_balance(self,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
		collection=db['test-user-wallet']

		result=collection.find_one({'email':email})
		client.close()
		if result is not none:
			bal=result['balance']
			currency_amt=bal['coin']
			if currency_amt >= amount:
				# true
				return True
			else:
				return False
		else:
			return False


	@classmethod
	def increase_balance_currency_amt(self,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
		collection=db['test-user-wallet']


		result=collection.find_one({'email':email})
		client.close()
		try:
			if result is not none:
				bal=result['balance']
				bal[coin]+=amount
				return True
			else:
				return False
		except:
			return False


	@classmethod
	def decrease_balance_currency_amt(self,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
		collection=db['test-user-wallet']


		result=collection.find_one({'email':email})
		client.close()
		if result is not none:
			bal=result['balance']
			bal[coin]-=amount
			return True
		else:
			return False

	
	@classmethod
	def reset_account(self,email):
        
		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
		collection=db['test-user-wallet']

		my_query={'email':email}

		new_value={

		'$set':{
		'balance':{
        "BTC":0.00000000,
        "ETH":0.00000000,
        "LTC":0.00000000,
        "XRP":0.00000000,
        "BNB":0.00000000,
        "USDT":50000.00000000
    	},

    	'fixed_balance':{
        "BTC":0.00000000,
        "ETH":0.00000000,
        "LTC":0.00000000,
        "XRP":0.00000000,
        "BNB":0.00000000,
        "USDT":0.00000000
    	}


    }

 }
 		
		try:
 			collection.update_one(my_query,new_value)
 			collection.update_one(my_query,new_fixed_value)
 			client.close()
 			return True
		except:
 			client.close()
 			return False


	@classmethod
	def make_user_wallet(self,email):


		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
		collection=db['test-user-wallet']

		post={

    "email":email,
    "balance":{
        "BTC":0.00000000,
        "ETH":0.00000000,
        "LTC":0.00000000,
        "XRP":0.00000000,
        "BNB":0.00000000,
        "USDT":50000.00000000
    },
    "fixed_balance":{
        "BTC":0.00000000,
        "ETH":0.00000000,
        "LTC":0.00000000,
        "XRP":0.00000000,
        "BNB":0.00000000,
        "USDT":0.0000000
    }
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
	def increase_fixed_balance_currency_amt(self,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
		collection=db['test-user-wallet']


		result=collection.find_one({'email':email})
		client.close()
		try:
			if result is not none:
				bal=result['fixed_balance']
				bal[coin]+=amount
				return True
			else:
				return False
		except:
			return False


	@classmethod
	def decrease_fixed_balance_currency_amt(self,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
		collection=db['test-user-wallet']


		result=collection.find_one({'email':email})
		client.close()
		try:
			if result is not none:
				bal=result['fixed_balance']
				bal[coin]-=amount
				return True
			else:
				return False
		except:
			return False


	@classmethod
	def get_wallet(self,email):

		
		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
		collection=db['test-user-wallet']


		result=collection.find_one({'email':email})
		if result:
			return cls(result['email'], result['balance'], result['fixed_balance']), str(result['_id'])
		else:
			return None, None


	@classmethod
	def get_wallet_currency(self,email,coin):

		
		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
		collection=db['test-user-wallet']


		result=collection.find_one({'email':email})
		if result:
			return cls(result['email'], result['balance'][coin]), str(result['_id'])
		else:
			return None, None

