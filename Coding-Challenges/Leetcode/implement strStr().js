// https://leetcode.com/problems/implement-strstr/
// return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
// examples:
  // Input: haystack = "hello", needle = "ll"
  // Output: 2

  // Input: haystack = "aaaaa", needle = "bba"
  // Output: -1

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
  // use indexOf method on input string to find first occurance of needle, if needle is not in input string, bu default the indexOf method return -1.
  // add edgecase for when needle is an empty string "" we return 0
  
  if(needle === "") return 0
  
  return haystack.indexOf(needle) 
};