# importing time library to track time
import time
# importing binary tree structure
from binary_search_tree import BinarySearchTree

# starting time tracker
start_time = time.time()

# reading the names file
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# reading the names file
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# the first for loop checks each name in names_1, so the speed of that depends on n,
# the number of names in the list. the next for loop also checks for every name in names_2
# so depends on the number of names in the list, also n. So, we have n * n complexity, of n^2

# this solution ^^ is 0(n^2) for each entry in name_1 your also looping through each entry in name_2. # runtime: 6.446194887161255 seconds

# optimized solution  below os o(n)(logn) - looping once through each name/node(names_1 - 0(n)) in the bst (names_2 - logn)  runtime: 0.11794686317443848 seconds

# inserting names_1 list into bst (logn)
bst = BinarySearchTree(names_1[0])  # adding first name in tree
for i in range(1, len(names_1)):  # looping though remaining names and inserting into bst
    bst.insert(names_1[i])

# loop through each name in names_2 list and see if there's duplicates in the names_1 bst tree
for name in names_2:  # o(n)
    # check if bst contains duplicates by using contains method on bst class
    # if target name from names_2 is in tree then return true and append
    if bst.contains(name):
        duplicates.append(name)

# bst is optimized for searches, faster b/c each comparison allows the operations to skip about half of the tree, reduces potential answer by 2, or eliminate one side. avg case is logn, worst case to find an element is 0(n) b/c it could be a LL, and need to search thru the whole tree one at a time.

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# walk through of given solution (o(n^2)): http://pythontutor.com/visualize.html#code=duplicates%20%3D%20%5B%5D%20%0A%0Anames_1%20%3D%20%5B%0A%20%20%20%20%22Jean%20Velazquez%22,%0A%20%20%20%20%22Nataly%20Flowers%22,%0A%20%20%20%20%22Ronnie%20Barrera%22,%0A%20%20%20%20%22Lilly%20Pineda%22,%0A%20%20%20%20%22Belen%20Flynn%22,%0A%20%20%20%20%22Fernando%20Stout%22,%0A%20%20%20%20%5D%0A%0Anames_2%20%3D%20%5B%0A%20%20%20%20%22Fernando%20Stout%22,%0A%20%20%20%20%22Lilly%20Pineda%22,%0A%20%20%20%20%22Dominique%20Beck%22,%0A%20%20%20%20%22Anabella%20Atkinson%22,%0A%20%20%20%20%22Nataly%20Flowers%22,%0A%20%20%20%20%22Joaquin%20Luna%22,%0A%20%20%20%20%5D%0A%0Afor%20name_1%20in%20names_1%3A%0A%20%20%20%20for%20name_2%20in%20names_2%3A%0A%20%20%20%20%20%20%20%20if%20name_1%20%3D%3D%20name_2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20duplicates.append%28name_1%29%0A%0A&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# walk through of optimized solution with bst (o(n)-see whiteboard) http://pythontutor.com/visualize.html#code=class%20BinarySearchTree%3A%20%20%23%20a%20single%20node%20is%20a%20tree%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%20%20%23%20similar%20to%20LL/DLL%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%20%20%23%20root%20at%20each%20given%20node%0A%20%20%20%20%20%20%20%20self.left%20%3D%20None%20%20%23%20left%20side%20at%20each%20given%20node%0A%20%20%20%20%20%20%20%20self.right%20%3D%20None%20%20%23%20right%20side%20at%20each%20given%20node%0A%0A%20%20%20%20%23%20Insert%20the%20given%20value%20into%20the%20tree%0A%20%20%20%20def%20insert%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20%23%20compare%20the%20root%20value%20to%20the%20new%20value%20being%20added%0A%20%20%20%20%20%20%20%20%23%20if%20the%20value%20is%20less%20than%20the%20root,%20move%20left%0A%20%20%20%20%20%20%20%20if%20value%20%3C%20self.value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20no%20child%20on%20that%20side%20insert%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.left%20is%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20creating%20a%20new%20class%20instance%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.left%20%3D%20BinarySearchTree%28value%29%20%20%23%20a%20single%20node%20is%20a%20tree%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20else%20keep%20moving%20left%20and%20call%20insert%20method%20again%20%28on%20left%29%20and%20do%20the%20check%20again%20until%20no%20child,%20and%20you%20can%20insert%20value%20to%20the%20tree%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.left.insert%28value%29%0A%20%20%20%20%20%20%20%20%23%20if%20the%20value%20is%20greater%20than%20the%20root,%20move%20right%0A%20%20%20%20%20%20%20%20elif%20value%20%3E%3D%20self.value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20no%20child%20on%20that%20side%20insert%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.right%20is%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20creating%20a%20new%20class%20instance%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.right%20%3D%20BinarySearchTree%28value%29%20%20%23%20a%20single%20node%20is%20a%20tree%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20else%20keep%20moving%20right%20and%20call%20insert%20method%20again%20%28on%20right%29%20and%20do%20the%20check%20again%20until%20no%20child,%20and%20you%20can%20insert%20value%20to%20the%20tree%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.right.insert%28value%29%0A%0A%20%20%20%20%23%20Return%20True%20if%20the%20tree%20contains%20the%20value%0A%20%20%20%20%23%20False%20if%20it%20does%20not%0A%20%20%20%20def%20contains%28self,%20target%29%3A%0A%20%20%20%20%20%20%20%20%23%20look%20at%20root%20and%20compare%20it%20to%20the%20target%0A%20%20%20%20%20%20%20%20%23%20if%20the%20target%20is%20less%20than%20the%20current%20node%20value,%0A%20%20%20%20%20%20%20%20if%20target%20%3C%20self.value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20move%20left,%20if%20value%20exists%20repeat%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.left%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20recurse%20left%20side%20until%20target%20is%20found%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20self.left.contains%28target%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%23%20if%20target%20is%20greater%20than%20the%20current%20node%20value,%20move%20right%20and%20repeat%0A%20%20%20%20%20%20%20%20elif%20target%20%3E%20self.value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20move%20right,%20if%20value%20exists%20repeat%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.right%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20recurse%20right%20side%20until%20target%20is%20found%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20self.right.contains%28target%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%23%20if%20the%20target%20equals%20the%20value%20return%20True%20-%20basecase%0A%20%20%20%20%20%20%20%20elif%20target%20%3D%3D%20self.value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%0Aduplicates%20%3D%20%5B%5D%20%0A%0Anames_1%20%3D%20%5B%0A%20%20%20%20%22Jean%20Velazquez%22,%0A%20%20%20%20%22Nataly%20Flowers%22,%0A%20%20%20%20%22Ronnie%20Barrera%22,%0A%20%20%20%20%22Lilly%20Pineda%22,%0A%20%20%20%20%22Belen%20Flynn%22,%0A%20%20%20%20%22Fernando%20Stout%22,%0A%20%20%20%20%5D%0A%0Anames_2%20%3D%20%5B%0A%20%20%20%20%22Fernando%20Stout%22,%0A%20%20%20%20%22Lilly%20Pineda%22,%0A%20%20%20%20%22Dominique%20Beck%22,%0A%20%20%20%20%22Anabella%20Atkinson%22,%0A%20%20%20%20%22Nataly%20Flowers%22,%0A%20%20%20%20%22Joaquin%20Luna%22,%0A%20%20%20%20%5D%0A%0Abst%20%3D%20BinarySearchTree%28names_1%5B0%5D%29%20%20%23%20adding%20first%20name%20in%20tree%0A%0Afor%20i%20in%20range%281,%20len%28names_1%29%29%3A%20%20%23%20looping%20though%20remaining%20names%20and%20inserting%20into%20bst%0A%20%20%20%20bst.insert%28names_1%5Bi%5D%29%0A%0A%23%20check%20if%20bst%20contains%20duplicates%20by%20using%20contains%20method%20on%20bst%20class%0Afor%20name%20in%20names_2%3A%0A%20%20%20%20if%20bst.contains%28name%29%3A%0A%20%20%20%20%20%20%20%20duplicates.append%28name%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# Resources - https://stackabuse.com/comparing-strings-using-python/
