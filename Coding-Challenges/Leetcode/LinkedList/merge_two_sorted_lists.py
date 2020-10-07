# https://leetcode.com/problems/merge-two-sorted-lists/

# merge two sorted LL and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # two pointer approach    
        # initiate new node that will stay at the head of the new sorted LL
        temp = ListNode()
            # compare node values as your traverse through both LL and add the smallest node value to new LL
                # if both node values are equal then add them both to the new LL and move pointer along
            # do this until you reach the end of both lists and return the new sorted LL
        
        # to help us traverse
        current = temp
        
        while(l1 is not None and l2 is not None):
            # if the value at the l1 node is < value at the l2 node
            if l1.val < l2.val:
                    # adding current l1 node to our new sorted LL
                    current.next = l1
                    # checked this node in l1 so moving the pointer over to next node in this LL 
                    l1 = l1.next
            else: # default then to node at l2 LL being the smaller value
                    # add current l2 node to our new sorted LL
                    current.next = l2
                    # checked this node in l2 so moving pointer over to next node in this LL
                    l2 = l2.next
            # keep pointer at the end of our new sorted LL
            current = current.next
        
        # edge case: what if the node value in either l1 or l2 is not none?
            # add to the end of out sorted LL since we don't have another LL to compare it to
        if(l1 is not None): 
            # include all remaining nodes from l2's current position to end 
       # [1,1,2,3,4,4 ->   # 6->7->8->9
            current.next = l1  
            l1 = l1.next
        elif(l2 is not None):
            current.next = l2
            l2 = l2.next
            
        return temp.next

# big O is O(n) where n is the length of the smaller of length of l1 or length of l2, in this case, in this example l1 - once we reach the end of l1, we exit loop and insert the remaining nodes in l2 at the end of the sorted list. so we're not iterating through the end of both LL's, just one.

# space is O(n) b/c we're creating a new sorted LL