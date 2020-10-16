// Write a function that reverses a string. The input string is given as an array of characters char[].

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

// You may assume all the characters consist of printable ascii characters.

// https://leetcode.com/problems/reverse-string/

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
        
  //    |      
  // [a,p,p,l,e] ->  [e,l,p,p,a]
  //            |
         
 // in-place sort
             
   let left = 0
   let right = s.length-1 
 
   while(left < right){
     let temp = s[left]
     s[left]=s[right] 
     s[right] = temp
     left++
     right--
 }
 return s
                 
};

  //          |      
  // [a,p,p,l,e,s] ->  [s,e,l,p,p,a]
  //        |