str1="hello"
str2="world"

print("\n1 Concatenation--------------------")
finalStr=str1+" "+str2
print(str1 , "+" , str2 , "=" , finalStr)                 #concatenation
#SLICING
print("\n2 Slicing--------------------------")
print("2.1 Positive_Indexing--------------")
print(len(finalStr))            #length
print(finalStr[:4])             #start to 4 (including 4th)
print(finalStr[3:])             #3 to end
print(finalStr[3:len(finalStr)])#3 to end
# Negative indexing
print("\n2.1 Positive_Indexing--------------")
print(finalStr[-11:-7]+" "+"[-11:-7]")
print(finalStr[-8:]+" "+"[-8:]")

# method

print("\n3 Method---------------------------")
print(finalStr.endswith("ld"),"endswith")
print(finalStr.capitalize()+" "+"capitalize")
print(finalStr.replace("world","wOrld")+" "+"replace")
print(finalStr.find("hello"),"find(hello)")
print(finalStr.count("l"),"count(l)")

print("\n4 Escape character-----------------")
print("\'single quote\n\\Backslash\n\r")

