//https://leetcode.com/problems/reverse-linked-list/

// reversed a single linked list
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
// A linked list can be reversed either iteratively or recursively. Could you implement both?

// iteratively 

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
  //                        p   ct
  //                        |
  // null<- 1<- 2<- 3<- 4<- 5  NULL  

// store previous node reference
let prev = null
// use current to traverse LL
let curr = head
while(curr !== null){
  // store next node before changing reference
  temp = curr.next
  // set next node to prev (pointer change)
  curr.next = prev
  // move previous to current's spot
  prev = curr
  // move current along to future spot, saved by previous above
  curr = temp
}
return prev // new head
};

// time O(n) we have to go through the enture list to reverse the pointers
// space O(1) no additional data structure added