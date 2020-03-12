from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # set DLL class to storage attribute
        self.storage = DoublyLinkedList()

    # add item to the back of the queue (head <-)
    def enqueue(self, value):
        # increment size when a new item is added
        self.size += 1
        # invoke add_to_head method from DLL class
        self.storage.add_to_head(value)

    # remove and return an item from the front of the queue (tail ->)
    def dequeue(self):
        # check if there are any items to remove
        if self.len() == 0:
            return None
        # decrement size when an item is removed
        self.size -= 1
        # invoke remove_from_tail from DLL class that returns removed value
        self.storage.remove_from_tail()

    # return the number of items in the queue
    def len(self):
        return self.size
