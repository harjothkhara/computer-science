// https://leetcode.com/problems/remove-element/

// Given an array nums and a value val, remove all instances of that value in-place and return the new length.

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

// The order of elements can be changed. It doesn't matter what you leave beyond the new length

// Given nums = [3,2,2,3], val = 3,
// Your function should return length = 2

var removeElement = function(nums, val) {
    
  let i = 0
  while(i<nums.length){
      if(nums[i] === val){
          // remove val from array
          nums.splice(i,1)
          // continue checking for val at current position after removal of val
          i = i-1
      } else{ // keep looking
          i++
      }    
  }
  return nums.length
};