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

// time O(n)
// space 0(1)

// another way:
var strStr = function(haystack, needle) {
  // loop though haystack string checking any substring matches with needle. we don't need to loop all the way to end of haystack but only the difference of haystack - needle i.e if we're at the last index of string but needle is length 2 then it would make sense to stop 2 away from the end instead of checking the last index.
    // create subsring of haystack and see if we find a match, if so, then we return the index
 
// no match found return -1
    for(let i=0; i<haystack.length - needle.length+1; i++){  // <= also works!
        // console.log(i)
        let haystackSlice = haystack.slice(i,i+needle.length)
        // console.log(haystackSlice)
        if(haystackSlice === needle){
            return i
        }
    }
    // no match found
    return -1
};

// haystack = "hello", needle = "ll"

// haystack = "he", needle = "ll"
// haystack = "el", needle = "ll"
// haystack = "ll", needle = "ll"
// haystack = "lo", needle = "ll"

// if needle is an empty string haystack will slice(0,0) to "" during initial loop and return index 0. "".length = 0 and slice end is not inclusive so the h gets chopped off.

// time - O(h-n) where h is the length of haystack and n is the length of needle
// space - O(1)