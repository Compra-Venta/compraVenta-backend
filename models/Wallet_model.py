import pymongo
from pymongo import MongoClient
#from bson.objectid import objectid

class Wallet:

	def __init__(self,email,balance,fixed_balance):

		self.email=email
		self.balance=balance
		self.fixed_balance=fixed_balance


	@classmethod
<<<<<<< HEAD
	def check_balance(cls,email,coin,amount):
=======
	def check_balance(self,email,coin,amount):
>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173

		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
		collection=db['test-user-wallet']
<<<<<<< HEAD
		try:
			result=collection.find_one({'email':email})
			client.close()
			if result is not None:
				bal=result['balance']
				currency_amt=bal[coin]
				if currency_amt >= amount:
					# true
					return 1
				else:
					return 0
			else:
				return -1
		except:
			client.close()
			return -1

	@classmethod
	def increase_balance_currency_amt(cls,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
=======

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
>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173
		collection=db['test-user-wallet']


		result=collection.find_one({'email':email})
<<<<<<< HEAD
		try:
			if result is not None:
				bal=result['balance']
				x = bal[coin]
				print(x)
				collection.update_one({'email':email},{"$set":{"balance."+coin:(x+amount)}})
				client.close()
				return 1
			else:
				print('here')
				client.close()
				return 0
		except:
			print('here')
			client.close()
			return -1


	@classmethod
	def decrease_balance_currency_amt(cls,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
		collection=db['test-user-wallet']
		try:
			result=collection.find_one({'email':email})
			if result is not None:
				bal=result['balance']
				x = bal[coin]
				print(x)
				collection.update_one({'email':email},{"$set":{"balance."+coin:(x-amount)}})
				client.close()
				return 1
			else:
				client.close()	
				return 0
		except:
			client.close()
			return -1

	
	@classmethod
	def reset_account(cls,email):
        
		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
=======
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
>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173
		collection=db['test-user-wallet']

		my_query={'email':email}

		new_value={

<<<<<<< HEAD
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
=======
		'$set':{
		'balance':{
        "BTC":0.00,
        "ETH":0.00,
        "LTC":0.00,
        "XRP":0.00,
        "BNB":0.00,
        "USDT":50000.00
    	},

    	'fixed_balance':{
        "BTC":0.00,
        "ETH":0.00,
        "LTC":0.00,
        "XRP":0.00,
        "BNB":0.00,
        "USDT":0.00
    	}


    }

 }
>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173
 		
		try:
 			collection.update_one(my_query,new_value)
 			collection.update_one(my_query,new_fixed_value)
 			client.close()
<<<<<<< HEAD
 			return 1
		except:
 			client.close()
 			return -1


	@classmethod
	def make_user_wallet(cls,email):


		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
=======
 			return True
		except:
 			client.close()
 			return False


	@classmethod
	def make_user_wallet(self,email):


		client=MongoClient('localhost',27017)
		db=collection['test-user-db-compra-venta']
>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173
		collection=db['test-user-wallet']

		post={

<<<<<<< HEAD
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
				return 0
			else:
				client.close()
				return 1
		except:
			client.close()
			return -1


	@classmethod
	def increase_fixed_balance_currency_amt(cls,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
		collection=db['test-user-wallet']

		result=collection.find_one({'email':email})
		try:
			if result is not None:
				bal=result['fixed_balance']
				x = bal[coin]
				collection.update_one({'email':email},{"$set":{"fixed_balance."+coin:(x+amount)}})
				client.close()
				return 1
			else:
				client.close()
				return 0
		except:
			return -1


	@classmethod
	def decrease_fixed_balance_currency_amt(cls,email,coin,amount):

		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
=======
    "email":email,
    "balance":{
        "BTC":0.00,
        "ETH":0.00,
        "LTC":0.00,
        "XRP":0.00,
        "BNB":0.00,
        "USDT":50000.00
    },
    "fixed_balance":{
        "BTC":0.00,
        "ETH":0.00,
        "LTC":0.00,
        "XRP":0.00,
        "BNB":0.00,
        "USDT":0.00
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
>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173
		collection=db['test-user-wallet']


		result=collection.find_one({'email':email})
<<<<<<< HEAD
		try:
			if result is not None:
				bal=result['fixed_balance']
				x = bal[coin]
				collection.update_one({'email':email},{"$set":{"fixed_balance."+coin:(x-amount)}})
				client.close()
				return 1
			else:
				client.close()
				return 0
		except:
			client.close()
			return -1


	@classmethod
	def get_wallet(cls,email):

		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
		collection=db['test-user-wallet']
		try:
			result=collection.find_one({'email':email})
			client.close()
			if result:
				return cls(result['email'], result['balance'], result['fixed_balance']), 1
			else:
				return None, 0
		except:
			client.close()
			return None, -1

	@classmethod
	def get_wallet_currency(cls,email,coin):

		
		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
		collection=db['test-user-wallet']

		try:
			result=collection.find_one({'email':email})
			client.close()
			if result:
				return result['balance'][coin], result['fixed_balance'][coin], 1
			else:
				return None, None, 0
		except:
			client.close()
			return None, None, -1

	
	@classmethod
	def do_wallet_updation(cls, email, coin_1, coin_2, amt_1, amt_2, source_1, source_2):

		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
		collection=db['test-user-wallet']
		try:
			collection.update_one({'email':email}, {"$inc":{source_1+"."+coin_1: amt_1, source_2+"."+coin_2:amt_2}})
			client.close()
			return 1
		except:
			client.close()
			return -1
=======
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

>>>>>>> 996a65a89312450173c1e72eb861bfcf61e1e173
