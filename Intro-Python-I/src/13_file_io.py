"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

f = open('foo.txt')  # opens file
print(f.read())  # mode argument is optional and 'r' is assumed if omitted
f.close()  # closed file
# f.closed()  # boolean that checks if file was closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing.
# Write three lines of arbitrary content to that file,
# then close the file.
# Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# write and create file if it does not exist. plus sign indicates both read and write.
b = open('bar.txt', 'w+')
b.write('keep it secret, keep it safe\n you shall not pass\n fool of a took')
# returns the number of characters written.
b.close()
b = open('bar.txt', 'r')
print(b.read())

# resources:
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# https://www.guru99.com/reading-and-writing-files-in-python.html
# https://www.codespeedy.com/how-does-carriage-return-work-in-python/
