// min swaps to sort an array in ascending order [0,1,2,3,4...]

// initial brute force attempt O(n**2) - only 1 test passed
function minimumSwaps(arr) {
  // swaps = iiiii (# of swaps to sort the array)

  // arr = [7,1,3,2,4,5,6]

  // loop from the beginning of the array to one before the end
  // check to see if the current num is in its correct position within the array (filter)
  // if not in correct position then we search the rest of the array for current spot
  // once we find the correct num for the current position we do a swap
  // increment our swap counter

  let i = 0;
  let swaps = 0;

  while (i < arr.length - 2) {
    // filter to check if current num is in the correct position, if not....
    if (arr[i] !== i + 1) {
      for (let j = i + 1; j < arr.length - 1; j++) {
        if (i + 1 === arr[j]) {
          // swap
          let temp = arr[i];
          arr[i] = arr[j];
          arr[j] = temp;
          // move i along and increment swap count
          i++;
          swaps++;
          break;
        }
      }
    }
  }
  return swaps;
}

// need to find a better solution because won't work with large numbers (1<=n<=10**5)
function minimumSwaps(arr) {
  // pre-processing
  const shift = Math.min(...arr) // lowest num in the array
  let swaps = 0
  let visited = [Array(arr.length).fill(false)] // [false, false, false, false...] 
                  // [] also works

  // iterate through the array
          // check if num in current index is in the correct spot, or, if num has already been visited. if                either then return and go to next num in the loop
          
          // x = i
          // loopLength = 0

          // else, iterate through current nums intended places until we reach a current index that has                been visited (cycle)
              // mark current index as visited
              // go to index where num should be (x= arr[x] - shift) index 1 -> index 2
              
          //count the cycle (length-1) to get the swap count. increment swap count

  // return the min swap count

  for(let i=0; i<arr.length; i++){ // O(n)
          // 1. in the correct spot or has already been visited move to next iteration round
          if(arr[i] === shift+i || visited[i]) continue
          
          // 2. not in correct spot, find a cycle!
          // in wrong spot, go searching for arr[i]'s intended spot until we find a cycle
          let x = i
          // keep track of loop count
          let loopLength = 0
          while(!visited[x]){ // find a cycle. - O(logn) at most half way through
              visited[x] = true //
              // lets go to the intended place of arr[x]
              x = arr[x] - shift
              loopLength++
          }
          // found a cycle, lets count it and add to swap count
          swaps += loopLength-1 
      }
  return swaps
}  // O(n) * O(logn)

// Youtube solution - https://www.youtube.com/watch?v=f7IIW0HVUcQ
const minimumSwaps = (arr) => {
  // pre-processing
  const shift = Math.min(...arr)
  let swaps = 0
  const visited = [...Array(arr.length)].map(() => false)
  // iterate through each value in the array
  arr.forEach((val, i) => {
    // if the current value is in the correct spot in the array 
    // or, if that spot in the array has already been visited, do nothing 
    if (val - shift === i || visited[i]) return
    // else, use a graph to find all the sub cycles
    let loopLength = 0
    let x = i
    while (!visited[x]) {
      visited[x] = true
      x = arr[x] - shift
      loopLength++
    }
    // add the length of the cycle to get # of swaps
    swaps += loopLength - 1
  })
  // once we've finished iterating return the swap count
  return swaps
}
// O(nlogn)
let arr = [0,2,3,4,1,6,5]
 minimumSwaps(arr)