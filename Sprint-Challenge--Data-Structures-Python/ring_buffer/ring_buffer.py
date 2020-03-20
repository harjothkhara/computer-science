from doubly_linked_list import DoublyLinkedList

# When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. - LRU


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # limit
        self.current = None
        self.storage = DoublyLinkedList()  # cache

    def append(self, item):  # adds elements to the buffer
       # check if length of storage is zero

       # length of storage list is less than capacity
            # add new item to the tail of list

       # storage list is at capacity
         # check if self.current.next is None

    def get(self):
        # returns all the elements in the buffer in a list in their given order
        # should not return any None values in the list even if they are present in the ring buffer
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
