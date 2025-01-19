x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#tuyplt to list , list to tuplt

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)


thistuple = ("apple", "banana", "cherry")
del thistuple