# Import required modules
from abc import ABC, abstractmethod

# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Create abstract method      
    @abstractmethod
    def printDetails(self):
        pass
  
    # Create concrete method
    def accelerate(self):
        print("Speed up ...")
  
    def break_applied(self):
        print("Car stopped")

# Create a child class
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Not having this feature")

# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
  
    def sunroof(self):
        print("Available")

# Create an instance of the Hatchback class
car1 = Hatchback("Maruti", "Alto", "2022")

# Call methods
car1.printDetails()
car1.accelerate()
car1.sunroof()



import zope.interface 


class MyInterface(zope.interface.Interface): 
	x = zope.interface.Attribute('foo') 
	def method1(self, x, y, z): 
		pass
	def method2(self): 
		pass

@zope.interface.implementer(MyInterface) 
class MyClass: 
	def method1(self, x): 
		return x**2
	def method2(self): 
		return "foo"
obj = MyClass() 

# ask an interface whether it 
# is implemented by a class: 
print(MyInterface.implementedBy(MyClass)) 

# MyClass does not provide 
# MyInterface but implements it: 
print(MyInterface.providedBy(MyClass)) 

# ask whether an interface 
# is provided by an object: 
print(MyInterface.providedBy(obj)) 

# ask what interfaces are 
# implemented by a class: 
print(list(zope.interface.implementedBy(MyClass))) 

# ask what interfaces are 
# provided by an object: 
print(list(zope.interface.providedBy(obj))) 

# class does not provide interface 
print(list(zope.interface.providedBy(MyClass))) 
