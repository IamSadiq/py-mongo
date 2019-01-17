import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

customers = mydb["customers"]

myquery = { "address": { "$gt": "S" } }

mydoc = customers.find(myquery)

for x in mydoc:
  print(x)

myquery = { "address": { "$regex": "^S" } }

mydoc = customers.find(myquery)

for x in mydoc:
  print(x)

myquery = { "address": "Park Lane 38" }

mydoc = customers.find(myquery)

for x in mydoc:
  print(x)
