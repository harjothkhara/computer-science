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


# python tutor walk through
# http://pythontutor.com/visualize.html#code=class%20LinkedPair%3A%0A%20%20%20%20def%20__init__%28self,%20key,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.key%20%3D%20key%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%3C%7Bself.key%7D,%20%7Bself.value%7D%3E%22%0A%0Aclass%20HashTable%3A%0A%20%20%20%20def%20__init__%28self,%20capacity%29%3A%0A%20%20%20%20%20%20%20%20self.capacity%20%3D%20capacity%20%20%23%20Number%20of%20buckets%20in%20the%20hash%20table%0A%20%20%20%20%20%20%20%20self.storage%20%3D%20%5BNone%5D%20*%20capacity%0A%0A%20%20%20%20def%20_hash%28self,%20key%29%3A%0A%20%20%20%20%20%20%20%20return%20hash%28key%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20_hash_mod%28self,%20key%29%3A%0A%20%20%20%20%20%20%20%20'''%0A%20%20%20%20%20%20%20%20Take%20an%20arbitrary%20key%20and%20return%20a%20valid%20integer%20index%0A%20%20%20%20%20%20%20%20within%20the%20storage%20capacity%20of%20the%20hash%20table.%0A%20%20%20%20%20%20%20%20'''%0A%20%20%20%20%20%20%20%20return%20self._hash%28key%29%20%25%20self.capacity%0A%20%20%20%20%20%0A%20%20%20%20def%20insert%28self,%20key,%20value%29%3A%0A%20%20%20%20%20%20%20%20%23%20hashmod%20the%20key%20to%20find%20the%20index%0A%20%20%20%20%20%20%20%20index%20%3D%20self._hash_mod%28key%29%0A%20%20%20%20%20%20%20%20new_node%20%3D%20LinkedPair%28key,%20value%29%0A%0A%20%20%20%20%20%20%20%20%23%20check%20if%20index%20is%20None%20and%20insert%20a%20new%20node%20pair%20at%20that%20index%0A%20%20%20%20%20%20%20%20if%20self.storage%5Bindex%5D%20is%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20create%20a%20new%20LinkedPair%20and%20place%20it%20in%20the%20bucket%0A%20%20%20%20%20%20%20%20%20%20%20%20self.storage%5Bindex%5D%20%3D%20new_node%0A%20%20%20%20%20%20%20%20%23%20if%20key%20already%20exists%20at%20head%20of%20LL,%20replace%20value%0A%20%20%20%20%20%20%20%20elif%20self.storage%5Bindex%5D.key%20%3D%3D%20key%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.storage%5Bindex%5D.value%20%3D%20value%0A%20%20%20%20%20%20%20%20%23%20check%20if%20a%20key%3Avalue%20node_pair%20already%20exists%20in%20the%20index%28bucket%29%0A%20%20%20%20%20%20%20%20else%3A%20%20%23%20existing%20node_pair%0A%20%20%20%20%20%20%20%20%20%20%20%20last_item%20%3D%20self.storage%5Bindex%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20traverse%20through%20LL%20and%20check%20for%20last%20item%20and%20key%20matches%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20hash%28'pear'%29%20%25%2016%20!%3D%20hash%28'apple'%29%20%25%2016%0A%20%20%20%20%20%20%20%20%20%20%20%20while%20last_item.next%20is%20not%20None%20and%20last_item.key%20!%3D%20key%3A%20%20%23%20keep%20going%20until%20at%20end%20or%20keys%20match%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20last_item%20%3D%20last_item.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20the%20key%20matches,%20replace%20the%20value%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20last_item.key%20%3D%3D%20key%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20last_item.value%20%3D%20value%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20else%20insert%20a%20new_node%20at%20the%20end%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20last_item.next%20%3D%20new_node%0A%20%20%20%20%0A%20%20%20%20def%20retrieve%28self,%20key%29%3A%0A%20%20%20%20%20%20%20%20index%20%3D%20self._hash_mod%28key%29%0A%20%20%20%20%20%20%20%20target%20%3D%20self.storage%5Bindex%5D%0A%20%20%20%20%20%20%20%20if%20target%20is%20not%20None%20and%20target.key%20%3D%3D%20key%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20target.value%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20None%0A%20%20%20%20%0A%20%20%20%20def%20remove%28self,%20key%29%3A%0A%20%20%20%20%20%20%20%20index%20%3D%20self._hash_mod%28key%29%0A%20%20%20%20%20%20%20%20if%20self.storage%5Bindex%5D%20is%20not%20None%20and%20self.storage%5Bindex%5D.key%20%3D%3D%20key%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.storage%5Bindex%5D%20%3D%20None%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Warning%3A%20Key%20does%20not%20exist%22%29%0A%0Aht%20%3D%20HashTable%282%29%0Aht.insert%28%22apple%22,%20%22Delicious%22%29%0Aht.insert%28%22pear%22,%20%22Not%20delicious%22%29%0Aht.insert%28%22banana%22,%20%22yummy%22%29%0Aht.insert%28%22apple%22,%20%22cake%22%29%0Aprint%28ht.storage%29%0Aht.retrieve%28%22apple%22%29%0Aprint%28ht.storage%29%0Aht.remove%28%22apple%22%29%0Aprint%28ht.storage%29&cumulative=false&curInstr=84&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
