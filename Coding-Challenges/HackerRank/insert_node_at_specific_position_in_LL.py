# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?isFullScreen=true
# You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which the integer must be inserted. Create a new node with the given integer, insert this node at the desired position and return the head node.

# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.


def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    node = head  # eventually goes to position - 1 once we finish traversing below

# additional edge cases not in problem---------------:
    length = 0
    # find length of LL:
    while(node != None):
        length += 1
        node = node.next
    node = head  # reset back to head

    # if position is > LL:
    if position > length:
        return head
    # if head is null
    if node == None and position > 1:
        return head
    # if head node is null and inserting at first position
    if node == None and position == 1:
        head = new_node
# additional edge cases not in problem---------------:

# index LL to one before the insertion point (tells us how far along we need to traverse)
    for i in range(position-1):  # 0(head),1,2,3, i == position - 1
        # keep traversing if not at position - 1
        node = node.next

    # now node is at position -1 we can start the insertion:
    new_node.next = node.next
    node.next = new_node
    node = head
    return node

# python tutor: http://pythontutor.com/live.html#code=class%20Node%3A%0A%20%20%20%20def%20__init__%28self,%20new_data%29%3A%0A%20%20%20%20%20%20%20%20self.data%20%3D%20new_data%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0Aclass%20LinkedList%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%20%20%20%20%20%20%20%20self.position%20%3D%20None%0A%0A%20%20%20%20%23%20createNode%20and%20and%20make%20linked%20list%0A%20%20%20%20def%20push%28self,%20new_data%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20Node%28new_data%29%0A%20%20%20%20%20%20%20%20new_node.next%20%3D%20self.head%0A%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%0A%20%20%20%20def%20deleteNode%28self,%20k%29%3A%20%23%20O%28n%29%20-%20only%20iterating%20once%20through%0A%20%20%20%20%20%20%20%20first%20%3D%20self.head%20%20%23%20starts%20at%20head%0A%20%20%20%20%20%20%20%20second%20%3D%20self.head%20%23%20goes%20to%20kth%20node%20from%20beginning%0A%20%20%20%20%20%20%20%20%23%20start%20by%20getting%20the%20second%20pointer%20to%20kth%20node%20%28k%20difference%29%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28k%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20If%20count%20of%20nodes%20in%20the%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20given%20list%20is%20less%20than%20'k'%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%201%29%20don't%20change%20and%20return%20original%20LL%0A%20%20%20%20%20%20%20%20%20%20%20%20if%28second.next%20%3D%3D%20None%29%3A%20%23%20if%20current%20node%20is%20the%20only%20one%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20and%20if%20index%20%3D%20k%20%28this%20is%20the%20intended%20node%20we%20want%20to%20delete%29%20then%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20delete%20the%20head%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%28i%20%3D%3D%20k%20-%201%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20self.head.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20return%20LL%20unchanged%20if%20k%20is%20longer%20then%20length%20of%20LL,%20else%20return%20empty%20LL%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20second%20%3D%20second.next%20%23%20else%20keep%20moving%20second%20pointer%20accross%20until%20at%20end%20of%20LL%0A%20%20%20%20%20%20%20%20%23%20next,increment%20both%20pointers%20by%20one%20at%20the%20same%20time%20until%20second%20is%20pointing%20to%20last%20node%20in%20LL%0A%20%20%20%20%20%20%20%20while%28second.next%20!%3D%20None%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20second%20%3D%20second.next%0A%20%20%20%20%20%20%20%20%20%20%20%20first%20%3D%20first.next%0A%20%20%20%20%20%20%20%20%23%20now%20first%20pointer%20should%20be%20pointing%20to%20the%20kth%20node%20from%20the%20end%0A%20%20%20%20%20%20%20%20%23%20remove%20pointer%20to%20next%20node%28kth%20node%29to%20point%20to%20kth%20node%20next%20node%0A%20%20%20%20%20%20%20%20first.next%20%3D%20first.next.next%0A%20%20%20%20%0A%20%20%20%20def%20insertNodeAtPosition%28self,%20data,%20position%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20Node%28data%29%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%20%23%20eventually%20goes%20to%20position%20-%201%20once%20we%20finish%20traversing%20below%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20length%20%3D%200%0A%20%20%20%20%20%20%20%20%23%20find%20length%20of%20LL%0A%20%20%20%20%20%20%20%20while%28node%20!%3D%20None%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20length%20%2B%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%20%23%20reset%20back%20to%20head%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20if%20position%20is%20%3E%20LL%0A%20%20%20%20%20%20%20%20if%20position%20%3E%20length%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20if%20head%20node%20is%20null%0A%20%20%20%20%20%20%20%20if%20node%20%3D%3D%20None%20and%20position%20%3E%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20return%20self.head%0A%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20if%20head%20node%20is%20null%20and%20inserting%20at%20first%20position%0A%20%20%20%20%20%20%20%20if%20node%20%3D%3D%20None%20and%20position%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20for%20i%20in%20range%28position%20-1%29%3A%20%0A%20%20%20%20%20%20%20%20%23%20keep%20traversing%20if%20not%20at%20position%20-%201%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20now%20node%20is%20at%20position%20-1%20we%20can%20start%20the%20insertion%3A%0A%20%20%20%20%20%20%20%20new_node.next%20%3D%20node.next%0A%20%20%20%20%20%20%20%20node.next%20%3D%20new_node%0A%20%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%20return%20node%0A%0A%20%20%20%20def%20printList%28self%29%3A%0A%20%20%20%20%20%20%20%20tmp_head%20%3D%20self.head%0A%20%20%20%20%20%20%20%20while%28tmp_head%20!%3D%20None%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28tmp_head.data,%20end%20%3D%20'%20'%29%0A%20%20%20%20%20%20%20%20%20%20%20%20tmp_head%20%3D%20tmp_head.next%0A%0Allist%20%3D%20LinkedList%28%29%0A%23%20llist.push%2811%29%0A%23%20llist.push%2812%29%0A%23%20llist.push%2813%29%0A%23%20llist.push%2814%29%0A%23%20llist.push%2815%29%0A%23%20llist.push%2816%29%0A%23%20llist.push%28382%29%0A%23%20llist.push%287%29%0Allist.push%2813%29%0Allist.push%2816%29%0Aprint%28%22Created%20Linked%20list%20is%3A%22%29%0Allist.printList%28%29%0A%23%20llist.deleteNode%284%29%0Allist.insertNodeAtPosition%281,10%29%20%23%20data,%20position%0Aprint%28%22%5CnLinked%20List%20after%20Deletion%20is%3A%22%29%0Allist.printList%28%29&cumulative=false&curInstr=58&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
