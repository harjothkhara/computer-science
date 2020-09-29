// given a sorted array and a target value, return the index if the target is found. if not, return the index where it would be if it were inserted in order.

// e.g
Input: [1,3,5,6], 5
Output: 2

Input: [1,3,5,6], 2
Output: 1

Input: [1,3,5,6], 7
Output: 4

Input: [1,3,5,6], 0
Output: 0

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
  // loop through each num in array
      // if current num is equal to target then return index, or i
      // check if the target is less than current num and return i (correct order)
  // target not found, needs to be inserted at the end of array, return index as arr length
  
  for(let i=0; i<nums.length; i++){
      if(nums[i] === target || target < nums[i]){
          return i
      }     
   }
  return nums.length
};

// time - O(n)
// space - O(1)


