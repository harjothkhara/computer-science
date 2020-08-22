// given an array of integers, find if the array contains any duplicates
// e.g [1,2,3,1] -> true
// e.g [1,2,3,4] -> false

// https://leetcode.com/problems/contains-duplicate/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  // space complexity O(n)
  // time complexity O(n)
  // use a set data structure to filter out duplicates
  // initialize a set
  const s = new Set()
  // add arr nums into set
  for(let num of nums){ // O(n)
      s.add(num)
  }
  // if the original length of the arr is different from the size of the set then we have duplicates, return true
  if(nums.length !== s.size){ // O(1)
      return true
  } else {         // else return false
      return false
  }
};

// others ways
var containsDuplicate = function(nums) {
  // 1.
  // space complexity - O(1) in-place comparisons, no extra space
  // time complexity - O(n^2)
  // for loop over the array
    // for loop over the array again
      // compare the first loop value to the second
      // if we find a duplicate, then return true
  // return false

  // 2.
  // space complexity - O(n)
  // time complexity - O(n)
   // use an object as a cache
   // store our key = num, value = boolean (we could also use a Set, or Map)
   // loop over our array
      //  if our value is already present in our object, then return true

      // if not, then add it to the object
   // return false

   // 3.
   // array.filter()
   // similar to the first solution, but checking

   // 4.
   // convert array to set
   // compare length of array to set
   // 2 is slightly better b/c we can exit out once we find duplicate

   // 5.
   // space O(1)
   // time O(n log(n))
   // sort the array
   // loop over the array, check if the value is the same as the previous value
};