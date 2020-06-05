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
