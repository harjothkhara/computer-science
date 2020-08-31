// https://leetcode.com/problems/longest-common-prefix/
// find the longest common prefix (beginning of word) amongst an array of strings
// if there is not common prefix, return an empty string ""
// e.g ["flower","flow","flight"] -> ''fl

var longestCommonPrefix = function(strs) {
  // handling an empty array case
  if(strs.length === 0) return ""
  // add first word in array as our prefix word to compare to others
  let firstPrefix = strs[0] // common prefix
  // 'flower'
  
  // loop through each word in the array starting with the second word
  for(let i=1; i<strs.length; i++){
      // ['flow']
      // check if firstPrefix word exists in current word in array
      // if not, we will slice down our firstPrefix word by 1 and continue looping until there's a match. while we cannot find this prefix at the beginning of this string we will decrease size of string
      while(strs[i].indexOf(firstPrefix) !== 0){ // if not the first letter in the string (prefix)
          firstPrefix = firstPrefix.slice(0, firstPrefix.length-1)
      }   // flower -> flowe -> flow -> flo -> fl -> f -> "" (covers empty string scenerio too)
      
  }
  return firstPrefix
};
  // time - O(n) space - 0(1)
  // indexof returns the first occurrence of a substring within a string, if at the beginning of string then it will give us an index of 0, if it occurance of a substring does not exist then -1 is returned. checks an index of a string within another string