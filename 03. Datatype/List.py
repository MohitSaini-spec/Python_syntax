import itertools
import collections
list=["A","B","C","D",["E","EE"],"F"]
print("Calling---------------")
print("Complete list:",list)
print("Call with index [4]:",list[4])
print("Call with index [-2]:",list[-2])  #start with -1    

#slicing
print("\nSlicing----------------")
print("Index [:4]: ",list[:4])         #start to 4 (including 4th)
print("Index [3:]: ",list[3:])         #3 to end
print("Index [3:len(list)]: ",list[3:len(list)])#3 to end

#method
print("\nMethod------------------------")

list[1]="b"         #mutable
print("len(list): ",len(list))        #length

list.append("G")
print('append("G"): ',list)

list1=["H","I"]
print("list b: ",list1)

list.extend(list1)
print(list)

list.reverse()
print("reverse: ",list)

list.insert(-2,"B")
print('insert(-2,"B"): ',list)

list.remove("b")
print("remove: ",list)

list.pop(2)
print("pop(2)",list)
 
print("\nOperations----------------")
lst = []
if not lst:
    print("lst is empty")

for (index, item) in enumerate(list):
 print('The item in position {} is: {}'.format(index, item))

 print("Check item is in list: ",'A' in list)

print("All: ",all(list))
print("Any: ",any(list))

rev = list[::-1]
print("Reversed with [::-1]: ",rev)

#Concatenate and Merge lists
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3','b4']
clist = ['c1', 'c3', 'c4', 'c2','c5']
for a, b in zip(alist, blist):       #short len(list) work
 print(a, b)
for a,b,c in itertools.zip_longest(alist, blist, clist):
 print(a, b, c)

#names = ["aixk", "duke", "edik", "tofp", "duke"]
#list(set(names))
#print("Remove duplicate: ",names)
#print(collections.OrderedDict.fromkeys(clist).keys())
print("Comparison: ",[1, 10, 111] < [1, 12, 100])
#nested list
alist = [[[1,2],[3,4]], [[5,6,7],[8,9,10], [12, 13, 14]]]
for row in range(len(alist)): #A less Pythonic way to loop through lists
 for col in range(len(alist[row])):
  print("with len: ",alist[row][col])

for row in alist: #One way to loop through nested lists
 for col in row:
  print("with nested loop: ",col)

print("Slicing: ",alist[1][1:])

# Initializing a List to a Fixed Number of Elements
my_list=[{1}] * 10
print(my_list) 
my_list[0].add(2)      #same task on each item
print(my_list)
for_list=[{1} for _ in range(10)]
print(for_list)
for_list[0].add(2)     #only on index[0]
print(for_list)

