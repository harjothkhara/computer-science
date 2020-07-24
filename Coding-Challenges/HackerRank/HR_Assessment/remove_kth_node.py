# understand - given a linked list 20->19->18->17->16->15->null
# remove the kth node from the end of the LL

 k = 3
 20 -> 19 -> 18 -> 17 -> 16 -> 15 -> null
              |
              k
           (remove)

# return new LL with the kth node removed
20->19->18->16->15->null

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, k): # O(n) - only iterating once through
        first = self.head  # starts at head
        second = self.head # goes to kth node from beginning
        # start by getting the second pointer to kth node (k difference)
        for i in range(k):
            # If count of nodes in the
            # given list is less than 'k'
            # 1) don't change and return original LL
            if(second.next == None): # if current node is the only one
                # and if index = k (this is the intended node we want to delete) then
                # delete the head node
                if(i == k - 1):
                    self.head = self.head.next
                # return LL unchanged if k is longer then length of LL, else return empty LL
                return self.head
            second = second.next # else keep moving second pointer accross until at end of LL
        # next,increment both pointers by one at the same time until second is pointing to last node in LL
        while(second.next != None):
            second = second.next
            first = first.next
        # now first pointer should be pointing to the kth node from the end
        # remove pointer to next node(kth node)to point to kth node next node
        first.next = first.next.next

    def printList(self):
        tmp_head = self.head
        while(tmp_head != None):
            print(tmp_head.data, end = ' ')
            tmp_head = tmp_head.next

llist = LinkedList()
llist.push(11)
llist.push(12)
llist.push(13)
llist.push(14)
llist.push(15)
llist.push(16)
llist.push(17)
llist.push(18)
llist.push(19)
llist.push(20)
print("Created Linked list is:")
llist.printList()
llist.deleteNode(4)
print("\nLinked List after Deletion is:")
llist.printList()

# resources: https://www.geeksforgeeks.org/delete-nth-node-from-the-end-of-the-given-linked-list/

# Brute Force iterations O(n)**2
def deleteNode_fromEnd(self, k): # k = position we want to delete
       node = self.head
       length = 0
       # find the length of LL
       while node:
           length +=1
           node = node.next
       node = self.head # reset node back to beginning
       # check to see if tail node should be delete(k=length-1)
       if k== 0:
          for i in range(length-1-k-1):
                node = node.next
          node.next = node.next.next
          node = self.head
          return node
       # check for deleteing single LL and check if k == length (also,delete the head)
       if length == 1 or length == k:
           node = node.next
           self.head = node
           return node
       # k is greater then length of list
       if k > length:
           return node
       # now we know how long LL is, traverse it and go to k-1 from end
       # go to node whose next pointer is k (node we want to delete)
       # position right before the node we're looking for
       for i in range(length-k-1):
           node = node.next
       # set k-1 pointer to point k's next pointer
       # connect that node with the node two places in front of it
       node.next = node.next.next
       # reset the head
       node = self.head
       return node
