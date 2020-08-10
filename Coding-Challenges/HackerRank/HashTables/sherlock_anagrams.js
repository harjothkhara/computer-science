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
// helper method - hashmap strategy
function areAnagrams(s1,s2){
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
     if(map.has(letter)){ // decrement if in hashmap
       map.set(letter, map.get(letter) - 1)
       } else { // s2 letter not in s1 hashmap
         return false // not an anagram
         }
     }
     return true // if all the letters match - anagram!
    }
    // Big O - O(n) + O(n) = 2(n) = O(n)
  let s1 = 'abba'
  let s2 = 'abcd'
  
  areAnagrams(s1,s2)