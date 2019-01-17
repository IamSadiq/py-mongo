import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

customers = mydb["customers"]

# FIND
x = customers.find_one()

print(x)


# FIND ALL
for x in customers.find():
  print(x)

for x in customers.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

for x in customers.find({},{ "address": 0 }):
  print(x)

for x in customers.find({},{ "name": 1, "address": 0 }):
  print(x)