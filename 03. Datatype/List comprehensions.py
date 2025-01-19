from random import randrange
squares = [x * x for x in (1, 2, 3, 4)]

sq = []
for x in (1, 2, 3, 4):
 squares.append(x * x)

# Get a list of uppercase characters from a string
print([s.upper() for s in "Hello World"])
# Strip off any commas from the end of strings in a list
print([w.strip(',') for w in ['these,', 'words,,', 'mostly', 'have,commas,']])

# When using if/else together use them before the loop
print([x if x in 'aeiou' else '*' for x in 'apple'])
# When using if only
print("If only",[x for x in range(10) if x % 2 == 0])

#double iteration
def foo(i):
 return i, i + 0.5
print([str(x)
 for i in range(3)
 for x in foo(i)
])

#sort
print([sorted(x) for x in [[2, 1], [4, 3], [0, 1]]])

#more readable print statement
[print(x) for x in (1, 2, 3)]

#random no.
print([randrange(1, 9) for _ in range(10)])

#ignore whitespace
print([
 x for x
 in 'foo'
 if x not in 'bar'
])

[x if x > 2 else '*' for x in range(10) if x % 2 == 0]

def f(x):
    return x**2
print([f(x) for x in range(10) if f(x) > 10])

[v for v in (f(x) for x in range(10)) if v > 10]
[v for v in map(f, range(10)) if v > 10]


# Dictionary Comprehensions
{x: x * x for x in (1, 2, 3, 4)}
dict((x, x * x) for x in (1, 2, 3, 4))  #same

#filter
initial_dict = {'x': 1, 'y': 2}
{key: value for key, value in initial_dict.items() if key == 'x'}


#swap
my_dict = {1: 'a', 2: 'b', 3: 'c'}
swapped = {v: k for k, v in my_dict.items()}
swapped = dict((v, k) for k, v in my_dict.iteritems())
swapped = dict(zip(my_dict.values(), my_dict))
swapped = dict(zip(my_dict.values(), my_dict.keys()))
swapped = dict(map(reversed, my_dict.items()))

# Merging Dictionaries
dict1 = {'w': 1, 'x': 1}
dict2 = {'x': 2, 'y': 2, 'z': 2}
{k: v for d in [dict1, dict2] for k, v in d.items()}

#List Comprehensions with Nested Loops
data = [[1], [2, 3], [4, 5]]
output = [element for each_list in data
 if len(each_list) == 2
 for element in each_list
 if element != 5]
print(output)

#Generator Expressions
# list comprehension
[x**2 for x in range(10)]


#Set Comprehensions
# A set of even numbers between 1 and 10:
{x for x in range(1, 11) if x % 2 == 0}
