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