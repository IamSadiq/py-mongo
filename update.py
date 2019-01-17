# UPDATE COLLECTION
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

customers = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

customers.update_one(myquery, newvalues)

#print "customers" after the update:
for x in customers.find():
  print(x)


myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = customers.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")