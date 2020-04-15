# '''
# Linked List hash table key/value pair
# '''


import time


class LinkedPair:  # LL node
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}, {self.next}>"


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.count = 0  # Number of items currently in the hash table
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # start from an arbitrary large prime
        hash_value = 5381
        # Bit-shift and sum value for each character
        for char in key:
            hash_value = ((hash_value << 5) + hash_value) + char
        return hash_value

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        # hashmod the key to find the index
        index = self._hash_mod(key)
        new_node = LinkedPair(key, value)

        # check if index is None and insert a new node pair at that index
        if self.storage[index] is None:
            # create a new LinkedPair and place it in the bucket
            self.storage[index] = new_node
        # if key already exists at head of LL, replace value
        elif self.storage[index].key == key:
            self.storage[index].value = value
        else:  # else, traverse LL for node insertion or value override point
            last_item = self.storage[index]
            # traverse through LL and check for last item and key matches
            # hash('pear') % 16 != hash('apple') % 16
            while last_item.next is not None and last_item.key != key:  # keep going until at end or keys match
                last_item = last_item.next
            # if the key matches, replace the value
            if last_item.key == key:
                last_item.value = value
            # else insert a new_node at the end
            else:
                last_item.next = new_node

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # hashmod the key to find the index
        index = self._hash_mod(key)
        item = self.storage[index]
        # check if a item exists in the bucket with matching keys
        if item is not None:
            # and keys match
            if item.key == key:
                # removing value stored with key
                item.value = None
            # find the node (search the LL) with matching key
            else:
                current_item = item.next
                while current_item is not None:
                    if current_item.key == key:
                        # removing value stored with key
                        current_item.value = None
                    # key doesn't match so move onto the next node
                    current_item = current_item.next
        else:
            # else, print warning
            print("Warning: Key does not exist")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # look through the list until key matches (search the LL)

        # get the index from hashmod
        index = self._hash_mod(key)
        item = self.storage[index]
        # check if item at index exists (root node)
        if item is not None:
            # if so and keys match
            if item.key == key:
                # return value at that index
                return item.value
            # else traverse (search) the LL at that index until key matches
            else:
                current_item = item.next
                # if there is a next node and there's something there go to it
                while current_item is not None:
                    # if keys match retrieve the value
                    if current_item.key == key:
                        return current_item.value
                    # move onto the next node and repeat
                    current_item = current_item.next
        # else if item doesn't exist return None
        else:
            # else, return None
            # print(f"Warning: collision at {index}")
            return None
    # to prevent storing everything in a limited storage capacity, even with LL implementation at the arr index, we still want to resize the array when it hits a certain load factor (# of entries / hash table capacity), and to prevent all items from being stored in limited storage slots down a very long o(n) LL chain (even though its possible and LL chaining will prevent collisions, performance of the hash table will degrade). optimal load factor is 0.7 but doubling it is ok and doesn't effect performance.

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # create a new array size * 2
        # move all values over
        # remove old array

        # save current hashmap in temp var
        prev_storage = self.storage
        # double capacity
        self.capacity *= 2
        # new storage
        self.storage = [None] * self.capacity

        # copy each item (that is not None) from old storage into new storage
        for item in prev_storage:
            # if head is only item, insert
            # self.storage[index] = bucket   self.storage[index].next = None
            if item is not None and item.next is None:
                self.insert(item.key, item.value)
            # if there's a LL, traverse it and insert each item
            # # self.storage[index] = bucket   self.storage[index].next = bucket
            if item is not None and item.next is not None:
                current_item = item
                while current_item.next is not None:
                    self.insert(current_item.key, current_item.value)
                    # move onto the next node and insert
                    current_item = current_item.next
                # once at the end, insert last node
                self.insert(current_item.key, current_item.value)


if __name__ == "__main__":
    ht = HashTable(2)  # hash table of size 2
    print(ht.storage)  # [None, None]
    print("")

    # adding 3 items, guaranteed collision:
    ht.insert("apple", "delicious")
    print(ht.storage)
    ht.insert("pear", "not delicious")
    print(ht.storage)
    ht.insert("banana", "yummy")
    print(ht.storage)
    ht.insert("apple", "cake")
    # ht.insert("line_3", "Linked list saves the day!")
    print(ht.storage)
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("apple"))
    print(ht.retrieve("banana"))
    # print(ht.retrieve("line_3"))
    print("")

    # Test removal
    ht.remove("apple")
    print(ht.storage)
    print("")

    # Test resizing
    old_capacity = len(ht.storage)
    print(old_capacity)
    ht.resize()
    new_capacity = len(ht.storage)
    print(new_capacity)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("apple"))
    print(ht.retrieve("pear"))
    print(ht.retrieve("banana"))

    print("")


# testing hashes
n = 100000
key = b"STR"
print(f"Hashing {n}x")


def djb2(key):
        # start from an arbitrary large prime
    hash_value = 5381
    # Bit-shift and sum value for each character
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value


start_time = time.time()
for i in range(n):
    djb2(key)
end_time = time.time()
print(f" DJB2 hash runtime: {end_time - start_time} seconds")

start_time = time.time()
for i in range(n):
    hash(key)
end_time = time.time()
print(f" Python hash runtime: {end_time - start_time} seconds")
