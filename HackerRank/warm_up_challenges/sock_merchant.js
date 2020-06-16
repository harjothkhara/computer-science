// https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup&isFullScreen=true

// John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

// For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

function sockMerchant(n, ar){
let indexToDelete = []
let count = 0
console.log("starting array: "+ ar)
for (let i=0; i<ar.length; i++){
  for (let j=i+1; j<ar.length; j++){
    if (ar[i] == ar[j]){
      console.log("which ith round:" + i)
      console.log("which jth round:" + j)
      console.log("comparing " + ar[i],ar[j])
      count+=1
      // storing index of item pairs i want to remove
      indexToDelete.push(i,j)
      console.log("index to delete: " + indexToDelete)
      // filtering out arr by index based on whats in our indexToDelete array
      let arr = ar.filter((x,index) => index !== indexToDelete[0] && index !== indexToDelete[1])
      // setting original array to filter array
      ar = arr
      // clearing out our indexes to delete for next round
      indexToDelete = []
      // setting i and j back to begging
      i = 0
      j = i // j will increment by 1 when we go back up to the beginning of loop
      console.log("filtered array: " + ar)
    }
 }
 }
 return count
}
  

sockMerchant(9, [10,20,20,10,10,30,50,10,20])
// var arrayName = Array(20).fill(42)
// sockMerchant(100, arrayName)