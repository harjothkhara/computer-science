"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

# sys.argv[0] is the name of the script. if no script name was passed to the interpreter, argv[0] is the empty string
print("This is the name of the script: ", sys.argv[0])
# This is the name of the script: 03_modules.py
print("Number of arguments: ", len(sys.argv))
# Number of arguments: 1
print("The arguments are: ", sys.argv)
# The arguments are: ['03_modules.py']

# for loop if there was more then one script running
for arg in (sys.argv):
    print("for loop result: ", arg)


# Print out the OS platform you're using:
# YOUR CODE HERE
print("I am using the following OS platform: ", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("this is the version of python i'm using: ", sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("this is the current process ID: ", os.getpid())
# PID uniquely identify an active process being run on a kernal OS

# Print the current working directory (cwd):
# YOUR CODE HERE
print("this is the current working directory: ", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("machines's login name: ", os.getlogin())
# machines's login name: root
