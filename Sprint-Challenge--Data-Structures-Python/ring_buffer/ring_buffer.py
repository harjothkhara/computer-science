from doubly_linked_list import DoublyLinkedList

# When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. - LRU
# FIFO


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # limit
        self.current = None
        self.storage = DoublyLinkedList()  # LL data structure

    # TODO: Your code here
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

        while(node):  # until node = None (end of list)
            # The append() method in python adds a single item to the existing list.
            list_buffer_contents.append(node.value)
            # point to next node in the list until next is None(at the end of list) at which point you exit and return list (line 58)
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


# python tutor walkthrough:

# http://pythontutor.com/visualize.html#code=class%20ListNode%3A%0A%20%20%20%20def%20__init__%28self,%20value,%20prev%3DNone,%20next%3DNone%29%3A%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.prev%20%3D%20prev%0A%20%20%20%20%20%20%20%20self.next%20%3D%20next%0A%20%20%20%20%20%20%20%20%0Aclass%20DoublyLinkedList%3A%0A%20%20%20%20def%20__init__%28self,%20node%3DNone%29%3A%0A%20%20%20%20%20%20%20%20self.head%20%3D%20node%0A%20%20%20%20%20%20%20%20self.tail%20%3D%20node%0A%20%20%20%20%20%20%20%20self.length%20%3D%201%20if%20node%20is%20not%20None%20else%200%0A%0A%20%20%20%20def%20__len__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20self.length%0A%0A%20%20%20%20def%20add_to_head%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20ListNode%28value,%20None,%20None%29%0A%20%20%20%20%20%20%20%20self.length%20%2B%3D%201%0A%20%20%20%20%20%20%20%20if%20not%20self.head%20and%20not%20self.tail%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%20%20%20%20%20%20%20%20%20%20%20%20self.tail%20%3D%20new_node%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20new_node.next%20%3D%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head.prev%20%3D%20new_node%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%0A%20%20%20%20def%20add_to_tail%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20ListNode%28value,%20None,%20None%29%0A%20%20%20%20%20%20%20%20self.length%20%2B%3D%201%0A%20%20%20%20%20%20%20%20if%20not%20self.head%20and%20not%20self.tail%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%20%20%20%20%20%20%20%20%20%20%20%20self.tail%20%3D%20new_node%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20new_node.prev%20%3D%20self.tail%0A%20%20%20%20%20%20%20%20%20%20%20%20self.tail.next%20%3D%20new_node%0A%20%20%20%20%20%20%20%20%20%20%20%20self.tail%20%3D%20new_node%0A%0Aclass%20RingBuffer%3A%0A%20%20%20%20def%20__init__%28self,%20capacity%29%3A%0A%20%20%20%20%20%20%20%20self.capacity%20%3D%20capacity%20%20%23%20limit%0A%20%20%20%20%20%20%20%20self.current%20%3D%20None%0A%20%20%20%20%20%20%20%20self.storage%20%3D%20DoublyLinkedList%28%29%20%23%20LL%20data%20structure%0A%20%20%20%20%0A%20%20%20%20%23%20adds%20elements%20to%20the%20buffer%0A%20%20%20%20def%20append%28self,%20item%29%3A%20%20%0A%20%20%20%20%20%20%20%23%20check%20if%20length%20of%20storage%20is%20zero%20and%20add%20to%20list%0A%20%20%20%20%20%20%20%20if%20len%28self.storage%29%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20it%20is%20set%20new%20item%20to%20head%0A%20%20%20%20%20%20%20%20%20%20%20%20self.storage.add_to_head%28item%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20set%20current%20to%20head%0A%20%20%20%20%20%20%20%20%20%20%20%20self.current%20%3D%20self.storage.head%0A%20%20%20%20%20%20%20%23%20length%20of%20storage%20list%20is%20less%20than%20capacity%0A%20%20%20%20%20%20%20%20elif%20len%28self.storage%29%20%3C%20self.capacity%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20add%20new%20item%20to%20end%20of%20list%20%28tail%29%0A%20%20%20%20%20%20%20%20%20%20%20%20self.storage.add_to_tail%28item%29%0A%20%20%20%20%20%20%20%23%20storage%20list%20is%20at%20capacity%0A%20%20%20%20%20%20%20%20elif%20len%28self.storage%29%20%3D%3D%20self.capacity%3A%0A%20%20%20%20%20%20%20%20%20%23%20check%20if%20self.current.next%20is%20None%20%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20self.current.next%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20replace%20value%20of%20current%28oldest%20item%29%20with%20new%20item%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.current.value%20%3D%20item%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20increment%20the%20current%20item%20to%20next%20node%28new%20oldest%20item%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.current%20%3D%20self.current.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20else%20if%20self.current.next%20is%20not%20None%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20replace%20value%20of%20current%20with%20new%20item%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.current.value%20%3D%20item%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20increment%20the%20current%20item%20back%20to%20beginning%20of%20list%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.current%20%3D%20self.storage.head%0A%0A%20%20%20%20def%20get%28self%29%3A%0A%20%20%20%20%20%20%20%20%23%20returns%20all%20the%20elements%20in%20the%20buffer%20in%20a%20list%20in%20their%20given%20order%0A%20%20%20%20%20%20%20%20%23%20should%20not%20return%20any%20None%20values%20in%20the%20list%20even%20if%20they%20are%20present%20in%20the%20ring%20buffer%0A%20%20%20%20%20%20%20%20%23%20Note%3A%20%20This%20is%20the%20only%20%5B%5D%20allowed%0A%20%20%20%20%20%20%20%20list_buffer_contents%20%3D%20%5B%5D%0A%0A%20%20%20%20%20%20%20%20%23%20TODO%3A%20Your%20code%20here%0A%20%20%20%20%20%20%20%20%23%20start%20at%20beginning%20of%20list%0A%0A%20%20%20%20%20%20%20%20node%20%3D%20self.storage.head%0A%0A%20%20%20%20%20%20%20%20while%28node%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20list_buffer_contents.append%28node.value%29%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20return%20list_buffer_contents%0A%0A%0Aring%20%3D%20RingBuffer%284%29%20%23%20capacity%0Aring.append%28'a'%29%0Aring.append%28'b'%29%0Aring.get%28%29%0Aring.append%28'c'%29%0Aring.append%28'd'%29%0Aring.append%28'e'%29%20%20%23%20overrite%20'a'%0Aring.append%28'f'%29%20%20%23%20overrite%20'b'%0Aring.append%28'g'%29%0Aring.append%28'h'%29%0Aring.append%28'i'%29%0Aring.get%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
