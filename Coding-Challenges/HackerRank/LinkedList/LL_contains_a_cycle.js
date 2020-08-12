// A LL contains a cycle if a node is visited more than once while traversing the list. Given a pointer to a node object names head that
// points to the head of a LL, your function must return 'true' if it contains a cycle, or 'false' if it does not.
// https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

// This HR problem does not work in JS, had to convert to python to pass tests in HR.
function hasCycle(head) {
  // edge cases
  // is each value unique? 1 -> 2 -> 3 -> 3
      // covered if we just store the node instead of data
  // what if head is null?
      // return false
  if(head === null) return false;
  // keep track of visited node
      // we could use a set for this (key)
      // we could use an object for this
          // key -> value
          // node -> true/false
  const visited = new Set();

  let curr = head
  // traverse the LL, 
  while(curr !== null){
      // check if we hit an already visited node
      if(visited.has(curr)){ // if visited has our current node
      // if yes return true
      // keep track of visited nodes
          return true
      }
      visited.add(curr) // adding current node to visited
      // keep on traversing
      curr = curr.next 
  }
  return false
}

// Python Solution
def has_cycle(head):
    // # keep track of visited node
  visited = set()
  node = head
  // # edge case: if head is null
  // # traverse LL
  while node is not None:
    // # check if node has been visited, if so return True - we found a cycle!
    if node in visited:
      return True
    // # if not visited, add it as visited
    visited.add(node)
    // # and keep on traversing to next node in list
    node = node.next

  // # if after traversing to end of list where node is None
  // # it means there's no cycle
  return False
