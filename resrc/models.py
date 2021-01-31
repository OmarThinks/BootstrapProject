import os
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, func
import json
from sqlalchemy.orm import backref, relationship, scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

SUPPORTED_TYPES = [int,str,float,bool,type(None)]
RESTRICTED_FIELDS=["password"]
Base = declarative_base()
engine = create_engine('sqlite:///databases/test.sqlite', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
										 #autoflush=False,
										 bind=engine))



"""
NotReceived
This class is used when the dada is not received
By default, it will have the value of None
None != Not received
"""
class NotReceived():
	pass
		


"""
validate_key

- Inputs:
	- the_dict:dict
		- The dictonary of the data to be validated
		- Example:
			- {"id":5,"name":"abc"}
	- key: str:
		- the key of the dict that contains the data
		- Example:
			- "id"
	- id: bool : default = False
		- Should we pass the id or not
		- True: let the id pass
		- False: do not le the id pass (Default)
	- unsupported : bool: default = False
		- pass unsupported data types, not in SUPPORTED_TYPES list
		- True: let it pass
		- False: do not let it pass (Default)
	- restricted : bool: default = False
		- pass restricted keys, in SUPPORTED_TYPES list
		- True: let it pass
		- False: do not let it pass (Default)
- Function:
	- telling us whether we should let this key pass or not
- Output: 
	- True: let ths pass
	- False: do not let this key pass
"""
def validate_key(the_dict:dict,key:str,id:bool=False,
	unsupported:bool = False, restricted:bool=False):
	# Validating fields startng with "_"
	if key[0] == "_":
		return False
	# Validating NotReceived
	if type(kwargs[key]) == Type(NotReceived):
		return False
	# Validating id
	if key.lower() == "id" and id == False:
		return False
	# Validating supported types
	if ((type(kwargs[key])not in SUPPORTED_TYPES) and (unsupported==False)):
		return False
	# validating restricted fields
	if ((str(kwargs[key]) in RESTRICTED_FIELDS) and (restricted==False)):
		return False
	return True

class MyModel():
	#def __init__(self):
	#	pass
	def __init__(self, **kwargs):
		# If something was not received, or key == id, the field will not be created
		for key in kwargs:
			if (type(kwargs[key]) != NotReceived or 
				key =="id" or 
				type(kwargs[key]) not in SUPPORTED_TYPES):
				setattr(self,key,kwargs[key])  
	
	def insert(self):
		print(self)
		db_session.add(self)
		db_session.commit()

	def update(self,**kwargs):
		# If some thing was not received, the field will not be updated
		# id can not be updated
		for key in kwargs:
			if validate_key(kwargs,key,restricted=True) == True:
				setattr(self,key,kwargs[key])  
		db_session.commit()

	def delete(self):
		db_session.delete(self)
		db_session.commit()

	def simple(self):
		# Prepare to delete all the keys starting with "_", or key == "id"
		toReturn = {}
		for key in self.__dict__:
			if key[0] == '_':
				continue
			if type(self.__dict__[key]) not in SUPPORTED_TYPES:
				continue
			toReturn[key] = self.__dict__[key]
		return toReturn

	def __repr__(self):
		return json.dumps(self.simple())

	def deep(self):
		toReturn = {}
		for key in self.__dict__:
			if key[0] == '_' :
				continue
			if type(self.__dict__[key]) not in SUPPORTED_TYPES:
				try:
					toReturn[key]=self.__dict__[key].simple()
				except Exception as e:
					continue
			else:
				toReturn[key] = self.__dict__[key]
		return toReturn



'''
User
a persistent product entity, extends the base SQLAlchemy Model
id,username,password

Relationships:
products,orders,images

'''
class User(Base,MyModel):
	#__metaclass__=MyModel
	__tablename__="user"
	# Autoincrementing, unique primary key
	id = Column(Integer(), primary_key=True)
	# String username
	username = Column(String(), unique=True, nullable=False)
	# username could be like "fish"
	# username has to be unique
	# not allowing several users to have the same username
	password =  Column(String(), unique=False, nullable=False)
	# Password is a string
	# Example: "12345", "abc"
	# it doesn't have to be unique

	products = relationship("Product",backref=backref('seller',
						uselist=True,
						cascade='delete,all'))
	orders = relationship("Order",backref=backref('buyer',
						uselist=True,
						cascade='delete,all'))
	images = relationship("Image",backref=backref('seller',
						uselist=True,
						cascade='delete,all'))
	

'''
Product
a persistent product entity, extends the base SQLAlchemy Model
id,name,price,in_stock,seller_id
'''
class Product(Base, MyModel):
	__tablename__="product"
	# Autoincrementing, unique primary key
	id = Column(Integer(), primary_key=True)
	# String name
	name = Column(String(), unique=False, nullable=False)
	# name could be like "Labtop"
	# name dowsn't have to be unique
	# allowing several users to sell the same product
	price =  Column(Float(), unique=False, nullable=False)
	# Price is a float
	# Example: 5.0, 6.0 , 50.0, 0.5
	# It should be float, allowing things with low
	# price to be sold
	in_stock =  Column(Boolean(), unique=False, 
		nullable=False, default=True)
	# in_stock is a boolean
	# Example: True, False
	# it represents whether this product is for sale or not
	# True = For sale, can be displayed to customers
	# False = now for sale, can not be displayed to customers
	seller_id = Column(Integer(),ForeignKey("user.id"),
	 unique=False, nullable=False)
	#seller_id = Column(Integer(), unique=False, nullable=False)
	# seller_id
	# This is the id of the seller user
	# The user who sells this product
	# it is an integer
	# Example: 1, 2 or 3
	
	orders = relationship("Order",backref=backref('product',
						uselist=True,
						cascade='delete,all'))





"""
Order:
id, user_id, product_id, amount
"""
class Order(Base, MyModel):
	__tablename__="order"
	# Autoincrementing, unique primary key
	id = Column(Integer(), primary_key=True)
	# String name
	user_id =Column(Integer(),ForeignKey("user.id"),
	 unique=False, nullable=False)
	# user_id
	# This is the id of the user who ordered the products
	# it is an integer
	# Example: 1, 2 or 3
	product_id  = Column(Integer,ForeignKey("product.id"))
	# product_id is an integer 
	# it refers to the product.id in the products table
	# Example: 1, 2 , 3
	amount =  Column(Integer(), unique=False, nullable=False)
	# amount is an integer
	# Example: 5, 6, 50
	total_cost = 0.0



'''
Image
a persistent product entity, extends the base SQLAlchemy Model
id,seller_id,name,formatting

The image will be stroed with it's id
'''
class Image(Base, MyModel):
	__tablename__="image"
	# Autoincrementing, unique primary key
	id = Column(Integer(), primary_key=True)
	seller_id = Column(Integer(),ForeignKey("user.id"),
	 unique=False, nullable=False)
	# This is the id of the seller user
	# The user who sells this product
	# it is an integer
	# Example: 1, 2 or 3
	name = Column(String(), unique=False, nullable=False)
	# image name could be like "fish"
	# image name can not to be unique
	# not allowing several users to have the same username
	formatting =  Column(String(), unique=False, nullable=False)
	# formattng is a string that represents the type of image
	# There can be only 2 types: "png" , "jpg"
	# it can not be unique












def init_db():
	Base.query = db_session.query_property()
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)
init_db()

user = User(username = "abc", password = "123", id = 123)
print(user)
print(user.__dict__)
print(type(user.__dict__["password"]))

#user.insert()
#user.create({"username":123})
#print(user)
#print(dir(user))








