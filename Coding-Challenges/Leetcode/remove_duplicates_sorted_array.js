// given a sorted array nums, remove the duplicates in-place that each element appears only once and returns the new length.

// do not allocate extra space for another array, you must do this by modifying the input array in-place with 0(1) extra memory.

// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

// initial solution
var removeDuplicates = function(nums) {
  // compare array values to the previus value behind it, if they're equal then we have a duplicate so remove current number from the array
      
      for(let i=0; i<nums.length; i++){
          if(nums[i] === nums[i-1]){
              // delete duplicate
              nums.splice(i,1)
              // set i back 1 so we check current iteration under new order for more duplicates
              i = i - 1
          }
      }
      return nums.length
  };

  // 2 pointer strategy where i is the slow-runner and j the fast runner.
  // as long as nums[i] = nums[j], we increment j to skip the duplicate
                 [1,         1,             2,3]
  // when nums[j] != nums[i], the duplicate run is over so we must copy its value to nums[i+1]. i is then incremented and we repeat the same process again until j reaches the end of the array

  var removeDuplicates = function(nums) {
    // 2 pointer: slow and faster runner, skip duplicates.
       let i = 0 // slow
       let j = 1 // fast
       
       while(j < nums.length){
           if(nums[j] !== nums[i]){
               i++
               nums[i] = nums[j]
               j++
           } else{
               j++  
           }
        }
       return i+1
    }
    // i=0 j=1
    //          |           |        
    // [0,1,2,3,4,2,2,3,3,4]
    // return i + 1 -> total number of elements in array (remember array is 0 based that's why we add 1)