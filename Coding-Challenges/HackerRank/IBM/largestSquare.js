// https://www.interviewbit.com/problems/maximum-size-square-sub-matrix/

function largestSquare(matrix) {
  // dynamic programming- creating cache so we don't check each index more than once
  let cache = [...A];
  // keep track of largest Square
  let result = 0;
  // iterating through matrix
  for (let i = 0; i < A.length; i++) {
    for (let j = 0; j < A[i].length; j++) {
      // no need to check non-defects aka 0's, not top and left sides since our iterative strategy checks the bottom left of a square first and then surrounding neighbors. top and left neighbors will be out of bounds and so index value will be the same(no change)
      if (i && j > 0 && cache[i][j] > 0) {
        // see if neighbor were able to make squares
        let neighbors = Math.min(
          cache[i][j - 1],
          cache[i - 1][j],
          cache[i - 1][j - 1]
        );
        // updating cache at index with new max square result (if any)
        cache[i][j] = 1 + neighbors;
      }
      // keeping track of max square
      if (cache[i][j] > result) result = cache[i][j];
    }
  }
  // returning largest square length inside matrix
  return result;
}

// resources: https://www.youtube.com/watch?v=FO7VXDfS8Gk
