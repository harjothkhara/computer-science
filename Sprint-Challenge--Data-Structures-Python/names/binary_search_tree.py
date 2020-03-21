
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


bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.in_order_print(print)

# bst.dft_print(print)

# bst.bft_print(print)
