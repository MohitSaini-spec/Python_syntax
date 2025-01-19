class Person:

  company = "novaars"
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def cahngecompanynames(cls):
    cls.company = "novars"

  def change_name(self, name):
    self.company = name

  def show(self):
    print(f"Company Name: {self.company}")
  def __str__(self):
    return f"{self.name}({self.age})"

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
p1.myfunc()
p2 = Person("p2",32)
p2.show()
p2.change_name("no name")
p2.show()
p3 = Person("p3",32)
p3.cahngecompanynames()
p3.show()
p4=Person("p4",32)
p4.show()



# del p1.age        parameter deleted
# del p1            object deleted

print(p1)


class Person1:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p11 = Person1("wick", 42)
p11.myfunc()
