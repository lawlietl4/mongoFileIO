import pymongo
import os
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = client.list_database_names()
mydb = client["test"]
colle = mydb['clients']
new_dict = {}
collectionList = mydb.list_collection_names()
my_dict = {"name": "test"}
change = {"$set":{"name": "delete_me"}}
changed = {"name": "delete_me"}

for file in os.listdir(os.curdir+"\\Assignment 1 - data\\simple"):
    with open(os.path.curdir+"\\Assignment 1 - data\\simple\\"+file, 'r') as f:
        n = f.readlines()
        for obj in n:
            elem = obj.split(', ')
            elem[3] = elem[3].strip('\n')
            # js = json.dumps()
            new_dict = {f'"id {elem[0]}':'"first name: {elem[1]}, last name: {elem[2]}, hire year: {elem[3]}'}
            print(new_dict)
            # colle.insert_one(new_dict)

# print(client.list_database_names())
# if "test" in dblist:
#     print("database exists")

# if "restaurants" in collectionList:
#     print("collection exists")

# colle.insert_one(my_dict)

# for x in colle.find(my_dict):
#     print(x)

# colle.update_one(my_dict, change)

# for x in colle.find(changed):
#     print(x)

# x = colle.delete_many({},{})
# print(x.deleted_count, " documents deleted.")