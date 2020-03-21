import time
from binary_search_tree import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# this solution ^^ is 0(n^2) for each entry in name_1 your looping through name_2
# runtime: 6.446194887161255 seconds

# optimized solution  below os 0(n) - looping once through each name/node in the tree  runtime: 0.11794686317443848 seconds

bst = BinarySearchTree(names_1[0])  # adding first name in tree
for i in range(1, len(names_1)):  # looping though remaining names and inserting into bst
    bst.insert(names_1[i])

# check if bst contains duplicates by using contains method on bst class
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
