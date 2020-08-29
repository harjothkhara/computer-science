// shuffle the array
// https://leetcode.com/problems/shuffle-the-array/
// 2n -> even numbers
var shuffle = function (nums, n) {
  // match corresponding x and y neighbors together inside of new array
  const newArr = [];
  for (let i = 0; i < n; i++) {
    newArr.push(nums[i]);
    newArr.push(nums[i + n]);
  }
  return newArr;
};

const arr = [2, 5, 1, 3, 4, 7];
shuffle(arr, 3);
