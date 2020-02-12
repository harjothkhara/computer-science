"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %s' % x)

y = round(y, 2)
print('y is %s' % y)

print('z is %s' % z)

# Use the 'format' string method to print the same thing


# Finally, print the same thing using an f-string

names = ["Sarah", "jorge", "sam", "frank"]
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

new_dict = {}

food_dict = {
    'apple': 'is a fruit',
    'cucumber': 'is a vegetable'
}
chosen_fruit = 'apple'
print(food_dict[chosen_fruit])

for key in food_dict:
    print(key.value())
