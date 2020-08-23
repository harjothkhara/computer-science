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
  for(let i=0; i<nums.length-1; i++){
    for(let j=i+1; j<nums.length; j++){
      if(nums[i] === nums[j]){
        return true
      }
    }
  }
  return false
}
  // 2.
  // space complexity - O(n) adding a data structure
  // time complexity - O(n) worst case at the end of array
   // use an object as a cache
   // store our key = num, value = boolean (we could also use a Set, or Map)
   // loop over our array
      //  if our value is already present in our object, then return true

      // if not, then add it to the object
   // return false
   var containsDuplicate = function(nums){
     let cache = {} 
     for(let n of nums){
       // if n is already in our cache - duplicate found
       if(cache[n]){
         return true // if we find the duplicate before reaching end of array we return out early
       }
       // if n is not in our cache, then we add it
       cache[n] = 'present'
       console.log(cache)
     }
     // no duplicates found
     return false
   }

   // 3.
   // array.filter()
   // similar to the first solution, but checking

   // 4. (see my initial solution above)
   // convert array to set
   // compare length of array to set
   // 2 is slightly better b/c we can exit out once we find duplicate

   // 5.
   // space O(1)
   // time O(n log(n))
   // sort the array
   // loop over the array, check if the value is the same as the previous value
   var containsDuplicate = function(nums){
    // sort the array
    const sortNums = nums.sort()
    for(let i=0; i<sortNums.length-1; i++){
      for(let j=i+1; j<sortNums.length;j++){
        if(sortNums[i] === sortNums[j]){
          return true
          }
        }
     }
     return false
  }