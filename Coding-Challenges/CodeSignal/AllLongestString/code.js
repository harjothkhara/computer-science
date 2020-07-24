function allLongestStrings(inputArray) {
  let longest = 0;
  let newArr = [];
  // iterate through array and save the longest char length to sum variable
  inputArray.forEach((word) =>
    word.length >= longest ? (longest = word.length) : null
  );
  // go through each string and add the logest string/s in the array
  for (let word of inputArray) {
    word.length === longest ? newArr.push(word) : null;
  }
  return newArr;
}

let inputArray = ['aba', 'aa', 'ad', 'vcd', 'aba'];

allLongestStrings(inputArray);
