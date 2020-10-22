// https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup&isFullScreen=true
          cumulus(regular-cloud)
           |
const c = [0,1,0,0,0,1,0]
                     |
                    thunder-cloud 
// you can jump 1 cloud over or 2 clouds. you must avoid the thunderclouds

// initial solution
function jumpingOnClouds(c) {
  // variable to keep track of # of moves
  let moves = 0;
  // iterate through the array
  for (let i = 0; i < c.length - 1; i++) {
    console.log(i, moves);
    // check if 2 jumps is possible === 0
    // if so, move ahead 2 jumps and increment jumps by 1
    if (c[i + 2] === 0) {
      i = i + 1;
      moves++;
    } else {
      // else move 1 jump ahead and increment jump by 1
      moves++;
    }
  }
  return moves;
}

// coaching - python solution

def jumpingOnClouds(c):
    // # store the number of jumps that we take
    num_jumps = 0
// # keep track of the current cloud we're on (index)
    curr = 0
// # while loop over c (once we're at the last cloud we're done)
    while curr < (len(c)-1): 
  // # either increment by 1 or 2
  // # we always want to jump 2 if we can, because we want the shortest path
  // # check if we can jump 2:
  // # check if current + 2 is still in our array or if the current + 2 item is 1(thundercloud)
        // # if its outside of the array(out of bounds) or a thundercloud, then jump 1
        if curr+2 >= len(c) or c[curr+2] == 1:
            curr+=1
        // # if it's not a thundercloud, jump 2
        else:
            curr+=2 
    // # increment our jump count
        num_jumps+=1 

    // # return num_jumps
    return num_jumps

// time - O(n) where n equals the length of c. worst case we visit every single num in the array
// space - 0(1) --> only affected when we create new data structures