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