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
