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
