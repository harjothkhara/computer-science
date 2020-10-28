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