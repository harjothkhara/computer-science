// https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D=arrays

// video explanation of algorithm: https://www.youtube.com/watch?v=YWYF6bOhPW8

function minimumBribes(q) {
  // bribe counter
  let bribes = 0
  // iterate queue and compare person number to queue position
  for(let i=q.length-1; i>=0; i--){
    // filter cases when you do not bribe at ith position - already in correct pos
      if(q[i] !== i+1) { // [2,5,1,3,4] if 4 !== 5
      // bribe and move ahead
          // being at initial ith position, valid current position after bribe can be (i-1)th position 
          if(i-1 >= 0 && q[i-1] == i+1){
            bribes++
            // swap(arr,i,i-1)
            let temp = q[i]
            q[i] = q[i-1]
            q[i-1] = temp
            } 
           // being at initial ith position, valid current position after bribes can be (i-2)th position  
           else if(i-2 >= 0 && q[i-2] == i+1){  
              bribes+=2
              // swap(arr,i-2,i-1)
              // swap(arr,i-1,i)
              let temp = q[i-2]
              q[i-2] = q[i-1]
              q[i-1] = temp
              temp = q[i-1]
              q[i-1] = q[i]
              q[i] = temp
            } 
            // too chaotic (trying to bribe more than 2 people which is ahead of you)  
            else {
              bribes = "Too chaotic"
              break
           }
      }
  }
  console.log(bribes)
}

// same solution as above but with notes and Big 0 (second day practice!)
function minimumBribes(q) {
  // [2,1,5,4,3]    
// 1. no bribes at i (filter to see if there was any bribes)
// 2. bribes (going down the queue and sorting it in its rightful order)
  // person at i bribed the person in front (i-1)
          // swapping (arr, i, i-1)
          // bribes++
  // person at i bribes 2 people in front (i-2)
          // swapping (arr, i, i-1)
         // swapping (arr, i-1, i-2) 
         // bribes+=2
  // person at i did more bribes (too chaotic) 
      // print("too chaotic")
  let bribes = 0
  // temp = 8
             // |    
  // [1 2 5 3 7 6 4 8]
  for(let i=q.length-1; i>=0; i--){
      if(q[i] !== i+1){ // filter to see if a bribe took place
          // check i-1 position
          if(q[i-1] === i+1){ // send q[i] back to its origin spot (sort)
              // swapping (arr, i, i-1)
              let temp = q[i-1]
              q[i-1] = q[i]
              q[i] = temp
              // increment swap count
              bribes++
            // check i-2 position  
          } else if(q[i-2] === i+1){ // send q[i] back to its origin spot (sort)
              // swapping (arr, i-1, i-2)
              let temp = q[i-2]
              q[i-2] = q[i-1]
              q[i-1] = temp
          // swapping (arr, i, i-1)
              temp = q[i-1]
              q[i-1] = q[i]
              q[i] = temp
              // increment swap count 
              bribes+=2
          } else {
              bribes = "Too chaotic"
              break
          }
      }
  }
  console.log(bribes)
}

// time - O(n)
// space 0(1)