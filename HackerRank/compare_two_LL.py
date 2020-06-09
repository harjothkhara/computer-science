# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?isFullScreen=true

# You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. The lists are equal only if they have the same number of nodes and corresponding nodes contain the same data. Either head pointer given may be null meaning that the corresponding list is empty.

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    a = llist1
    b = llist2
    # since either head pointer may be null, doing the check
    # to make sure atleast one head pointer has a data value.
    # 'and' instead of the 'or' assumes all nodes have some data 
    while(a != None or b != None): 
        # checking specifc data and null cases between the two head pointers
        if a is None and b is not None:
            return 0
        if b is None and a is not None:
            return 0
        # if both nodes are !None, then check if the data nodes are equal
        if a.data != b.data:
            return 0
        # data nodes are equal so keep on traversing the list
        a = a.next
        b = b.next
    # if we break out of loop then all nodes in the two lists are equal,           including two nulls.
    return 1

    # python tutor http://pythontutor.com/live.html#code=class%20Node%3A%0A%20%20%20%20def%20__init__%28self,%20new_data%29%3A%0A%20%20%20%20%20%20%20%20self.data%20%3D%20new_data%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0Aclass%20LinkedList%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%20%20%20%20%20%20%20%20%23%20self.position%20%3D%20None%0A%0A%20%20%20%20%23%20createNode%20and%20and%20make%20linked%20list%0A%20%20%20%20def%20push%28self,%20new_data%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20Node%28new_data%29%0A%20%20%20%20%20%20%20%20new_node.next%20%3D%20self.head%0A%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%20%20%20%20%0A%20%20%20%20def%20compare_lists%28self,llist2%29%3A%0A%20%20%20%20%20%20%20%20a%20%3D%20self.head%20%23%20pointer%20to%20head%20of%20LL%20instance%0A%20%20%20%20%20%20%20%20b%20%3D%20llist2.head%20%23%20pointer%20to%20head%20of%20LL2%20instance%0A%20%20%20%20%20%20%20%20%23%20a%20and%20b%20both%20point%20to%20individual%20Node%20instance%0A%20%20%20%20%20%20%20%20while%28a%20!%3D%20None%20or%20b%20!%3D%20None%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20one%20is%20data%20node%20is%20Null%20and%20the%20other%20isn't%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20a%20is%20None%20and%20b%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20b.data%20is%20None%20and%20a.data%20is%20not%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20node%20data%20values%20are%20different%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20a.data%20!%3D%20b.data%3A%20%23%20Node%3Adata,next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20node%20is%20same,%20carry%20on%20traversing%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20a%20%3D%20a.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20b%20%3D%20b.next%0A%20%20%20%20%20%20%20%20%23%20if%20both%20data%20nodes%20are%20equal%20including%0A%20%20%20%20%20%20%20%20%23%20two%20that%20are%20None%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20printList%28self%29%3A%0A%20%20%20%20%20%20%20%20tmp_head%20%3D%20self.head%0A%20%20%20%20%20%20%20%20while%28tmp_head%20!%3D%20None%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28tmp_head.data,%20end%20%3D%20'%20'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20tmp_head%20%3D%20tmp_head.next%0A%0Allist%20%3D%20LinkedList%28%29%0Allist2%20%3D%20LinkedList%28%29%0Allist2.push%28None%29%0Allist2.push%281%29%0Allist.push%28None%29%0Allist.push%282%29%0Allist.push%281%29%0Allist.compare_lists%28llist2%29%0A&cumulative=false&curInstr=74&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false