
car_name = [ "Volvo" , "BMW" , "Toyota" , "Mercedes" ]
new__car_name = [ "Ford" , " Tesla"]

print("New car list :" , new__car_name)
print("Car list :" , car_name )

car_name.insert(0,"Mazda")              # Insert :insert at index
print("Insert ( Mazda ):",car_name)

car_name.append("TATA")                 # Append :add on end 
print("Append ( TATA ):",car_name)

car_name.extend( new__car_name )        # Extand :add 2 list
print("Extand (New car list):", car_name)             



