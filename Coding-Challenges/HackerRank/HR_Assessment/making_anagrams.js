// https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

// Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

// Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

// Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

// For example, if  and , we can delete  from string  and  from string  so that both remaining strings are  and  which are anagrams.

function makeAnagram(a, b) {
  // keeps track of deletions from str a and b
let count = 0 // letters matching from both str a and str b to make an anagram
let length = a.length
// 1 <= |a|, |b| <=10**4
const lengthOfA = a.length
const lengthOfB = b.length

// doesn't matter, we'll eventually ending up deleting letters that don't match up with each string
// if (lengthOfA !== lengthOfB){
//   // the length has to be equal to the shortest character length,
//   // we will iterate until that point
//   lengthOfA > lengthOfB ? length = lengthOfB : length = lengthOfA
//   }
 
  // seperating each string letter
  a = a.split('')
  b = b.split('')
  
for (let i =0; i<length; i++){
  console.log("i = " + "" + i)
  // if an anagram exists (letter in a is in b)
  if (b.includes(a[i])){
    console.log("letter in 'a, remove in 'b'--> " + a[i])
      // removing the letter in a
      let temp = a[i]
      a.splice(i,1)
      // found match in a
      count+=1
      // find and remove the same letter in b
      b.splice(b.indexOf(temp),1)
      // found match in b
      count+=1
      // go back to same round to check new letter in same position
      i = i-1
    }
  } // subtracting the matching anagram count against original letter count of both strings
  return (lengthOfA + lengthOfB) - count
}
makeAnagram('cde', 'abc') // 4
// makeAnagram('showman', 'woman') // 2
// makeAnagram('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke') // 30