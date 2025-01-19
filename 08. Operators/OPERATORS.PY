# OPERATORS
# 1. ARITHMATIC OPERATORS
print("{:-^50s}".format("ARITHMETIC"))
x,y=5,2
print( x,"+",y, "=",x+y )        # 5+2 = 7
print( x,"-",y, "=",x-y )        # 5-2 = 3
print( x,"*",y, "=",x*y )        # 5*2 = 10
print( x,"/",y, "=",x/y )        # 5/2 = 2.5
print( x,"%",y ,"=",x%y )        # 5%2 = 1
print( x,"**",y, "=",x**y )       # 5*5 = 25 (multiply 5, 2 times)
print( x,"//",y, "=",x//y)         # 5//2= 2  (in int)

# 2. ASSIGNMENT OPERATORS

print("{:-^50s}".format("ASSIGNMENT"))
x = 5         # Declaretion
print("Declare outside print function",x)
x += 5        # x = x + 5 
print("Incement '+=5' ",x)      # (any arithmetic or bitwise op is used at the place of +)
print("Declare inside print function 'y:=5' ",y:=5)   # Assigning inside a funcation

# 3. COMPARISON OPERATORS (return true or false on the bases of condition)
print("{:-^50s}".format("COMPARISON"))
a , b = 3 , 6
print( a,"==",b,"=",a == b )  # compare a =
print( a,"!=",b,"=",a != b )
print( a,">",b,"=",a > b )
print( a,"<",b,"=",a < b )
print( a,">=",b,"=",a >= b )
print( a,">=",b,"=",a >=b )

# 4. LOGICAL OPERATOR
print("{:-^50s}".format("LOGICAL"))
print( a<5 and b>10)
print( a<5 or b>10)
print( not(a<5 and b>10))

# 5. IDENTITY OPERATOR
print("{:-^50s}".format("IDENTITY"))
print(a is b)
print(a is not b)

# 6. MEMBERSHIP OPERATOR

print("{:-^50s}".format("MEMBERSHIP"))
listtocheck=[0,1,2,3,4,5,6,7,8,9]
print(a in listtocheck)
print(a not in listtocheck)

num1=5