import unittest
from pydantic_models import (UserPost, UserUpdate, ProductPost, 
	ProductPost, OrderPost, OrderUpdate,
	ImagePost, ImageUpdate)
#from app import create_app
#from models import db
import json
from models import NotReceived

unittest.TestLoader.sortTestMethodsUsing = None

class pydanticTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
		#db_drop_and_create_all()
		#create_app()
		# create and configure the app
		#self.app = create_app(testing=True) #Flask(__name__)
		#self.client = self.app.test_client
		#db.app = self.app
		#db.init_app(self.app)
		#db.create_all()        
		pass
	
	def tearDown(self):
		"""Executed after reach test"""
		print("_+++++++++++++++++++++++++++++++++_")

	#Note: Tests are run alphapetically
	def test_000001_test(self):
		self.assertEqual(1,1)
		print("Test 1:Hello, Tests!")


	def test_001_01_1_UserPost(self):
		toValidate = {"username":123,"password":789}
		user = UserPost(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test 1_1_1:UserPost Successful")

	def test_001_01_2_UserPost(self):
		toValidate = {}
		try:
			user = UserPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
				"msg": "field required","type": "value_error.missing"},{"loc": [
				"password"],"msg": "field required","type": "value_error.missing"}])
		print("Test 1_1_2:UserPost:Fail:all missing required")

	def test_001_01_3_UserPost(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = UserPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test 1_1_3:UserPost:Fail:username required")






	def test_001_02_1_UserUpdate(self):
		toValidate = {"username":123,"password":789}
		user = UserUpdate(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test 1_2_1:UserUpdate Successful")

	def test_001_02_2_UserUpdate(self):
		toValidate = {"username":123}
		user = UserUpdate(**toValidate)
		self.assertEqual(user.username,"123")
		self.assertEqual(type(user.password),NotReceived)
		#self.assertEqual(user.dict(),{"username":"123","password":NotReceived()})
		print("Test 1_2_2:UserUpdate Successful Missing field")

	def test_001_02_3_UserUpdate(self):
		toValidate = {}
		user = UserUpdate(**toValidate)
		self.assertEqual(type(user.username),NotReceived)
		self.assertEqual(type(user.password),NotReceived)
		print("Test 1_2_3:UserUpdate Successful: all Missing fields")

	def test_001_02_4_UserUpdate(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = UserUpdate(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test 1_2_4:UserUpdate:Fail:username required")



















	def test_002_01_1_ProductPost(self):
		toValidate = {"username":123,"password":789}
		user = ProductPost(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test 2_1_1:ProductPost Successful")

	def test_002_01_2_ProductPost(self):
		toValidate = {}
		try:
			user = ProductPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
				"msg": "field required","type": "value_error.missing"},{"loc": [
				"password"],"msg": "field required","type": "value_error.missing"}])
		print("Test 2_1_2:ProductPost:Fail:all missing required")

	def test_002_01_3_ProductPost(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = ProductPost(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test 2_1_3:ProductPost:Fail:username required")









	def test_002_02_1_ProductUpdate(self):
		toValidate = {"username":123,"password":789}
		user = ProductUpdate(**toValidate)
		self.assertEqual(user.dict(),{"username":"123","password":"789"})
		print("Test 2_2_1:ProductUpdate Successful")

	def test_002_02_2_ProductUpdate(self):
		toValidate = {"username":123}
		user = ProductUpdate(**toValidate)
		self.assertEqual(user.username,"123")
		self.assertEqual(type(user.password),NotReceived)
		#self.assertEqual(user.dict(),{"username":"123","password":NotReceived()})
		print("Test 2_2_2:ProductUpdate Successful Missing field")

	def test_002_02_3_ProductUpdate(self):
		toValidate = {}
		user = ProductUpdate(**toValidate)
		self.assertEqual(type(user.username),NotReceived)
		self.assertEqual(type(user.password),NotReceived)
		print("Test 2_2_2:ProductUpdate Successful: all Missing fields")

	def test_002_02_4_ProductUpdate(self):
		toValidate = {"password":{},"username":{}}
		try:
			user = ProductUpdate(**toValidate)
			self.assertEqual(True,False)
		except Exception as e:
			#print(str(e.json()))
			self.assertEqual(json.loads(e.json()),[{"loc": ["username"],
			"msg": "str type expected","type": "type_error.str"},{"loc": [
	  		"password"],"msg": "str type expected","type": "type_error.str"}])
		print("Test 2_2_3:ProductUpdate:Fail:username required")


































# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()