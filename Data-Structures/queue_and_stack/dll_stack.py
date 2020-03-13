import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()  # tracking storage in here

# stack is last in first out

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
