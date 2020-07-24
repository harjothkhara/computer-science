# You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on.
# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
# TWO POINTER METHOD 
# - set both pointers to head
# - move pointer 1 n nodes from head (pretend the head is the tail)
# - move both pointer 1 and 2 by one until pointer 1 reaches the end of LL (tail)
# - now pointer 2 will be at the nth position from the tail
def getNode(head, positionFromTail):
   # 2 pointers - set both pointers to head to begin
   pointer1 = head
   pointer2 = head
   # check if our LL is empty
   if head is not None:
    # check if we have more than one node in LL
    if head.next is not None: 
      # move pointer1 n nodes from head
      for i in range(positionFromTail): # 0(head),1, 2 ...(positinFromTail) 
        pointer1 = pointer1.next
        # pointer1 is now n nodes from head
        
        # move both pointers one by one until pointer one's next value is None 
        # (tail reached!)
      while(pointer1.next is not None):
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        # now pointer 1 should be at tail
        # now pointer 2 should be n positions away from tail - return node value
   return pointer2.data


# USING LENGTH OF LL
# - count the length of the LL by traversing to the end
# - then subtract the position from tail from the length subtracting  -1 to not include the tail node and traverse to exact node from the tail!
#  - return node value 

def getNode(head, positionFromTail):
 # count the length of LL
 length = 0
 curr = head
 while(curr is not None):
    length +=1
    curr = curr.next
 # reset curr back to head   
 curr = head
# traverse to nth position from tail
 # subtract nth tail position from length of LL not including tail
 for i in range(length-positionFromTail-1): # 4(head), 3, 2, 1(tail)
    curr = curr.next                              #    <-  <-
# curr should be at nth position from tail
# return node value at nth position from tail
 return curr.data

   # http://pythontutor.com/live.html#code=class%20Node%3A%0A%20%20%20%20def%20__init__%28self,%20new_data%29%3A%0A%20%20%20%20%20%20%20%20self.data%20%3D%20new_data%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0Aclass%20LinkedList%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%0A%20%20%20%20%23%20createNode%20and%20and%20make%20linked%20list%0A%20%20%20%20def%20push%28self,%20new_data%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20Node%28new_data%29%0A%20%20%20%20%20%20%20%20new_node.next%20%3D%20self.head%0A%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%0A%20%20%20%20def%20deleteNode%28self,%20k%29%3A%20%23%20O%28n%29%20-%20only%20iterating%20once%20through%0A%20%20%20%20%20%20%20%20first%20%3D%20self.head%20%20%23%20starts%20at%20head%0A%20%20%20%20%20%20%20%20second%20%3D%20self.head%20%23%20goes%20to%20kth%20node%20from%20beginning%0A%20%20%20%20%20%20%20%20%23%20start%20by%20getting%20the%20second%20pointer%20to%20kth%20node%20%28k%20difference%29%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28k%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20If%20count%20of%20nodes%20in%20the%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20given%20list%20is%20less%20than%20'k'%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%201%29%20don't%20change%20and%20return%20original%20LL%0A%20%20%20%20%20%20%20%20%20%20%20%20if%28second.next%20%3D%3D%20None%29%3A%20%23%20if%20current%20node%20is%20the%20only%20one%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20and%20if%20index%20%3D%20k%20%28this%20is%20the%20intended%20node%20we%20want%20to%20delete%29%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20delete%20the%20head%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%28i%20%3D%3D%20k%20-%201%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20self.head.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20return%20LL%20unchanged%20if%20k%20is%20longer%20then%20length%20of%20LL,%20else%20return%20empty%20LL%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20second%20%3D%20second.next%20%23%20else%20keep%20moving%20second%20pointer%20accross%20until%20at%20end%20of%20LL%0A%20%20%20%20%20%20%20%20%23%20next,increment%20both%20pointers%20by%20one%20at%20the%20same%20time%20until%20second%20is%20pointing%20to%20last%20node%20in%20LL%0A%20%20%20%20%20%20%20%20while%28second.next%20!%3D%20None%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20second%20%3D%20second.next%0A%20%20%20%20%20%20%20%20%20%20%20%20first%20%3D%20first.next%0A%20%20%20%20%20%20%20%20%23%20now%20first%20pointer%20should%20be%20pointing%20to%20the%20kth%20node%20from%20the%20end%0A%20%20%20%20%20%20%20%20%23%20remove%20pointer%20to%20next%20node%28kth%20node%29to%20point%20to%20kth%20node%20next%20node%0A%20%20%20%20%20%20%20%20first.next%20%3D%20first.next.next%0A%20%20%20%20%0A%20%20%20%20def%20getNode%28self,head,%20positionFromTail%29%3A%0A%20%20%20%20%20%20%20%20pointer1%20%3D%20self.head%0A%20%20%20%20%20%20%20%20pointer2%20%3D%20self.head%0A%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20if%20pointer1.next%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20for%20i%20in%20range%28positionFromTail%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20pointer1%20%3D%20pointer1.next%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20while%28pointer1.next%20is%20not%20None%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20pointer1%20%3D%20pointer1.next%0A%20%20%20%20%20%20%20%20%20%20%20%20pointer2%20%3D%20pointer2.next%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20pointer2.data%0A%0A%20%20%20%20def%20printList%28self%29%3A%0A%20%20%20%20%20%20%20%20tmp_head%20%3D%20self.head%0A%20%20%20%20%20%20%20%20while%28tmp_head%20!%3D%20None%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28tmp_head.data,%20end%20%3D%20'%20'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20tmp_head%20%3D%20tmp_head.next%0A%0Allist%20%3D%20LinkedList%28%29%0Allist.push%281%29%0A%23%20llist.push%282%29%0A%23%20llist.push%283%29%0A%23%20llist.push%284%29%0Allist.getNode%281,%202%29%0Aprint%28%22Created%20Linked%20list%20is%3A%22%29%0Allist.printList%28%29%0A%23%20llist.deleteNode%284%29%0Aprint%28%22%5CnLinked%20List%20after%20Deletion%20is%3A%22%29%0Allist.printList%28%29&cumulative=false&curInstr=21&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false