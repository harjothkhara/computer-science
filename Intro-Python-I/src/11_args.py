# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE


def f1(n1, n2):
    return n1+n2


print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"
"""
'*' allows you to take in an extra arguments that weren't previous set in parameters.
the variable we associate with '*' becomes an iterable.
By convention it is often used with the word 'args'. 'def extraArguments(*args)'
"""
# YOUR CODE HERE


def f2(*num):
    return sum(num)


print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

# some more fun with args '*' and not knowing which arguments will be passed into function:


def test_args(arg1, *args):
    print("first normal arg set in function", arg1)
    for arg in args:
        print("another arg not defined in function:", arg)


test_args('alfie', 'python', 'eggs', 'bacon')

# if your passing in arguments set somwhere elsewhere add '*'in front of the collection name
mytuple = ("cheese", 5, "bread")
test_args(*mytuple)

# if your passing in arguments set somwhere elsewhere add '*'in front of the collection name
mylist = [7, 6, 5, 4]

# How do you have to modify the f2 call below to make this work?
# add an '*' in front of the collection your passing in as an argument.
# Should print 22 '*' will make python unpack the values in mylist and pass it to the function
print(f2(*mylist))

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.

# YOUR CODE HERE


def f3(arg1, arg2=1):
    return arg1 + arg2

# arg1 is mandatory, and won't work without the arg2 default value. if arg2 value is provided it will overwrite the default value


print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".

# YOUR CODE HERE
def f4(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print("key: {0}, value: {1}".format(key, value))

# # another way
# def f4(**kwargs):
#     print(kwargs)
#     for key in kwargs:
#         print(f"key: {key}, value: {kwargs[key]}")


f4(a=12, b=30)

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# How do you have to modify the f4 call below to make this work?
# '**' needed in front of dictionary collection name in order to unpack keyword names inside.
f4(**d)


"""
Practicing
"""


def greet_me(**kwargs):  # keyword arguments
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


# needs '**' kwargs in parameter of function
greet_me(name="Bob", teacher="John", occupation="banker",
         hobbies="swimming", school="hogwarts")


def greet_me_again(name, age, occupation, hobbies):  # keyword arguments
    print("name", name)
    print("age", age)
    print("occupation", occupation)
    print("hobbies", hobbies)


# when passing in a collection into the function, parameter of function doesn't need '*'
# Keys in a dictionary need to be unique
kwargon = {'name': 'Bob', 'age': 'peter',
           'occupation': 'plumber', 'hobbies': 'running'}

# when calling a function with a dictionary that has keyword value, then add '**' in front of collection name so that python can unpack the dictionary before passing it into function
greet_me_again(**kwargon)
