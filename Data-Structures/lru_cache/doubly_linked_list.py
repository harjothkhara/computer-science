"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
# core - our node!


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

# manager of nodes


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):  # returns a string
        pass
        if self.head is None and self.tail is None:
            return "empty"
        curr_node = self.head
        # " (3) <-> (5) <-> ..."
        output = ''
        output += f'( {curr_node.value} ) <-> '  # head (3) <->
        while curr_node.next is not None:  # if there's something to go to
            curr_node = curr_node.next  # if there's another node
            output += f'( {curr_node.value} ) <-> '
        return output

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # adding to an empty list - case 1
        # create a new node
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.next = self.head  # old head. pointer L -> R
            self.head.prev = new_node  # pointer  L <- R
            # update head
            self.head = new_node  # new head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):  # similar to pop method in an array
        # if list is empty
        if self.head is None and self.tail is None:
            return
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # adding to an empty list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail  # same as add_to_head except we work backwards
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # already at head
        if node is self.head:
            return
        # otherwide delete node at current location
        self.delete(node)
        # move node to head
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):  # LRU position
        # already at tail
        if node is self.tail:
            return
        # otherwise delete node at current position
        self.delete(node)
        # move node to tail
        self.add_to_tail(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail. """

    def delete(self, node):
        self.length -= 1
        # only 1 item in list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # item at head
        elif self.head == node:
            self.head = self.head.next
            node.delete()
        # item at tail
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()
        # item in middle
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass


# instance of class
our_dll = DoublyLinkedList()
print(our_dll)
# running class method
our_dll.add_to_head(5)
print(our_dll)
our_dll.add_to_head(3)
print(our_dll)
our_dll.add_to_head(7)
print(our_dll)
our_dll.add_to_head(8)
print(our_dll)
our_dll.add_to_tail(1)
print(our_dll)
removed_val = our_dll.remove_from_head()
print(removed_val)  # print removed head
print(our_dll)  # with head value removed
removed_val = our_dll.remove_from_tail()
print(removed_val)  # print removed tail
print(our_dll)  # with tail value removed
