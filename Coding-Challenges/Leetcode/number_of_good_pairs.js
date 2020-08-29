// Number of Good Pairs
// https://leetcode.com/problems/number-of-good-pairs/
// Given an array of integers nums = [1,2,3,1,1,3]. A pair (i,j) is called good if nums[i] == nums[j] and i < j.
// return the number of good pairs
// e.g nums = [1,2,3,1,1,3] -> 4
 // there are 4 good pairs at (0,3), (0,4), (2,5),(3,4)

 var numIdenticalPairs = function(nums) {
  // loop through array and check if current value is equal to neighboring number
      // loop again starting at j (i+1){
      // if so, add it to the count, else keep looping until array - 1
      // return count
      
      let count = 0
      for(let i=0; i<nums.length-1; i++){
          for(let j=i+1; j<nums.length; j++){   
              if(nums[i] === nums[j]){
                  count +=1
              }
          }
      
       }
       return count 
  };