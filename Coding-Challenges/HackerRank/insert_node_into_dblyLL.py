# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?isFullScreen=true
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None


class Dbly_LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

   # how do we figure out where to insert the node?
     #  traverse the LL, compare the values with our 'data'. If data is less than
     #  node value, then we know we want to insert it before this node
     #  to insert, follow the diagram

    # edge cases
        #  duplicate values -> we're already covered here
        #  if prev == null (we want to insert before the head) ->
            #  check if we have a prev
            #  set dataNode = current.prev
            #  dataNode.next = current
        #  we need to insert after the tail -->
            ##
        #  empty list (head == null) -> return (dataNode)

    def sortedInsert(self,data):
        node = self.head
        new_node = Node(data)
        new_node.data = data

        # check for empty
        if node.data == None:
            return node
        # check if data is less then head
            # insert to beggining
        if node.data >= new_node.data:
            node.prev = new_node
            new_node.next = node
            self.head = new_node
            return self.head
        # data is greater then head keep traversing
        while(node != None): # node not at None
            if new_node.data < node.data:
                node.prev.next = new_node
                new_node.prev = node.prev
                new_node.next = node
                node.prev = new_node
                node = head
                return node
            # handle adding new node to end of LL
            if node.next == None:
                node.next = new_node
                new_node.prev = node
                return self.head
            node = node.next
        return head

    def printList(self):
        tmp_head = self.head
        while(tmp_head != None):
            print(tmp_head.data, end = ' ')
            tmp_head = tmp_head.next

llist = Dbly_LinkedList()
# llist.push(11)
# llist.push(12)
# llist.push(13)
# llist.push(14)
# llist.push(5)
# llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("Created Linked list is:")
llist.printList()
print("\nLinked List after Deletion is:")
llist.printList()
