// https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true
// return an integer that represents the number of anagram pairs of substrings of the string that are anagrams of each other
// an anagram just reproduces the same letters in a word but in a different order
// 1. substrings, not combinations 2. what is an anagram and how can you figure it out (same letters and length of string as another word for it to be an anagram)
// given: s = abba 
// 4 -> [a,a], [b,b], [ab,ba],[abb,bba]

// moad, daom
// true

// moad, oadm
// true

// abf, bfc
// false

// abcdefgh, defghabc
// true

// O(n log(n)) sorting
// O(n) w/ hashmap way -> a little  bit more efficient then sorting way
// given two strings, determine if they are anagrams
function areAnagrams(s1,s2){
  // first check if they're different length
   // not anagrams
  
  // otherwise, they're the same length and we sort both
  // sort both strings
   
  // sort s1
  // O(n log(n))

  // sort s2
  // O(n log(n))

  // O(n)
  // hashmap of letter to count of letters (another method)
  // O(n)
  // loop through s2 and see if its contained in it and > 0
    // decrement the count of s1 map

  // if we get to the end and we haven't  has a 'miss', then return true

  // compare the strings to see if they're equal
  // O(1)
}

function sherlockAndAnagrams(s) { // O(n)**2 where n 
  // slice up individual string to see if there
  // are any anagram pairs within it. we will use
  // our areAngrams helper function to check if
  // each substring pair is or is not an anagram
    let subs = []; // adding substring pairs
    for (let i = 0; i < s.length; i++) {  // O(n)**2 where n is the same length
        for (let j = i + 1; j < s.length + 1; j++) {
            subs.push(s.slice(i, j))
        }
    }

    let count = 0;
    for (let i = 0; i < subs.length; i++) { // O(n)**2 where n is the same length
        for (let j = i + 1; j < subs.length; j++) {
            if (areAnagrams(subs[i], subs[j])){
               count++;
               console.log(subs[i],subs[j])
              } 
        }
    }

    return count;
} // Big O = 2(n)**2 = O(n)**2

// helper method - hashmap strategy
function areAnagrams(s1,s2){ // O(n) where n is the same length
  // 1. length of two strings needs to be the same
   if(s1.length !== s2.length) return false
  // 2. same letters (given length is now the same)
   // map of letter to count of letters
   // O(n) - s1 and s2 are same length
   let map = new Map()
   for(let letter of s1){
     if(map.has(letter)){ // letter already in map
       map.set(letter, map.get(letter) + 1)
       } else { // if letter not in map
         map.set(letter, 1)
         }
     }
   // checking s2 letter against s1 map`
   // s2 needs to have same letters as s1
   // O(n) - s1 and s2 are same length
   for(let letter of s2){
     if(map.has(letter) && map.get(letter) > 0){ // decrement if in hashmap
       map.set(letter, map.get(letter) - 1)
       } else { // s2 letter not in s1 hashmap
         return false // not an anagram
         }
     }
     return true // if all the letters match - anagram!
    }
    // Big O - O(n) + O(n) = 2(n) = O(n)
      // not O(n+m) b/c both are the same length
  // let s1 = 'abba'
  // let s2 = 'abcd'
  
  // areAnagrams(s1,s2)

  // alternative: using JS object to keep track of letter occurrences

  // O(n)
// given two strings, determine if they are anagrams
// function areAnagrams(s1, s2) {
//   // first check if they're differnt length
//     // not anagrams
//   if (s1.length !== s2.length) return false;
  
//   // O(n)
//   // map of letter to count of letters
//   let map = {};
//   for (let letter of s1) {
//     if (map.hasOwnProperty(letter)) {
//       map[letter]++
//     } else {
//       map[letter] = 1;
//     }
//   }
  
//   for (let letter of s2) {
//     if (map[letter]) {
//       map[letter]--
//     } else {
//       return false;
//     }
//   }
//   // O(n)
//   // loop through s2 and see if it's contained in it and > 0
//     // decrement the count of s1 map
//   return true;
//   // if we get to the end and we haven't had a "miss", then return true
// }