// https://www.hackerrank.com/challenges/two-strings/problem
// Given two strings, determine if they share a common substring. A substring may be as small as one character.
// For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.

// using a hashset strategy (dict that stores the key -> value)
// Set {'a', 'b' ....}

// o(n) where n === |s1| + |s2| (length of s1 + length of s2)
// o(|s1| + |s2|) -> o(n + m)
function twoStrings(s1, s2) {
  // O(s1 + s2) run time
  // create a hashtable(dictionary) of characters of the first string
  // how do we do this?
  // loop through the string and store the characters in it
  // key -> value
  const s1Set = new Set(s1); // hashSet - stores key only, no dupes
  for (let char of s2) {
    // check if each char in string2 exists in our hashSet(dictionary)
    // if so, we have a common substring between string1 and string2, return
    if (s1Set.has(char)) {
      return 'YES';
    }
  }
  // if after iterating each char in string2 without finding a common char, we return 'no' substring found
  return 'NO';
}

const s1 = 'wouldyoulikefries';
const s2 = 'abcabcabcabcabcabc';
twoStrings(s1, s2);
