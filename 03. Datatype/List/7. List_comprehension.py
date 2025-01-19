
car_name = [ "Volvo" , "BMW" , "Toyota" , "Mercedes" , " Ford " , " Tesla" ]
newlist = [x for x in car_name if "a" in x]
print(newlist)

newlist = [x for x in car_name]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x.upper() for x in car_name]
print(newlist)

newlist = ['hello' for x in car_name]
print(newlist)

newlist = [x if x != "BMW" else "AUDI" for x in car_name]
print(newlist)

