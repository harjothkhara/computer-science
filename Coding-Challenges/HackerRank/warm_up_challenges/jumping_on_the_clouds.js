// https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup&isFullScreen=true

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
