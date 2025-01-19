# Inordered 
# Inchangable item but you chan add or remove items
# No duplicate
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
print(type(thisset))
print("Set :",thisset)
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(" Set constructor :",thisset)

# Accessing ----------------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset)    #check the presence

# Add & Remove
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.add("orange")                 # ******no index ( inordered )
thisset.update(tropical)              # ******
print(" After add :",thisset)

thisset.remove("banana")              # ****** reomve
thisset.discard("papaya")             # ****** Remove
thisset.pop()                         # ****** Remove random
print(thisset)
thisset.clear()                       # ****** remove all ele
del thisset                           # ****** Delete set

# Loop set -----------------------------------------------------------------------
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Join set------------------------------------------------------------------------
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set4 = set1 | set2                      # ****** same as .union
set3 = set1.union(set2)                 # ****** same as | ( multiple )
set1.update(set2)                       # ****** update change original
print("Update :",set1,
      "\nUnion :",set3,
      "\nUnion | :",set4)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1,"\n",set2)                      # ****** show common

intersect=set1.intersection(set2)           # ****** op=( & ), update ,[ set1 - (set1 - set2 ) ] common
print("Intersection        :" , intersect )

set3 = set1.difference(set2)                # ****** op=( - ), update ,[ set - set2  ] not in set2

symm_diff=set1.symmetric_difference(set2)   # ****** op=( ^ ), update ,[ All ]
print("\nSymmetric_difference   :",symm_diff)
