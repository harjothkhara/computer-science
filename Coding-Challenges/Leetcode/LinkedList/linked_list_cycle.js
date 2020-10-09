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