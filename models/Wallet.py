import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class Wallet:

	def __init__(self,email,data):
		# if calling through object we need to have these 2 things.
		self.email=email
		self.data=data

	def insert(self):
		# Inserting new document in our collection.
		#Using pymongo to connect to the mongodb.
		#Now we will establish connection on default port num 27017.
		client=MongoClient('localhost',27017)
		db=client['test-user-db-compra-venta']
		collection=db['test-wallet-collection']
		email=self.email
		data=self.data

		#post in the form of json/dictionary.

		post={

			'email':email
			'data':data

		}

		client.close()

		try:
			collection.insert_one(post)
			
			return True
		except:
			return False


	
	#Creating class method because we don't want to call through object.
	# we want to retrieve data thrugh email

	@classmethod
	def find_by_email(cls,email):

		client=MongoClient()
		db=client['test-user-db-compra-venta']
		collection=db['test-wallet-collection']
		# finding by making email as a key which will definately be unique to all users.
		ans=collection.find_one({'email':email})
		client.close()
		if ans is not None:
			return cls(ans['email'],ans['data']),ans['_id']
			
		else:
			
			return None,None
			


	@classmethod
	def find_by_email_and_cryptocurrency(cls,email,cryptocurrency):

		client=MongoClient()
		db=client['test-user-db-comra-venta']
		collection=db['test-wallet-collection']
		# getting information of a paticular currency.
		ans=collection.find_one({'email':email})
		client.close()
		if ans is not None:

			return ans['data'].get(cryptocurrency,None)
		else:
			return None
	

	@classmethod
	def reset_wallet(cls,email):

		client=MongoClient()
		db=client['test-user-db-compra-venta']
		collection = db['test-wallet-collection']
		

		reset_data={

			'USD':1000000.000000

		}

		try:
			collection.update({'email':email},{"$set":{"data":reset_data}})
			client.close()
			return 1

		except:
			client.close()
			return None

	@classmethod

	def transaction(cls,email,base_asset,quote_asset,amount1,amount2):

		client=MongoClient()
		db=client['test-user-db-compra-venta']
		collection = db['test-wallet-collection']

		user_key={'email':email}
		user_value={'$set':{base_asset:amount1}}

		user_value1={'$set':{quote_asset:amount2}}
		
		try:
			collection.update(user_key,user_value)
			collection.update(user_key,user_value1)
			

		except:
			return None











