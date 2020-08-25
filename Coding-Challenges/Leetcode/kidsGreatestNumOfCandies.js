// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
// given array candies [2, 3,  5,1,3] and integer extra candies 3 where
                        |  |   | | |
                      kid1 kid2 
// candies[i] represents the number of candies that the ith kid has
// for each kid check if there is a way to distribute extra candies among the kid
// such that he or she can have the greatest number of candies among them.
// Notice that multiple kids can have the greatest number of candies
i.e kid 1 -> 5 candies, kid 2 -> 5 candies, kid 3 -> 2 candies
// kid 1 and 2 have the greatest number of candies after adding the extra candies

var kidsWithCandies = function(candies, extraCandies) {
  // [2,3,5,1,3]       // 3
 //       |
 //.  | |.| x |
// find which kid has the greatest number of candies (gnoc) to begin with
const greatestNumOfCandiesKid = Math.max(...candies) 
// go through each kid and add the extra candies and then compare total to gnoc kid
let newCandiesCount = null
let result = []
for(let kid of candies){
  newCandiesCount = kid + extraCandies
// if current kid can get to gnoc kid total - mark as true, else false
if (newCandiesCount >= greatestNumOfCandiesKid){
  result.push(true)
} else {
  result.push(false)
}
}
return result  

};