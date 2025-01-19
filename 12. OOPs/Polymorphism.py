# A simple Python function to demonstrate 
# Polymorphism

def add(x, y, z = 0): 
    return x + y+z

# Driver code 
print(add(2, 3))
print(add(2, 3, 4))

#----------------------------------------------
#calling diffrent function of diffrent method 
# wth same name using loop
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()


#----------------------------------------------
#accesssing method of diffrent class using inheritancs
class Bird:
  def intro(self):
    print("There are many types of birds.")
    
  def flight(self):
    print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
    
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
    
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
 
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
 
#     def type(self):
#         print("India is a developing country.")
 
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
 
#     def language(self):
#         print("English is the primary language of USA.")
 
#     def type(self):
#         print("USA is a developed country.")

# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
 
# obj_ind = India()
# obj_usa = USA()
 
# func(obj_ind)
# func(obj_usa)

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create a list of Animal objects
animals = [Dog(), Cat()]

# Call the speak method on each object
for animal in animals:
    print(animal.speak())