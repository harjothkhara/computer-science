// Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/
// given strings Jewels(J) and Stones(S). You want to know how many of the stones you have are also jewels.
  // Input: J = "aA", S = "aAAbbbb" output: 3
// initial solution - space O(1), time O(n**2)
var numJewelsInStones = function(J, S) {
  // loop through each letter in jewels strings  and see if any of the
    // letters match up with any letter in the stones string (2 loops)
    // if there is a match, i.e any of the letters in the stones is a jewel then increment the count variable
    
    let count = 0
    for(let jewel of J){
        for (let stone of S){
            if(jewel === stone){
                count += 1
            }
        }
    }
    return count
};

// optimization: since the characters in J are distinct, add them to a hashset where access is 0(1)
var numJewelsInStones = function(J, S) {
  let count = 0
  const jewel = new Set(J) // O(1) access
  for(let stone of S){ // O(n)
    if(jewel.has(stone)){
      count += 1
    }
  }
  return count
};
// space - O(n) creating a new data structure 
// time - O(n) one for loop, and access to letters in set is 0(1)

var numJewelsInStones = function(J, S) {
  let count = 0
  for(let i=0; i<S.length; i++){ // loop through our stones
    // does index inside J exist with the given S letter at each iteration
    if(J.indexOf(S.charAt(i)) > -1){ 
      count += 1
    }
  }
  return count
};