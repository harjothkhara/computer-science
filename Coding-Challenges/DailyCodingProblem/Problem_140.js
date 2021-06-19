// Good morning! Here's your coding interview problem for today.

// This problem was asked by Facebook.

// Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

// For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

// Follow-up: Can you do this in linear time and constant space?

function ArrayDup(arr){
  let dupT = {}  // {2:2,4:1,6:2,8:1,10:2}
  // iterate over the array and keep track of counts of numbers by adding to dupT object
  for(let i=0; i<arr.length; i++){ // O(n)
    if(dupT[arr[i]] > 0){
      dupT[arr[i]] = dupT[arr[i]] + 1
      } else {
          dupT[arr[i]] = 1
        }
    }
    // iterate over dupT object and add single number occurrences to singleCount array
  let singleCount = []
  for(let key in dupT){ // O(n)
    if(dupT[key] === 1){
        singleCount.push(key)
      }
    }
  return singleCount
  }

const arr = [2, 4, 6, 8, 10, 2, 6, 10]

ArrayDup(arr)  // O(n) + O(n) = O(n)
// [4,8]

// proportional amount of space as the number of elements in the array, which means that it's O(n) space as well as O(n) time
