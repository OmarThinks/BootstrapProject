import unittest
from models import NotReceived, validate_key, MyModel, User, Product, Order, Image, init_db



unittest.TestLoader.sortTestMethodsUsing = None

class modelsTestCase(unittest.TestCase):
	"""This class represents the trivia test case"""

	def setUp(self):
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
	def test_001_test(self):
		self.assertEqual(1,1)
		print("Test 1:Hello, Tests!")

	def test_a_1_1_1_validate_key(self):
		the_dict = {"id":41,"password":"abc","username":"tryu","bool1":True,"bool2":False,
		"nr":NotReceived}
		validated = []
		for key in the_dict:
			validated.append(validate_key(the_dict,key))
		self.assertEqual([False,False,True,True,True,False],validated)
		print("Test a_1_1_1 : validate_key: success")

	def test_a_1_1_2_validate_key(self):
		the_dict = {"id":41,"password":"abc","username":"tryu","bool1":True,"bool2":False,
		"nr":NotReceived}
		validated = []
		for key in the_dict:
			validated.append(validate_key(the_dict,key,id=True))
		self.assertEqual([True,False,True,True,True,False],validated)
		print("Test a_1_1_2 : validate_key: success")

	def test_a_1_1_3_validate_key(self):
		the_dict = {"id":41,"password":"abc","username":"tryu","bool1":True,"bool2":False,
		"nr":NotReceived}
		validated = []
		for key in the_dict:
			validated.append(validate_key(the_dict,key,dangerous = True))
		self.assertEqual([False,True,True,True,True,False],validated)
		print("Test a_1_1_3 : validate_key: success")

	def test_a_1_1_4_validate_key(self):
		the_dict = {"id":41,"password":"abc","username":"tryu","bool1":True,"bool2":False,
		"nr":NotReceived}
		validated = []
		for key in the_dict:
			validated.append(validate_key(the_dict,key,dangerous = True))
		self.assertEqual([False,True,True,True,True,False],validated)
		print("Test a_1_1_4 : validate_key: success")

	def test_a_1_1_5_validate_key(self):
		the_dict = {"id":41,"password":"abc","username":"tryu","bool1":True,"bool2":False,
		"nr":NotReceived, "unsupported":{}}
		validated = []
		for key in the_dict:
			validated.append(validate_key(the_dict,key,dangerous = True, unsupported=True))
		self.assertEqual([False,True,True,True,True,False,False],validated)
		print("Test a_1_1_5 : validate_key: success")

	def test_a_1_1_6_validate_key(self):
		user = User(username = "abc", password = "pass")
		the_dict = {"id":41,"password":"abc","username":"tryu","bool1":True,"bool2":False,
		"nr":NotReceived, "unsupported1":{}, "unsupported2":user}
		validated = []
		for key in the_dict:
			validated.append(validate_key(the_dict,key,dangerous = True, unsupported=True))
		self.assertEqual([False,True,True,True,True,False,False,True],validated)
		print("Test a_1_1_6 : validate_key: success")

	def test_a_1_1_7_validate_key(self):
		user = User(username = "abc", password = "pass")
		the_dict = {"id":41,"password":"abc","username":"tryu","bool1":True,"bool2":False,
		"nr":NotReceived, "unsupported1":{}, "unsupported2":user}
		validated = []
		for key in the_dict:
			validated.append(validate_key(the_dict,key,dangerous = True, unsupported=False))
		self.assertEqual([False,True,True,True,True,False,False,False],validated)
		print("Test a_1_1_7 : validate_key: success")











# Make the tests conveniently executable
if __name__ == "__main__":
	unittest.main()