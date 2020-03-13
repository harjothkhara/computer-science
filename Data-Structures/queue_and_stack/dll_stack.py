import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()  # tracking storage in here

# stack is last in first out

    # adding a new node to the list (end of stack) <->H
    def push(self, value):
        self.storage.add_to_head(value)  # could also use add_to_tail

    # remove last node in from list and return its value (last item in stack is the fist one out)
    def pop(self):
        return self.storage.remove_from_head()  # could also use remove_from_tail

    def len(self):
        return self.storage.length
