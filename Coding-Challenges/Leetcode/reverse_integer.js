// https://leetcode.com/problems/reverse-integer/
// given a 32-bit signed integer, reverse digits of an integer
// e.g 123 -> 321
//  -123 -> -321
// 120 -> 21

// assume there's a limit to storing integers within a 32-bit signed integer range. when the reversed integer overflows, or is out of  the 32 bit integer range, return 0.

var reverse = function(x) {
  let reversed = 0
  const max = Math.pow(2,31) //2147483648 // 32 bit integer range
  let y = Math.abs(x) // make digits positive (easy to work with)
  
  while(y > 0){
    // identify digit to pop
    let pop = y % 10; 
    // pop digit from the end, bitwise OR to remove a non-positive int e.g 0.3 | 0 -> 0; 7 | 0 -> 7
    y = y/10 | 0 // bitwise OR operator, if not a positive int, it will return 0
    // adding our popped digit to the first position of our reversed variable 
    reversed = (reversed * 10) + pop
    
    // check out of bounds condition of our 32 bit int  
    if(reversed > max || reversed < -max) return 0  
    }
    // if our x digit was positive to begin with do nothing, else add a negative to the return value
  return x > 0 ? reversed : -reversed
    
}; 