# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:  # LL node
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"


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
        pass

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
        # check if a target exists in the bucket with matching keys
        if self.storage[index] is not None and self.storage[index].key == key:
            # if so, remove that target
            self.storage[index] = None
        else:
            # else, print warning
            print("Warning: Key does not exist")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # get the index from hashmod
        index = self._hash_mod(key)
        # retrieving our target bucket
        target = self.storage[index]
        # check if a target exists in the bucket with matching keys
        if target is not None and target.key == key:
            # if so, return value
            return target.value
        else:
            # else, return None
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # create a new array size * 2
        # move all values over
        # remove old array


if __name__ == "__main__":
    ht = HashTable(2)  # hash table of size 2
    print(ht.storage)
    print("")
    # adding 3 items, guaranteed collision:
    ht.insert("apple", "delicious")
    ht.insert("pear", "not delicious")
    ht.insert("banana", "yummy")
    ht.insert("apple", "cake")
    # ht.insert("line_3", "Linked list saves the day!")
    print(ht.storage)
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("apple"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))
    print("")

    # Test removal
    ht.remove("apple")
    print(ht.storage)
    print("")
    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")
