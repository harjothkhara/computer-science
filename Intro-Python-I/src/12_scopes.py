# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12  # global by default


def change_x():
    # global keyword allows us to modify global variable otherwise we can only access it inside of function scope.
    global x
    x = 99  # local to function by default


change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()

"""
The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
"""
