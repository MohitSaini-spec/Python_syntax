class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    print("Parent cons")

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    print("child cons")

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("john","wick",2005)
x.printname()
x.welcome()