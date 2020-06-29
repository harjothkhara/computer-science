// https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps


// Space Complexity = 0(n)
// Time Complexity = 0(n)
function countTriplets(arr, r) {
  // counter to track number of triplets
    let totalCount = 0
    const possibilities = {}
    const combos = {}
  // find common ratio and add it to triplets arr

    arr.forEach((number) => {
        totalCount += (combos[number] || 0);
        const nextNumber = number * r; // 1

        combos[nextNumber] = (
          // if its already in there
           (combos[nextNumber] || 0)
        +  (possibilities[number] || 0)
        );

        possibilities[nextNumber] =
            // if its already in there add 1 to it
           (possibilities[nextNumber] || 0) + 1;
      });

      return totalCount

// http://pythontutor.com/javascript.html#code=function%20countTriplets%28arr,%20r%29%20%7B%0A%20%20%0A%20%20let%20totalCount%20%3D%200%0A%20%20const%20possibilities%20%3D%20%7B%7D%0A%20%20const%20combos%20%3D%20%7B%7D%0A%0A%20%20arr.forEach%28%28number%29%20%3D%3E%20%7B%0A%20%20%20%20%20%20totalCount%20%2B%3D%20%28combos%5Bnumber%5D%20%7C%7C%200%29%3B%0A%20%20%20%20%20%20const%20nextNumber%20%3D%20number%20*%20r%3B%20//%201%0A%20%20%20%20%0A%20%20%20%20%20%20combos%5BnextNumber%5D%20%3D%20%28%0A%20%20%20%20%20%20%20%20//%20if%20its%20already%20in%20there%0A%20%20%20%20%20%20%20%20%20%28combos%5BnextNumber%5D%20%7C%7C%200%29%0A%20%20%20%20%20%20%2B%20%20%28possibilities%5Bnumber%5D%20%7C%7C%200%29%20%20%0A%20%20%20%20%20%20%29%3B%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20possibilities%5BnextNumber%5D%20%3D%0A%20%20%20%20%20%20%20%20%20%20//%20if%20its%20already%20in%20there%20add%201%20to%20it%0A%20%20%20%20%20%20%20%20%20%28possibilities%5BnextNumber%5D%20%7C%7C%200%29%20%2B%201%3B%0A%20%20%20%20%7D%29%3B%0A%20%20%20%20%0A%20%20%20%20return%20totalCount%0A%20%20%20%20%0A%7D%0A%0AcountTriplets%28%5B1,5,5,25,125%5D,%205%29&curInstr=20&mode=display&origin=opt-frontend.js&py=js&rawInputLstJSON=%5B%5D
