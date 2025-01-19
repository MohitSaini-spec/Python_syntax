
# Multi Words Variable Names
myVariableName = "John"    #camel case
MyVariableName = "John"    #pascal case
my_variable_name = "John"  #anake case

#syntax
print("{:-^100}".format("Typecasting"))
intNum=int(4.5)
floatNum=float(2)
firstname='firstname'
lastname="lastname"
print("Type of int after conversion:",type(floatNum))


print("{:-^100}".format("Assigning value"))
#multiple value assign at once
x, y, z = "Orange", "Banana", "Cherry"
print("Multiple value assign at once :",x)
print("Multiple value assign at once :",y)
print("Multiple value assign at once :",z)
a = b = c = "Orange"
print("Assigning one value to diffrent var:",a)
print("Assigning one value to diffrent var:",b)
print("Assigning one value to diffrent var:",c)

#unpack collecation 
fruits = ["apple", "banana", "cherry"]   #list
x, y, z = fruits
print("Unpack the list :",x)
print("Unpack the list :",y)
print("Unpack the list :",z)

print( "Printing  string and variable : hello "+x)

print("{:-^100}".format("Printing multivalue"))

#printing multiple variables
print("Print multiple variable with , :",x,y,z)
print("Print multiple variable with + :",x+y+z) #print strinf without space
print("Adding both int and float:",intNum+floatNum)  #addboth value
#print(x+intNum) doesn't allowed
