
# Ordred (3.7)
# changeable
# not duplicate data
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print( " Whole dict    :",thisdict)
print( " Only brand's  :",thisdict["brand"])
print( " Length        :",len(thisdict))
print( " Type          :",type(thisdict))

constructor = dict(name = "John", age = 36, country = "Norway")
print(" Constructor   :",constructor)

key = thisdict.keys()             # use to display only keys
print(" Keys          :",key) 

value = thisdict.values()           # use to display only value
print(" Values        :",value)       

item = thisdict.items()            # Use to display both key and value
print(" Items         :",item)

# Change--------------------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.get("year"))
thisdict.update({"model": "GT40"})  # change/Add
thisdict["color"] = "White"         # Change/Add
thisdict.pop("model")               # Remove (remove random if empty)
thisdict.popitem()                  # Remove last item
print(thisdict)
thisdict.clear()                    # Remove all (not delete)
del thisdict                        # Delete 

# Copy dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()            # Or( mydict=dict(thisdict) )
print(mydict)

# Nested -----------------------------------------------------------------------
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for key, val in myfamily.items():
  print(key)

  for y in val:
    print(y + ':', val[y])
