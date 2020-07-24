function matrixElementsSum(matrix) {
  let set = new Set();
  let rooms = 0;
  for (let arr of matrix) {
    console.log(arr);
    // adding indices with 0 inside to set
    arr.forEach((num, index) =>
      num === 0 &&
      // index isn't in our set then add it
      !set.has(index)
        ? set.add(index)
        : // if index already in set - beware ghosts nearby
        set.has(index)
        ? (num = 0)
        : // else, add it to available rooms (no ghosts nearby)
          (rooms += num)
    );
  }
  return rooms;
}

let matrix = [
  [0, 1, 1, 2],
  [0, 5, 0, 0],
  [2, 0, 3, 3],
];

matrixElementsSum(matrix);
