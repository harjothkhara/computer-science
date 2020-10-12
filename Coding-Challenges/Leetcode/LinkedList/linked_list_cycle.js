// https://leetcode.com/problems/linked-list-cycle/
// given the head of a LL, determine if the LL has a cycle in it.
  // there is a cycle in a LL if there is some node on the list that can be reached again by continuously following the next pointer. internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
  // pos is note passed as a parameter.

Input: head = [3,2,0,-4], pos = 1
                 |    |
                 <----|
{/* Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed). */}

var hasCycle = function(head) {
    // trying to see where the same node in a LL is visited more than once i.e if the pointer from the tail of a LL goes back to previously visited node (cycle!)
   // return true if there is a cycle, otherwise false. 
    
   // head 
   //   |
   //   3 -> 2 -> 0 -> -4
   //        ^          ↓
   //        |          |
   //        - -  -  -  |
   
  // traverse down the LL and keep track of each node visited
         // upon arriving at a new node, we check to see if the node has been visited
         // if it has, then we have a cycle so we return true
         // else we add node to our visited set and keep traversing

    // 1. using a hashtable     
    let visited =  new Set() // (uniqiue) node: val, next 
    let curr = head
    while(curr !== null){
        if(visited.has(curr)){
            return true
        }
        visited.add(curr)
        curr = curr.next
    }
    return false
};
// fyi: duplicate nodes are ok, just make sure we don't revisit the same node 
        // internally: (pos => index of node)

  // 2. using a two pointer approach
  var hasCycle = function(head) {
    // 2 pointers approach - fast runner and a slow runner
        // fast runner will move 2 nodes at a time where as the slow runner will move 1 node at a time. if its a cycle, eventually the fast runner will catch the slow runner and both will be equal (cycle)
    
    // head 
    //  s    f 
    //  |    |              
    //  3 -> 2 -> 0 -> -4
    //       ^          ↓
    //       |          |
    //       - -  -  -  |
    
    // edge case: an empty LL []
    if(head === null) return false
    
    let slow = head
    let fast = head.next
    
    // if slow === fast (both at the same node, we have a loop!)
    while(slow !== fast){
        // [1]              [1,2]
        if(fast === null || fast.next === null) return false
                                          // |  |
        // else move both pointer along [1,2,3]
        slow = slow.next // move over by 1
        fast = fast.next.next  // move over by 2
    }
    return true // we have a cycle!
};