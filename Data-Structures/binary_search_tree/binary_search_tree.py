from dll_stack import Stack
from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')

# solvable without having reference to the parent


class BinarySearchTree:  # a single node is a tree
    def __init__(self, value):  # similar to LL/DLL
        self.value = value  # root at each given node
        self.left = None  # left side at each given node
        self.right = None  # right side at each given node

    # Insert the given value into the tree
    def insert(self, value):
        # compare the root value to the new value being added
        # if the value is less than the root, move left
        if value < self.value:
            # if no child on that side insert
            if self.left is None:
                 # creating a new class instance
                self.left = BinarySearchTree(value)  # a single node is a tree
            # else keep moving left and call insert method again (on left) and do the check again until no child, and you can insert value to the tree
            else:
                self.left.insert(value)
        # if the value is greater than the root, move right
        elif value >= self.value:
            # if no child on that side insert
            if self.right is None:
                # creating a new class instance
                self.right = BinarySearchTree(value)  # a single node is a tree
            # else keep moving right and call insert method again (on right) and do the check again until no child, and you can insert value to the tree
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # look at root and compare it to the target
        # if the target is less than the current node value,
        if target < self.value:
            # move left, if value exists repeat
            if self.left is not None:
                # recurse left side until target is found
                return self.left.contains(target)
            else:
                return False
        # if target is greater than the current node value, move right and repeat
        elif target > self.value:
            # move right, if value exists repeat
            if self.right is not None:
                # recurse right side until target is found
                return self.right.contains(target)
            else:
                return False
        # if the target equals the value return True - basecase
        elif target == self.value:
            return True

    # Return the maximum value found in the tree
    # max node found on last leaf on right side of tree
    def get_max(self):
        if self.right is not None:
            # recurse right if value exists
            return self.right.get_max()
        else:
            # return max value if no pointer to next node exists (self.right === None)
            return self.value

    # Call the function `cb` on the value of each node.
    # fyi - cb function is defined in test - adding random ints to an array
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call cb function on self.value, each node value
        cb(self.value)
        # traversing BST on every branch until there are no more nodes on left/right
        # if left
        if self.left is not None:
            # call for_each function
            # no return, not returning a recursive value at each stack but executing a function
            self.left.for_each(cb)
        # if right
        if self.right is not None:
            # call for each function
            # no return, not returning a recursive value at each stack but executing a function
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

        # Depth First Traversal(DFT)
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # go left FIRST
        if node.left is not None:
            node.in_order_print(node.left)

        # print ourselves
        print(node.value)

        # go right
        if node.right is not None:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        # intializa a stack
        storage = Stack()  # FIFO
        # push root to stack
        storage.push(self)

        # while stack not empty
        while storage.len() > 0:
            # pop top item out of stack into a temp
            node = storage.pop()
        # DO THE THING (print)
            print(node.value)
        # if temp has a right push into stack
            if node.right:
                storage.push(node.right)
        # if temp has a left push into stack
            if node.left:
                storage.push(node.left)

        # STRETCH Goals -------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.dft_print(print)
