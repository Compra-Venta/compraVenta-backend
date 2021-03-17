from pymongo import MongoClient
from pprint import pprint
import pymongo

class Wallet:

	def __init__(self,email):
		self.email=email
	
	@classmethod
	def retrieve_wallet(cls,email):
		client=MongoClient('localhost',27017)
		collection=db['wallet_user']
		ans=collection.find_one({'email':email})
		client.close()
		if ans is not None:
			return cls(ans['BTC'],ans['ETH'],ans['LTC'])
		else:
			return None,400
	
	@classmethod
	def retrieve_btc(cls,email):
		client=MongoClient('localhost',27017)
		collection=db['wallet_user']
		ans=collection.find_one({'email':email})
		client.close()
		if ans is not None:
			return cls(ans['BTC'])
		else:
			return None,400
			
	@classmethod
	def retrieve_eth(cls,email):
		client=MongoClient('localhost',27017)
		collection=db['wallet_user']
		ans=collection.find_one({'email':email})
		client.close()
		if ans is not None:
			return cls(ans['ETH'])
		else:
			return None,400
			
	@classmethod
	def retrieve_ltc(cls,email):
		client=MongoClient('localhost',27017)
		collection=db['wallet_user']
		ans=collection.find_one({'email':email})
		client.close()
		if ans is not None:
			return cls(ans['LTC'])
		else:
			return None,400
			
		
	def insert(self,btc,eth,ltc):
		client=MongoClient('localhost',27017)
		collection=db['wallet_user']
		post={
			'btc':btc,
			'eth':eth,
			'ltc':ltc
			}
		try:
			if collection.insert_one(post) is not None:
				client.close()
				return True
			else:
				client.close()
				return False
		except:
			client.close()
			return False
