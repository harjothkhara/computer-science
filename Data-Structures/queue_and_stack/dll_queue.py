from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# FIFO First in first out


class Queue:
    def __init__(self):
        self.size = 0
        # set DLL class to storage attribute
        self.storage = DoublyLinkedList()

    # add item to the back of the queue (head <-)
    def enqueue(self, value):
        # increment size when a new item is added
        self.size += 1
        # invoke add_to_tail method from DLL class
        self.storage.add_to_tail(value)

    # remove and return an item from the front of the queue (tail ->)
    def dequeue(self):
        # check if there is anyone in the queue
        if self.size == 0:
            return
        # decrement size when an a queue item is removed
        else:
            self.size -= 1
        # invoke remove_from_head from DLL class that returns removed value
            return self.storage.remove_from_head()

    # return the number of items in the queue
    def len(self):
        return self.size
