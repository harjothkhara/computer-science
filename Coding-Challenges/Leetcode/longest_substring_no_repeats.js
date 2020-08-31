// https://leetcode.com/problems/longest-substring-without-repeating-characters/

// given a string, find the length of the longest substring without repeating characters
// e.g input: "abcabcbb" -> 3
//  The answer is "abc", with the length of 3. 

// initial o(n**2) solution
var lengthOfLongestSubstring = function(s) {
  // goal: longest substring that is contiguous (unlike a subsequence) without any repeating characters
  
  // loop through every letter in the string and if its continguous and not a duplicate then add it to the longest substring variable. return the length of longest substring variable

  // count variable that tracks length of longest substring
  
  // longest substring variable
  
  // outer loop to track where substring starts (i)
      // reset longest substring to ""
      // inner loop to track where substring finishes (i+1)
          // check if letter is already in longest substring variable, if so, check/update length
                  // if length of substring is greater then count then we update count to new length
          // else, add letter to substring variable
  // return length of longest substring variable
             
  // "pwwkew""
  let count = 0
  let longestSubstring = ""
  
  if(s.length === 1) return 1
  
  for(let i=0; i<s.length; i++){
      longestSubstring = ""
      longestSubstring += s[i]
      for(j=i+1; j<s.length; j++){ 
          if(longestSubstring.includes(s[j])){
              if(count < longestSubstring.length){
                  count = longestSubstring.length
              }
              break
          } else {
               longestSubstring += s[j]
               if(j === s.length-1 ){
                if(count < longestSubstring.length){
                   count = longestSubstring.length
                 }  
               }
          }
      }
  }
  return count
};

// time - O(n**2)
// space - O(n)

