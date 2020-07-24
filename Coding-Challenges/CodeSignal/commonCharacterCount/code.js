function commonCharacterCount(s1, s2) {
  s1 = s1.split('');
  s2 = s2.split('');

  // track frequency of characters
  const objs1 = {};
  const objs2 = {};

  // adding s1 letters and letter count to s1 object
  for (let i = 0; i < s1.length; i++) {
    // if obj1 does not have the letter from s1, add it!
    !objs1.hasOwnProperty(s1[i])
      ? (objs1[s1[i]] = 1)
      : // if obj1 has the same letter from s1 appear again, increment existing lettter count
        (objs1[s1[i]] += 1);
  }
  console.log(objs1);
  // adding s2 letters and letter count to s2 object
  for (let i = 0; i < s2.length; i++) {
    // if obj2 does not have the letter from s2, add it!
    !objs2.hasOwnProperty(s2[i])
      ? (objs2[s2[i]] = 1)
      : // if obj2 has the same letter from s2 appear again, increment existing lettter count
        (objs2[s2[i]] += 1);
  }
  console.log(objs2);
  console.log(objs2.hasOwnProperty('b'));

  // track common characters
  let total = 0;

  for (let prop in objs1) {
    // and check lowest number of letters between both (object value) common letter and add to total
    // check if letter property in objs1(prop) exists in objs2
    if (objs2.hasOwnProperty([prop]) === true) {
      // check which letter frequency is the shortest and add it to our total count
      if (objs2[prop] < objs1[prop]) {
        total += objs2[prop];
      } else {
        total += objs1[prop];
      }
    }
  }
  return total;
}
