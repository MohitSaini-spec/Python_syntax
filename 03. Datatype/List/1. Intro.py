#INTRO

# Allowed duplicate data / Mutable / Ordered / 
list_name = [ 30 , "August" , 2024 , "Saturday" ]
print( list_name )
print( "Number of element :",len( list_name ) )
print( "Type              :",type( list_name ) )

# Constructor 
new_list = list(( 30 , "August" , 2024 , "Saturday" )) # Use of double round-brackets
print( "Constructor       :" , new_list )

# Access items of list
print( "Second element    :",list_name[1])            # Access using index
print( "Slice form 0 to 1 :",list_name[ -4:-3 ] )     # Accessing slice
if "August" in list_name:       # 
    print("Exist             : August exists in list")

# Changing items
list_name[1]="July"
list_name[2:4] = [2025, "Friday"]
print( "After changing    :", list_name )

print("----------------------Method---------------------" )
# Add items
new__car_name = [ "Ford" , " Tesla"]
car_name = [ "Volvo" , "BMW" , "Toyota" , "Mercedes" ]

print("New car list       :" , new__car_name)
print("Car list           :" , car_name )

car_name.insert(0,"Mazda")              # Insert :insert at index
print('.insert(0,"Mazda") :',car_name)

car_name.append("TATA")                 # Append :add on end 
print(".append(TATA)      :",car_name)

car_name.extend( new__car_name )        # Extand :add 2 list
print(".extend(newcarlist):", car_name)             

#remove
car_name.remove("BMW")
print(".remove()          :", car_name)             
car_name.pop(0)
print(".pop(0)            :", car_name)             
car_name.pop()
print(".pop()             :", car_name)             
del car_name[-1]
print("del car_name[-1]   :",car_name)
car_name.clear()
del car_name

print("LOOP---------------------------------------------------")
car_name = [ "Volvo" , "BMW" , "Toyota" , "Mercedes" , " Ford " , " Tesla" ]
for x in car_name :
  print(x,end="  ")
print("")

for i in range(len( car_name )):
  print( car_name[i], end="  ")
print("")

i = 0
while i < len( car_name ):
  print( car_name[i] , end="  ")
  i = i + 1
print("")

[print(x,end="  ") for x in car_name]