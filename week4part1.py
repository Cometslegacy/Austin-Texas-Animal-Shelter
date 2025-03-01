from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
	""" CRUD operations for Animal collection in MongoDB """

	def __init__(self,USER = 'aacuser', PASS = 'SNHU1234', HOST = 'nv-desktop-services.apporto.com', PORT = 33100, DB = 'AAC', COL = 'animals'):
		# Connection Variables
		#USER = 'aacuser'
		#PASS = 'SNHU1234'
		#HOST = 'nv-desktop-services.apporto.com'
		#PORT = 33100
		#DB = 'AAC'
		#COL = 'animals'

		# Initialize Connection
		self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
		self.database = self.client[DB]
		self.collection = self.database[COL]

	# Create method to implement the C in CRUD
	def create(self, data):
		if data is not None:
			self.database.animals.insert_one(data)
		else:
			raise Exception("Nothing to save, because data parameter is empty")

	# Read method to implement the R in CRUD
	def read(self, query):
		if query is not None:
			return self.database.animals.find(query)
		else:
			raise Exception("Query not found.")

	# Update method to implement the U in CRUD
	def update(self, query, new_values):
		try:
			result = self.database.animals.update_many(query, {"$set": new_values})
			return result.modified_count
		except Exception as e:
			print(f"Update Error: {e}")
			return 0

	# Delete method to implement the D in CRUD
	def delete(self, query):
		try:
			result = self.collection.delete_many(query)
			return result.deleted_count
		except Exception as e:
			print(f"Delete Error: {e}")
			return 0

