from doubly_linked_list import DoublyLinkedList

# When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. - LRU


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # limit
        self.current = None
        self.storage = DoublyLinkedList()  # LL data structure

    # adds elements to the buffer
    def append(self, item):
       # check if length of storage is zero and add to list
        if len(self.storage) == 0:
            # if it is set new item to head
            self.storage.add_to_head(item)
            # set current to head
            self.current = self.storage.head
       # length of storage list is less than capacity
        elif len(self.storage) < self.capacity:
            # add new item to end of list (tail)
            self.storage.add_to_tail(item)
       # storage list is at capacity
        elif len(self.storage) == self.capacity:
         # check if self.current.next is not None, i.e node has a next value
            # if self.current.next is not None
            if self.current.next:
                # replace value of current(oldest item) with new item
                self.current.value = item
                # increment the current item to next node(new oldest item)
                self.current = self.current.next
            #  if self.current.next is None, i.e current is at end of list, no next value
            else:
                # replace value of current with new item
                self.current.value = item
                # increment the current item back to beginning of list
                self.current = self.storage.head

    def get(self):
        # returns all the elements in the buffer in a list in their given order
        # should not return any None values in the list even if they are present in the ring buffer
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # start at beginning of list

        node = self.storage.head

        while(node):
            list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents


ring = RingBuffer(4)  # capacity
ring.append('a')
ring.append('b')
ring.append('c')
ring.append('d')
ring.append('e')  # overrite 'a'
ring.append('f')  # overrite 'b'
ring.append('g')  # overrite 'c'
ring.append('h')  # overrite 'd' - self.current.next = None

ring.append('i')  # overrite 'e'
ring.append('j')  # overrite 'f'


print(ring.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
