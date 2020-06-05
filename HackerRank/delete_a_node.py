# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
# DELETE NODE AT KTH POSITION (FROM HEAD)


def deleteNode(self, k):
    node = self.head
    # go to node whose next pointer is k (node we want to delete)
    for i in range(k-1):
        node = node.next
    # set k-1 pointer to point k's next pointer
    node.next = node.next.next
    # reset the head
    node = self.head
    return node

# http://pythontutor.com/live.html#code=class%20Node%3A%20%20%0A%20%20%20%20def%20__init__%28self,%20new_data%29%3A%20%20%0A%20%20%20%20%20%20%20%20self.data%20%3D%20new_data%20%20%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0Aclass%20LinkedList%3A%20%0A%20%20%20%20def%20__init__%28self%29%3A%20%0A%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%20%20%0A%20%20%20%20%23%20createNode%20and%20and%20make%20linked%20list%20%20%0A%20%20%20%20def%20push%28self,%20new_data%29%3A%20%20%0A%20%20%20%20%20%20%20%20new_node%20%3D%20Node%28new_data%29%20%20%0A%20%20%20%20%20%20%20%20new_node.next%20%3D%20self.head%20%20%0A%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%20%20%0A%20%20%0A%20%20%20%20def%20deleteNode%28self,%20k%29%3A%20%0A%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20%23%20go%20to%20node%20whose%20next%20pointer%20is%20k%20%28node%20we%20want%20to%20delete%29%0A%20%20%20%20%20%20%20for%20i%20in%20range%28k-1%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20node.next%0A%20%20%20%20%20%20%20%23%20set%20k-1%20pointer%20to%20point%20k's%20next%20pointer%0A%20%20%20%20%20%20%20node.next%20%3D%20node.next.next%0A%20%20%20%20%20%20%20%23%20reset%20the%20head%0A%20%20%20%20%20%20%20node%20%3D%20self.head%0A%20%20%20%20%20%20%20return%20node%0A%20%20%20%20%20%20%0A%20%20%20%20def%20printList%28self%29%3A%20%0A%20%20%20%20%20%20%20%20tmp_head%20%3D%20self.head%20%0A%20%20%20%20%20%20%20%20while%28tmp_head%20!%3D%20None%29%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28tmp_head.data,%20end%20%3D%20'%20'%29%20%0A%20%20%20%20%20%20%20%20%20%20%20%20tmp_head%20%3D%20tmp_head.next%0A%0Allist%20%3D%20LinkedList%28%29%20%20%0Allist.push%289%29%20%20%0Allist.push%2815%29%20%20%0Allist.push%284%29%20%20%0Allist.push%287%29%0Allist.push%2819%29%0Allist.push%282%29%0Allist.push%286%29%0Allist.push%2820%29%0Aprint%28%22Created%20Linked%20list%20is%3A%22%29%20%0Allist.printList%28%29%20%0Allist.deleteNode%283%29%20%20%0Aprint%28%22%5CnLinked%20List%20after%20Deletion%20is%3A%22%29%20%0Allist.printList%28%29&cumulative=false&curInstr=126&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
