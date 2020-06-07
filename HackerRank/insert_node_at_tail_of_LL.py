# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
# You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.
# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    node = head
    # edge cases
    if node == None:  # if head is pointing to Null initial list is empty
        # new_node.next = None
        # node = head
        # setting head to new_node if intial list is empty (head->Null)
        node = new_node
        return node
    # othewise traverse the list
    while(node != None):
        # check to see if we're at the end
        if node.next == None:
            # insert (rearrange pointers)
            node.next = new_node
            new_node.next = None
            # point back to head of list
            node = head
            return node
        # otherwise keep traversing
        node = node.next
