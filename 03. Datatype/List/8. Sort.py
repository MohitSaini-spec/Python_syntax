car_name = [ "Volvo" , "BMW" , "Toyota" , "Mercedes" , "Ford" , "Tesla" ]
car_name.sort()
print( car_name )

car_name.sort( reverse=True )
print( car_name )

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
