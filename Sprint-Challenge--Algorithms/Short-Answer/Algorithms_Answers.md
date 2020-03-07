#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) linear runtime of 0(n). the while loop grows n times as long as "a" (0)1 is less than n^3 which grows in proportion to n.

    def algo1(n):
      a = 0
      count = 0

      while (a < n * n * n):
        a = a + n * n
        count += 1

      print(f"Count: {count}\n")

b) 0(nlogn). this is a nested loop which at first glance looks like 0(n^2), however the inner loop j grows at a faster rate(double) than n, which makes the while loop logn. everything within the while loop is 0(1). the outer for loop grows at n times, thus n(outerloop) \* logn(innerloop) = 0(nlogn). everything within the two loops is 0(1) and is relatively inconsequential.

    def algo2(n):
      total = 0
      count = 0

      for i in range(n):
        j = 1

        while j < n:
            j *= 2
            total += 1
            count += 1

      print(f"Count: {count}"

c) 0(n). this is a recursive function that's called once and grows proportional to n, or bunnies. the base case is 0(1) and doesn't matter in the calculation of big 0, it is however, important to the recursive call as this where it is trending towards and eventually returns once the basecase is met.

    def bunnyEars(bunnies, count):
        count += 1
        print(f"Count: {count}")
        if bunnies == 0:
            return 0

        return 2 + bunnyEars(bunnies-1, count)

## Exercise II

```
Since, the building has floors that are sequential ordered with numbers (no need for us to sort),we can simply run a binary search to find the optimal drop point for eggs. First we would see where the midpoint of n floors is and then proceed to drop an egg to see if it gets broken. If it breaks we can conclude that the optimal drop cannot be above us, so we eliminate that option and look further down. We then take the midpoint of where we currently stand with the ground to see which floor lies in the middle. We repeat the steps above by going to the new midpoint and see if the egg breaks or not, if not, we can eliminate everything below us. We repeat these steps until we find the optimal target drop point.

This step is more efficient than linear search because we don't need to go floor by floor, we divide and conquer! This algorithm has a log n time complexity, which is better than linear time 0(n) and worse than constant time 0(1).
```
