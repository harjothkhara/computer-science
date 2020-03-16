from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# Least Recently Used Strategy - the oldest entry (the one that was added/updated the longest time ago) is removed to make space for the new entry. Resource: https://www.interviewcake.com/concept/java/lru-cache

# Using a DLL (Doubly Linked List) data structure with the most recently used item at the head and the least recently used item at the tail - O(1) operation. Traversing and accessing an item in the linked list will be O(n) since we need to walk through the whole list.


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit  # max # of nodes held
        self.size = 0  # current # of nodes holding
        self.dll = DoublyLinkedList()  # holding key/value entries in the correct order
        # storage dict that provides fast access to every node stored in the cache
        self.storage = {}


# fetches a value given a key. when a key-value is fetched from the cache, we'll go through the same priority increase dance that also happens when a new pair is added to the cache
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used (MRU - front)
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
# Retrieve a node with the matching key to the front

    def get(self, key):
        if key in self.storage:
            # return the value and move to front
            node = self.storage[key]
            # move the key-value pair to the end of the order (MRU)
            self.dll.move_to_end(node)
            # return value associated with the key
            return node.value[1]
        # or return None if key-value pair doesn't exist in cache
        else:
            return None

# set operation on our cache to add key-value pairs to the cache. Lowest priority pair will get removed from the cache if the cache is already at its max capacity. If key already exists in cache, we overwrite the old value associated with the key the new value.
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check if key already exists
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            # moving most-recently used entry in the cache to the end
            return self.dll.move_to_end(node)
        # if cache is at max capacity then oldest entry needs to be removed
        elif self.size == self.limit:
            # if at size limit remove LRU from cache
            del self.storage[self.dll.head.value[0]]
            # and from DLL - similar to pop method
            self.dll.remove_from_head()
            #  decrease the size of the list
            self.size -= 1
        # if key already exists in the cache, we simply
        # want to overwrite the old value associated with the key with
        # the newly-specified value.
        self.dll.add_to_tail((key, value))
        # store item in dict with key
        self.storage[key] = self.dll.tail
        # increase size
        self.size += 1
