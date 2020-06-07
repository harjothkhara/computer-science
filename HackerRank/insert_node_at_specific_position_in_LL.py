# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?isFullScreen=true
# You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted. Create a new node with the given integer, insert this node at the desired position and return the head node.

# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.


def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    node = head  # eventually goes to position - 1 once we finish traversing below

# index LL to one before the insertion point (tells us how far along we need to traverse)
    for i in range(position-1):  # 0(head),1,2,3, i == position - 1
        # keep traversing if not at position - 1
        node = node.next

    # now node is at position -1 we can start the insertion:
    new_node.next = node.next
    node.next = new_node
    node = head
    return node
