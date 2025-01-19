import re


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

x = re.sub("\s", "9", txt)
print(x)

x = re.split("\s", txt)
print(x)

x = re.search("Portugal", txt)
print(f'Portugal in txt : {x}')

x = re.findall("The", txt)
print(f'Finding The in  txt :{x}')

x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

x = re.search("ai", txt)
print(x) #this will print an object

x = re.search(r"\bS\w+", txt)
print(x.string)
print(x.span())
print(x.group())