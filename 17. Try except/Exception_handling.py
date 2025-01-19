import sys
a=10
b=3

print("{:-^50}".format("Try,Except,else,finally"))
try:
    quotient = a / b
    print(quotient)
except ZeroDivisionError as z:
    print("Name of exception :",z)
    print("You cannot divide by zero")
except (TypeError, NameError):
    print("You must convert strings to floats or integers before dividing")
    print("A variable you're trying to use does not exist")  
else:
    print("Success.")
finally:
    print("I will do may work any how")



#-------------------------------------------------------------------------
print("{:-^50}".format("Raising Exceptions"))
x = "hi"
if not type(x) is str:
    raise TypeError("Sorry, only strings are allowed")
else:
    print("This is string")


#-------------------------------------------------------------------------
print("{:-^50}".format("Assertions"))
if b==0:
    assert b!=0,"ZERO!!"                    #==========
else:
    print("Every thing is fine")

#-------------------------------------------------------------------------
print("{:-^50}".format("Custom Exception"))
class chotu(Exception):                     #==========                     
    pass
d= int(input("Enter a number. "))
try:
    if d>18:
        print("Eligible to vote")
    else:
        raise chotu                         #==========
except chotu:
    print("You are chotu.")

#-------------------------------------------------------------------------
print("{:-^50}".format("Standard Exception"))
f = int(input("Enter a password. "))
if f == 1234:
    sys.stderr.write("Verified")            #==========
else:
    print("Incorrect Password")