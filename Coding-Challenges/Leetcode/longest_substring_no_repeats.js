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

// optimized solution using a sliding window approach(expanding/shrinking` our window with our 2 pointers) with a hashset
var lengthOfLongestSubstring = function(s) {
    // "abcabcbb"
    let pointerA = 0 // slow pointer (used to pop duplicate)
    let pointerB = 0 // fast pointer will expand the window making sure none of the characters are the same
    let max = 0 // will keep track of when the window is the biggest

    let hashSet = new Set() // add new letters, no duplicates

    while(pointerB < s.length){
      // is the current letter in our longest substring set?
      if(!hashSet.has(s[pointerB])){
        // if not in hashset, then add it
        hashSet.add(pointerB[pointerA])
        // increment pointer
        pointerB++
        // compare size of hashset at current iteration with our max
        max = Math.max(hashSet.size, max) 
      } else {
        // if letter is already in the hashset then pop the last letter from the beginning of hashset (not continguous, so start a new continguous block)
        hashSet.delete(s[pointerB])
        // increment slow pointer
        pointerA++
      }
    } 
  return max
};