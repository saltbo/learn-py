
# Python's ternary expression syntax
# Syntax: value_if_true if condition else value_if_false
# Example of a ternary expression
"hello" if 0 > 1 else "world"

# Lists

# create a list with 3 elements, all initialized to 0
list1 = [0] * 3
print(list1)


# remove an element from a list in Python
array = [0,1,0,2,3,0,4,0,5,6]
print(array)
array.remove(0)
print(array)

# remove all occurrences of an element from a list in Python
# using list comprehension
array = [x for x in array if x != 0]
print(array)

# Tuples
# create a tuple with 3 elements
tuple1 = (0, 1, 2)
print(tuple1)

# Dictionaries
# create a dictionary with 3 key-value pairs
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1)


# Sets
# create a set with 3 elements
set1 = {1, 2, 3}
print(set1)
# create an empty set
set2 = set()
print(set2)
# add an element to a set
set2.add(1)
print(set2)

# & | - ^
# create two sets
set3 = {1, 2, 3}
set4 = {3, 4, 5}
# intersection of two sets
set5 = set3 & set4
print(set5)
# union of two sets
set6 = set3 | set4
print(set6)
# difference of two sets
set7 = set3 - set4
print(set7)
# symmetric difference of two sets
set8 = set3 ^ set4
print(set8)


# For loops
# iterate over a list
for i in [0, 1, 2]:
    print(i)
# iterate over a range of numbers
for i in range(3):
    print(i)
# iterate over a range of numbers with a step
for i in range(0, 10, 2):
    print(i)
# iterate over a string
for i in "abc":
    print(i)
# iterate over a dictionary
for key, value in {'a': 1, 'b': 2}.items():
    print(key, value)
# iterate over a set
for i in {1, 2, 3}:
    print(i)
# iterate over a tuple
for i in (0, 1, 2):
    print(i)
# iterate over a list with index
for index, value in enumerate([0, 1, 2]):
    print(index, value)
# iterate over two lists simultaneously
for a, b in zip([0, 1, 2], ['a', 'b', 'c']):
    print(a, b)
# iterate over a list in reverse order
for i in reversed([0, 1, 2]):
    print(i)
# iterate over a sorted list
for i in sorted([2, 0, 1]):
    print(i)

# While loops
# iterate while a condition is true
i = 0
while i < 3:
    print(i)
    i += 1
# iterate while a condition is true with break
i = 0
while True:
    print(i)
    i += 1
    if i >= 3:
        break

# With statement
# open a file and read its contents
with open('file.txt', 'r') as file:
    contents = file.read()
    print(contents)
# open a file and write to it
with open('file.txt', 'w') as file:
    file.write('Hello, world!')

# Functions
# define a function
def add(a, b):
    return a + b
# call a function
result = add(1, 2)
print(result)

# define a function with default arguments
def add2(a, b=0):
    return a + b
# call a function with default arguments
result = add2(1)
print(result)

# define a function with variable-length arguments
def add3(*args):
    return sum(args)
# call a function with variable-length arguments
result = add3(1, 2, 3)
print(result)
# define a function with keyword arguments
def add4(**kwargs):
    return sum(kwargs.values())
# call a function with keyword arguments
result = add4(a=1, b=2, c=3)
print(result)

# return multiple values from a function
def add5(a, b):
    return a + b, a - b
result = add5(1, 2)
print(result)
# unpack multiple values from a function
a, b = add5(1, 2)
print(a, b)

# lambda functions
add6 = lambda a, b: a + b
result = add6(1, 2)
print(result)
# map function
result = list(map(lambda x: x * 2, [1, 2, 3]))
print(result)
# filter function
result = list(filter(lambda x: x % 2 == 0, [1, 2, 3]))
print(result)
