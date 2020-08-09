// given words in a magazine and words in a note, print 'Yes' if you can replicate the ransom note exactly using the whole words from the magazine, othewise 'No'
// https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true
// e.g magazine -> give me one grand today night
// note ->  give one grand today     'Yes'
// e.g magazine -> two times three is not four
// note ->  two times two is four     'No'
// 'two' only occurs once in the magazine

// const magazine = ["give","me","one","grand","today", "night"]
// const note = ["give","one","grand","today"]

// o(|magazine| + |note|) length of magazine + length of note
// o(n + m)
function checkMagazine(magazine, note) {
  // create a hash table for magazine, where key => value is word => # of occurrences. key: word, value: # of occurrences
  const mag = new Map();
  for (let word of magazine) {
    // if char is already in hash table, then increment the value of occurrences by 1
    if (mag.has(word)) {
      // incrementing value in hash map by 1 if key already exists
      mag.set(word, mag.get(word) + 1);
    } else {
      // if char is not in the hashmap add it
      mag.set(word, 1);
    }
  }
  console.log(mag);
  // look up in our hash table, words from note, if we find the key and the value > 0
  for (let word of note) {
    // if word in note exists in hash table and value still has occurrences available
    if (mag.has(word) && mag.get(word) > 0) {
      // decrease the value by 1
      mag.set(word, mag.get(word) - 1);
    } else {
      // word note is not in magazine and has not occurrences available
      // return no
      console.log('No');
      return;
    }
  }
  // return yes
  console.log('Yes');
  return;
}
// big O -> o(length of magazine) + o(length of note), or o(m+n)

// const magazine = ["give","me","one","grand","today", "night"]
// const note = ["give","one","grand","today"]
const magazine = ['two', 'times', 'three', 'is', 'not', 'four'];
const note = ['two', 'times', 'two', 'is', 'four'];

checkMagazine(magazine, note);

// initial solution :(
function checkMagazine(magazine, note) {
  let mag = new Map();
  for (let i = 0; i < magazine.length; i++) {
    // find word in mag and save as key
    // to hashmap, and value = # of times its available
    // if there a duplicate word in magazine, counter the value
    if (mag.has(magazine[i])) {
      let val = mag.get(magazine[i]);
      mag.set(magazine[i], val + 1);
    } else {
      mag.set(magazine[i], 1);
    }
  }
  // adding note to hashmap
  let not = new Map();
  for (let i = 0; i < note.length; i++) {
    // find word in mag and save as key
    // to hashmap, and value = # of times its available
    // if there a duplicate word in magazine, counter the value
    if (not.has(note[i])) {
      let val = not.get(note[i]);
      not.set(note[i], val + 1);
    } else {
      not.set(note[i], 1);
    }
  }
  // compare magazine and notes hashmaps
  let message = null;
  for (let i = 0; i < note.length; i++) {
    if (mag.has(note[i]) && mag.get(note[i]) - not.get(note[i]) > -1) {
      message = 'Yes';
    } else {
      // if the frequency of characters is more in the note than
      // is available in the magazine, we break and print 'No'. Finish
      message = 'No';
      break;
    }
  }
  console.log(message);
}

// big o -> o(m * n) length of m * length of n, looping through 2 different things
// o(|magazine| * |note|) quadratic
function checkMagazine2(magazine, note) {
  for (let magWord of magazine) {
    for (let noteWord of note) {
      console.log(noteWord + magWord);
    }
  }
}
