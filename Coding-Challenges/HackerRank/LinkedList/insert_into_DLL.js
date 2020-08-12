// given reference to head and a integer data, create a new DoublyLinkedListNode object having data value and insert it into a sorted linked list, while maintaining the sort
// 1 <-> 3 <-> 4 <-> 10 -> null
// after inserting 5
// 1 <-> 3 <-> 4 <-> 5 <-> 10 -> null
// https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?isFullScreen=true

// my initial solution

// * For your reference:
// *
// * DoublyLinkedListNode {
// *     int data;
// *     DoublyLinkedListNode next;
// *     DoublyLinkedListNode prev;
// * }
// *
// */
function sortedInsert(head, data) {
// initialize LL node
let new_node = new DoublyLinkedListNode(data)
// console.log(new_node.data)
let curr = head
// if head is null or head.data is 1 (empty LL or 1 node in LL)
if(curr.data === null || curr.next === null){
   return curr
}
// console.log(curr.next.data)
// traverse through DLL until new node > curr.next
while(curr !== null){
   // console.log(curr.data)
   // inserting at the head
   if(curr.data > data){
       new_node.next = curr
       curr.prev = new_node
       curr = new_node // new head
       return curr
   }
   // inserting at the tail
   else if(curr.next === null){
       curr.next = new_node
       new_node.prev = curr
       break
   }
   else if(curr.next.data > data){
       // found insertion point, manipulate pointers
       // save next value in temp
       let temp = curr.next
       curr.next = new_node
       new_node.prev = curr
       new_node.next = temp
       temp.prev = new_node
       break
   }
curr = curr.next
}
return head // should be at head
// break out of loop when insertion point found
// add new node at curr.next, remember to save curr.next in temp

// once inserted and pointers manipulated go traverse back to head
// using prev -- while curr.prev === None
// return head

}
// another solution from technical training
function sortedInsert(head, data) {
  const newNode = new DoublyLinkedListNode(data);
  // what if head is null
  if(head === null){
    return newNode
  }

  // if it should be inserted at the front, handle that case
  if(data <= head.data){
    newNode.next = head
    head.prev = newNode
    return newNode // new head
  }
    // new.n = head
    // head.prev = new
    // return new (head = new)

let curr = head
while(curr !== null){
  if(curr.data > data){
    // insert before curr.data
   newNode.next = curr 
   curr.prev.next = newNode 
   newNode.prev = curr.prev 
   curr.prev = newNode 
   return head
  }
  if(curr.next === null){
    break
  }
  curr = curr.next
}
// if we get to the end without inserting our node, then we want to insert it at the end
curr.next = newNode
newNode.prev = curr

return head
  // the list is sorted already
  // go through the list and check if data is < > the item
    // if data is >  , then go to the next node
    // if data is < , then we insert it before our current node
      // insertion
  // if we get to the end without inserting our node, then we want to insert it at the end

  // edge cases
    // what if the data is less than the head (beginning)
    // what if the data is = to the value (add >= <= to before or after, it doesn't really matter)
    // what if we need to insert at the very end of the LL (end)
    // what if our list is null
}