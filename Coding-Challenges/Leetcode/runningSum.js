// given an array nums = [1,2,3,4]. runningSum = [1,3,6,10]
// we define a running sum of an array as runningSum[i] = sum(nums[0]...nums[i])
// return the running sum of nums

var runningSum = function(nums) {
  // start of with the first num in the array and add it to new array
      // add the next number in the array to the previous num in new array, take the total and add it to the              next sequence in new array. continue until we reach the end of our nums array
  
  let newArr = []
  for(let i=0; i<nums.length; i++){
      if(i===0){
          newArr.push(nums[i])
      }
      else{ 
          newArr.push(nums[i] + newArr[i-1])
          // console.log(newArr)
      }
  }
  
  return newArr
};

// technical coaching solution:
var runningSum = function(nums) {
  // create a var that keeps track of the sum at each iteration
  let sum = nums[0]
  // create an array for our running sum
  let sumsArr = [nums[0]] // first num added to sumsArr
  // iterate over nums
    // add each new number to our sum
    // add the new sum into the array
  for(let i=1; i<nums.length; i++){
    sum += nums[i]
    sumsArr.push(sum)
  }
  
  // return running sums array
  return sumsArr
};

