# from dll_stack import Stack
# from dll_queue import Queue
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
                self.left = BinarySearchTree(value)
            # else keep moving left and call insert method again (on left) and do the check again until no child, and you can insert value to the tree
            else:
                self.left.insert(value)
        # if the value is greater than the root, move right
        elif value >= self.value:
            # if no child on that side insert
            if self.right is None:
                self.right = BinarySearchTree(value)
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
        # if the target equals the value return True
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

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


root = BinarySearchTree(5)
root.insert(5)
root.insert(10)
