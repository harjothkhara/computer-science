// great explanations - https://leetcode.com/problems/valid-parentheses/

// given a string s containing just the characters '(', ')', '{', '}', '[' and ']' determine if the input string is valid.
// an input string is valid if: 
    // 1. open brackets must be closed by the same type of brackets
    // 2. open brackets must be closed in the correct order

    var isValid = function(s) {
      // stack - LIFO
      
      // parenthesis mapping
    const closing = { 
          ']':'[',
          ')':'(', 
          '}':'{'
          }
  
      // initialize a stack
      let stack = []
      if(s.length === 1) return false
      // loop through each bracket within the string one at a time
      for (let p of s){
        // if we see a closing bracket
          if(closing.hasOwnProperty(p)){
            // check elemement on top of the stack
              // if the opening bracket matches then we pop it if it is non empty
              let top_element = stack.length > 0 ? stack.pop() : '#'
              // closing and opening bracket on stack don't match
              if(closing[p] !== top_element) return false
        // else we have an opening bracket so push onto stack  
            } else {
              stack.push(p)
              }
      }
      // if stack isn't empty - remember we remove all matching brackets from the stack so at the end our stack should be empty
     if(stack.length > 0) return false  
      
      // in the end if the stack is empty, then we have balanced brackets
      return true
  };

  // alternate - better runtime solution
  var isValid = function(s) {
    // use a stack data structure for the correct order
    
    // loop through character string
    // if open parentheses type then add to the stack (deal with them later to find a matching closing parentheses)
        
    // if closing parentheses then we check the the top of the stack for a corresponding open parentheses 
            // if a match is found we pop the open parentheses from the stack

    // empty stack then our input string is valid, we have all matching parentheses 
    
    
    let stack = []
    // edge case - an odd number of char cannot be valid
    if(s.length%2 !== 0 ) return false
    
    for(let i=0; i<s.length; i++){
        // open parenthesis
        if(s[i] === '(' || s[i] === '{' || s[i] === '['){
            stack.push(s[i])
        }
        // closed parenthesis
        else if(s[i] === ')') {
            if(stack[stack.length-1] === '('){ // is it at the top of the stack
                stack.pop()
            }   
            else{
                return false
            }    
        }
        else if(s[i] === '}'){
            if(stack[stack.length-1] === '{'){ // is it at the top of the stack
                stack.pop()
            }   
            else{
                return false
            }    
        }
        else if(s[i] === ']'){
            if(stack[stack.length-1] === '['){ // is it at the top of the stack
                stack.pop()
            }   
            else{
                return false
            }    
        }
    }
    // return true if our stack is empty, we've matched all the open parenetheses and popped them
    return stack.length === 0
    
};
// O(n) time complexity b/c we move through the string one char at a time push and popping operations on a stack O(1) time.
// O(n) as we push all opening brackets onto the stack, worst case we push all brackets on the stack e.g (((((((