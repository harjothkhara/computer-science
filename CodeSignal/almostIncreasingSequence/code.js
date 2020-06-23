// almost increasing sequence - given a sequence as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array a0 < a1 < ....sequence containing only one element is also considered to be strictly increasing

// https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG/comments

function almostIncreasingSequence(arr) {
  let count = 0;
  for (let i = 0; i < arr.length - 1; i++) {
    // start comparing!
    // if current value is greater than next value
    if (arr[i] >= arr[i + 1]) {
      count += 1;
      // check neighbor behind
      let stepback = arr[i - 1] >= arr[i + 1];
      // check neighbor ahead 2 spots
      let stepforward = arr[i] >= arr[i + 2];
      if (stepback && stepforward) {
        return false;
      }
    } // checking count during each iteration
    if (count > 1) return false;
  }
  return true;
}

// almostIncreasingSequence([1, 3, 2, 1]) // -> false
// almostIncreasingSequence([1, 3, 2]) // -> true
// almostIncreasingSequence([1, 2, 1, 2]) // -> false
// almostIncreasingSequence([3, 6, 5, 8, 10, 20, 15]) // -> false
// almostIncreasingSequence([1, 1, 2, 3, 4, 4]) // false
almostIncreasingSequence([1, 4, 10, 4, 2]); // false
