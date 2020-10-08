// https://leetcode.com/problems/delete-node-in-a-linked-list/

// write a function to delete a node in a singly LL. You will not be given access to the head of the list, instead you will be given access to the node to deleted directly. It is guaranteed that the node to be deleted is not a tail node in the list.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function(node) {
  // FYI: no need to return from deleted node since program will return from the head once submitted.
  //      n   
  //      |
  // 4 -> 5 -> 1 -> 9
  // 4 -> 1 -> 1 -> 9
  // 4 -> 1 -> 9
  
 // change current node we want to delete to the value of its next node
   node.val = node.next.val
 // set the current node's next value to jump over the next node so we have no duplicates
  node.next = node.next.next
   
};

