// given an array of ints and a target int, return the indices of the two numbers that add up to the target
// e.g [2,7,11,15] target = 9
        | |
        0 1    2+7 = 9
// output: [0,1]

// https://leetcode.com/problems/two-sum/

// initial solution:
var twoSum = function(nums, target) {
  // [2,7,11,15] target = 9
  
  // check each number in the array with each other to see if they sum to target
  // have 2 pointers, a slow pointer and a fast pointer that checks every other num for a sum     
  // match to the target. if two nums sum to the target then return
   
for (let i=0; i<nums.length-1; i++){
    let pointerA = i
    let pointerB = i+1
    
    while(pointerB < nums.length){
       if(nums[pointerA] + nums[pointerB] === target){
           return [pointerA, pointerB]
       } else {
           pointerB++
       }
    }
  }
};

// time - O(n**2)
// space - O(1) ?

// optimized solution:
var twoSum = function(nums, target) {
  // [2,7,11,15] target = 9
  // add each num and its index to a hashmap (first iteration)
  // check if each elements difference against the target exists in the hashmap (second iteration)
      // 9-2=7
      // 9-7=2
      // 9-11=-1
      // 9-15=-6
  // intialiazing hashmap
  let map = new Map() // { 2 => 0, 7 => 1, 11 => 2, 15 => 3 } 
  
  // adding array elements (key: num, val: indices) to hashmap
  for(let i=0; i<nums.length; i++){
      map.set(nums[i], i) // key (num) -> index
  }
  
  // checking if each elements complement (difference) exists in our hashmap
  for(let i=0; i<nums.length; i++){
      let complement = target - nums[i] 
      // check if num pairs exists in hashmap and if indices are distinct (i.e not the same)
      if(map.has(complement) && map.get(complement) !== i ){  // e.g target = 6 nums[i] = 3
                                   // key -> index  index 1 !== index 1  
          return [i, map.get(complement) ] // index pair for two number sum in an array
              // [0, 1]    // key -> index
      }
  }

};
// time - O(2n) -> O(n)   always a tradeoff for time vs space
// space - O(n)

// one pass hashmap solution
var twoSum = function(nums, target) {
  let map = new Map() 
   // one pass hashmap
 for(let i=0; i<nums.length; i++){
     let complement = target - nums[i]
                    
     if(map.has(complement)){ 
        return [map.get(complement),i ] 
     }
   map.set(nums[i],i)
 }
};
// time - O(2n) -> O(n)   always a tradeoff for time vs space
// space - O(n)

