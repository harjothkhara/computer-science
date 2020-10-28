
// https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

// initial solution - time complexity O(n**2), FAILED 1 TEST
// Complete the rotLeft function below.
function rotLeft(a, d) {
  // temp variable to store the left rotating num (beg of array)
  // iterate until we reach the number of left rotations
  for(let i=0; i<d; i++){
      // save current value to temp (always be first item in the array)
      let temp = a[0]
      // iterate down the array until we reach the last num in the array
      for(let j=0; j<a.length; j++){
          // once we're at the last item in array, we set temp equal to it. 
          if(j === a.length-1){
              a[j] = temp
          } else{
          // set the next value to the prev value
              a[j] = a[j+1]
          }
      }
  }
  // return new array (console.log)
  return a
}

// working solution -- passes all tests!
// Complete the rotLeft function below.
function rotLeft(a, d) {
  let rotatedArr = []
  let i = d // dividing ground
  let rotatedIndex = 0
// iterate through all nums to the right of the d point and add the nums consecutively to the new rotated array.
while(i < a.length){ // add to front half of new array
    // add to beginning of new array
    rotatedArr[rotatedIndex] = a[i]
    i++
    rotatedIndex++
}
// reset i back to 0 to iterate the left side of array
i = 0
// iterate through all the nums to the left of the d point and add the the rest of the remaining nums (after the other nums) to the new rotated array
while(i < d){ // add to back half of new array
    // add to beginning of new array
    rotatedArr[rotatedIndex] = a[i]
    i++
    rotatedIndex++
}
// return the newly rotated array
return rotatedArr
}

// time - O(2n) -> O(n)
// space - O(n)