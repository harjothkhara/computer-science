test_list = [1, 2, 3, 4, 5]
test_tuple = (1, 2, 3, 4, 5)
test_dictionary = {"key1": "val1", "key2": "val2"}
test_set = ([1, 2, 3, 4, 5])

# prints out each item from the LIST
# ordered, like an array [], mutable, allows duplicates
for element in test_list:
    print(element)

# prints out each item from the TUPLE
# ordered, (), immutable, allows duplicates
for element in test_tuple:
    print(element)

# prints out each KEY from the DICTIONARY
# key/value storage, un-ordered, (), mutable, allows duplicates
for element in test_dictionary:
    print(element)
# prints out the KEY
for element in test_dictionary:
    print(element)
# prints out the VALUES
for element in test_dictionary:
    print(test_dictionary[element])
    # could also have used values() method

# prints out each UNIQUE item from the SET
# ONLY stores KEYS, un-ordered, (), mutable, no duplicates
for element in test_dictionary:
    print(element)
