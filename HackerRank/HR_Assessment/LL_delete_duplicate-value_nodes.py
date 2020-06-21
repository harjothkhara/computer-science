# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
# You're given the pointer to the head node of a sorted linked list, where the data in the nodes is in ascending order. Delete as few nodes as possible so that the list does not contain any value more than once. The given head pointer may be null indicating that the list is empty.

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def removeDuplicates(head):
    # both pointers start at head
    pointer1 = head
    pointer2 = head
    # move pointer 2 one step ahead
    pointer2 = pointer2.next
    # pointer 1 moves to next node and checks if its the same as pointer2
    while(pointer2 is not None):
        # if the same -- we have a duplicate
        if pointer1.data == pointer2.data:
            # if p1 next is None
            if pointer1.next is None:
                temp = pointer1
                pointer1.next = temp
                pointer2.next = None
        # else, move pointer2 to next node and set pointer1 next to pointer2
            pointer2 = pointer2.next
            pointer1.next = pointer2
    # if not duplicate, move pointer1 and pointer2 by one and check again
    # for duplicates
        elif pointer1.data is not pointer2.data:
            if pointer1.next is not None:
                pointer1 = pointer1.next
                pointer2 = pointer2.next
# we exit our loop and stop traversing once pointer2's next is None
# set current back to head and return head node
    pointer2 = head
    return pointer2
