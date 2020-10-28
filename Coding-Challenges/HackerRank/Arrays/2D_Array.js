// https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=arrays


// Complete the hourglassSum function below.
function hourglassSum(arr) { // brute forece solution
  const rows = arr.length
  const columns = arr[0].length
 
  let maxHourglassSum = -63 // hourglass only has 7 elements in it, and each value can be at lowest -9 (per constraints), so we can set our initial max to begin with to be -9*7 = -63 (can't use Number.MIN_VALUE)

  // loop through the 2d array(nested - column, row)
  for(let i=0; i<rows-2; i++){
      for(let j=0; j<columns-2; j++){
      // find each hourclass - move in direction to make an hourclass,            adding up each indice value within the hour glass
           let currentHourglassSum = arr[i][j] + arr[i][j+1] + 
              arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + 
              arr[i+2][j+1] + arr[i+2][j+2]
      // for each hourglass, check max value against current hourglass total we just calculated vs stored value.
          maxHourglassSum = Math.max(maxHourglassSum, currentHourglassSum)
      }
  }   
  // return hourglass max sum
  return maxHourglassSum
}
// time - O(n**2) where n is the length of a rows and the length of columns
// space - 0(1) no data stucture 