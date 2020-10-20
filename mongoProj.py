import pymongo
import os
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = client.list_database_names()
mydb = client['test']
colle = mydb['clients']
new_dict = {}
collectionList = mydb.list_collection_names()
my_dict = {"name": "test"}
change = {"$set":{"name": "delete_me"}}
changed = {"name": "delete_me"}

class Employee():
    def __init__(self, employee_id, firstname, lastname, year):
        self.firstname = firstname.title()
        self.lastname = lastname.title()
        self.year = year
        self.employee_id = employee_id
    def __str__(self):
        string = f"{self.firstname}, {self.lastname} hired in: {self.year} with id number: {self.employee_id}"
        return string

def mongoimport():
    e = Employee(0,"","",1200)
    index = 1
    for file in os.listdir(os.curdir+"\\Assignment 1 - data\\simple"):
        if index != 10001:
            with open(os.path.curdir+"\\Assignment 1 - data\\simple\\"+file, 'r') as f:
                n = f.readlines()
                for obj in n:
                    elements = obj.split(', ')
                    # print(elements)
                    employee_id = elements[0]
                    firstname = elements[1]
                    lastname = elements[2]
                    year = elements[3]
                    year = year.strip('\n')
                    e = Employee(employee_id,firstname,lastname,year)
                    print(e)
                    json.JSONEncoder()
                    colle.insert_one(e)
                index += 1
        elif index == 10001:
            break

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

mongoimport()