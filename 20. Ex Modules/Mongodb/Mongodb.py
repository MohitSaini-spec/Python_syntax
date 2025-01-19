import pymongo 

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]


print("Creation=================================================")
print("Database Name :",myclient.list_database_names())
db=myclient.list_database_names()
if "mydatabase" in db:
    print("existing database")

print("Collection :",mydb.list_collection_names())

if "mydatabase" in db:
    print("existing database")


#INSERTION===================================
print("INSRTION===============================================")
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print("Inserted ID", x.inserted_id)

insertThese = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}

]
manyinsert = mycol.insert_many(insertThese)


# Update============================================================
print('UPDATING============================================')
print("'Valley 345' updated to 'Canyon 123'")
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
mycol.update_one(myquery, newvalues)
for x in mycol.find({},{"_id":0}):
  print(x)


myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")

mycol.update_one(   
  { "address": "Post Title 5" }, 
  {
    "$set": 
      {
        "name": "Mohit Saini",
        "address": "Post Title 5"
      }
  }, 
  upsert=True        # add i fnot pesent
)

#FINDING=========================================================

print("\nFINDING========================================")
mydoc = mycol.find_one({},{"_id":0})
print("First document:\n", mydoc)

myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery,{"_id": 0})
print("Second document:")
for x in mydoc:
    print(x)

# print("All documents :",end="")
# for i in mycol.find():
#     print(i)

print("Name and address :\n", end="")
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }): #both 0 and 1 only work with id 
  print(x)

# print("Exclude address :", end="")
# for x in mycol.find({},{ "address": 0 }):
#   print(x)


print("Address greter then 's' :\n")
temp ={"address":{"$gt":"M"}}
mydoctemp=mycol.find(temp,{"_id":0})
for x in mydoctemp:
    print(x)

print("Stored with 's' :")
myquery = { "address": { "$regex": "^P" } }
mydoc = mycol.find(myquery,{"_id":0})
for x in mydoc:
  print(x)


#finding with limit
print("First 5 elemet :")
myresult = mycol.find({},{"_id":0}).limit(5)
#print the result:
for x in myresult:
  print(x)

#Sorting============================================
print("\nSorting============================================")
print("Sorted with name in descending order")
mydoc = mycol.find({},{"_id":0}).sort("name",-1)
for x in mydoc:
  print(x)

#delete============================================================
print("\nDeleting============================================================")
print("Deleted with address :", end="")
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)


myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

x=mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

#COllection deleted =================
mycol.drop()
