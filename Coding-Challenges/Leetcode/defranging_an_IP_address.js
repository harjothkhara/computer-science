// given a valid IP address, return a altered version of that IP address where every period "." is replaced with "[.]"
// https://leetcode.com/problems/defanging-an-ip-address/

// initial solution:
var defangIPaddr = function (address) {
  // go through IP address (string) and replace "." with "[.]"
  // use regex method 'replace' to identify all '.' and return new string replacing with '[.]'

  return address.replace(/[.]/g, '[.]');
};

// another solution
var defangIPaddr = function (address) {
  // go through IP address (string) and replace "." with "[.]"

  // loop through string and add letters to new variable and add condition with the loop that wherever string == '.' we add '[.]' instead

  let newString = '';
  for (let char of address) {
    if (char === '.') {
      newString = newString + '[.]';
    } else {
      newString = newString + char;
    }
  }
  return newString;
};

// time - O(n)
// space - O(n)
