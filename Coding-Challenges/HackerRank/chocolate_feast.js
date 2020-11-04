// https://www.hackerrank.com/challenges/chocolate-feast/problem

function chocolateFeast(n, c, m) {
  // calculate how many chocolates can be bought with the initial budget
  let chocolates = Math.floor(n/c)
  // wrappers = how many chocolates we have ^^
  let wrappers = chocolates
  // loop comparing wrappers to m trade-in-value. if wrappers > m:
  while(wrappers >= m){
      // update # of cholocates by how many wrappers we can trade in for new chocolates
      chocolates += Math.floor(wrappers/m)
      // update wrappers by how many we traded in vs how many we kept
      // wrappers after eating new bars + wrappers we didn't trade-in
       wrappers = Math.floor(wrappers/m) + wrappers%m
  }
  // return max # of chocolates eaten
  return chocolates
}

// time O(m)
// space O(1)