// Given a singly linked list, determine if its is a palindrome(same word backwards: e.g racecar -> racecar)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
//  *     this.val = (val===undefined ? 0 : val)
//  *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
// space O(n)
// time O(n)
// my solution:
var isPalindrome = function (head) {
  // convert the LL to a string(O(n), then compare string to string reverse(O(n). Create a string O(n) space

  let currentNode = head;
  let linkedlistArr = [];
  while (currentNode !== null) {
    linkedlistArr.push(currentNode.val);
    currentNode = currentNode.next;
  }
  const rev = [...linkedlistArr].reverse();

  for (let i = 0; i < linkedlistArr.length; i++) {
    if (linkedlistArr[i] !== rev[i]) return false;
  }
  return true;
};
// [10,10] -> true
// "1010" -> reverse -> "0101" -> false
