"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.

Comprehensions in Python. Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) using sequences which have been already defined.

List comprehensions are used for creating new lists from other iterables. As list comprehensions returns lists, they consist of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element. ... Here, square brackets signifies that the output is a list
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [i for i in range(1, 6)]

print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# creates a new list containing the cubes of all values from range(10)
y = [i**3 for i in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [words.upper() for words in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work? used int() build in python method
# elements in x are strings, need to convert each to int before using any math operation
y = [elements for elements in x if int(elements) % 2 == 0]

print(y)
