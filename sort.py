# SORTING
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

customers = mydb["customers"]

mydoc = customers.find().sort("name")

for x in mydoc:
  print(x)

mydoc = customers.find().sort("name", -1)

for x in mydoc:
  print(x)