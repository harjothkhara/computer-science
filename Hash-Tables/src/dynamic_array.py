class DynamicArray:
    def __init__(self, capacity=1):
        self.count = 0  # Number of elements in the array
        self.capacity = capacity  # Total amount of storage in the array
        # allocating, reserving that memory for our capacity
        self.storage = [None] * capacity

    def insert(self, index, value):
        # 0(n)
        # Check if we have enough capacity
        if self.count >= self.capacity:
            # If not, add more capacity
            self.resize()
        # Shift over every item after index to the right by 1
        for i in range(self.count, index, -1):  # going backwards from count to index
            self.storage[i] = self.storage[i-1]
        # Add the new value to the index
        self.storage[index] = value
        # Increment count
        self.count += 1

    # best and avg case is 0(1), worst case is 0(n) when we need to resize (happens less and less frequently, if we're doubling the size of the memory each time we hit capacity e.g 2 -> 4 -> 8 -> 16 -> 32). as our elements grow we end up resizing our memory less amount of time.
    def append(self, value):
        # 0(1) (most of the time)
        # Check if we have enough capacity
        if self.count >= self.capacity:
            # If not, double the size
            self.resize()
        # Add value to the index of count (count is going to be the last index)
        self.storage[self.count] = value
        # Increment count
        self.count += 1

    def resize(self):
        # O(n)
        # Double capacity
        self.capacity *= 2
        # Allocate a new storage array with double capacity (new memory)
        new_storage = [None] * self.capacity
        # Copy all elements from old storage to new
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

    # Insert -------
# [1, 2, 3, 4, None] --> [1, None, 3, 4]  --> insert value
# # Insert object before index
# arr = [1, 2, 3, 4]
# arr.insert(2, 2.5)
# shift everything over , Insert object before index
# |      |
# [1, 2, 3, 4, None, None] capacity --> [1, 2, 2.5, 3, 4, None] --> 0(n) operation
# >> [1, 2, 2.5, 3, 4]
# shift everything over by one, make sure index is empty before we insert there

# arr = [1, 2, 2.5, 3, 4, None]
# for i in range(5, 2, -1):
#     print(i)


a = DynamicArray(2)  # size
a.insert(0, 10)  # add 10 at 0 index
a.insert(0, 11)  # add 11 at 0 index
print(a.storage)  # [11, 10]
a.append(9)  # hit capacity so array is resized(doubled) [11, 10, 9, None]
a.append(8)  # 8 is added
print(a.storage)  # [11, 10, 9, 8]
a.append(7)  # hit capacity so array is resized(doubled) again

print(a.storage)  # [11, 10, 9, 8, 7, None, None, None]
