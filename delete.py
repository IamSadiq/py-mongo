import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

customers = mydb["customers"]

# DELETING ONE
myquery = { "address": {"$regex": "^S"} }

x = customers.delete_many(myquery)

print(x.deleted_count, " documents deleted.")


# DELETE ALL
x = customers.delete_many({})

print(x.deleted_count, " documents deleted.")