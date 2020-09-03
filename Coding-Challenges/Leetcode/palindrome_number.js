// https://leetcode.com/problems/palindrome-number/
// determine whether an integer is a palindrome. an integer is a palindrome when it read the same backward as forward.
// e.g 121 -> 121 true
// -121 -> 121- false
// 10 -> 01 false

var isPalindrome = function(x) {
  //     121 -> 121 true
  //     123 -> 321  false
      
  //     -121 -> 121- false
  //      10 -> 01 false
      
      // if number is negative then retirn false
      // loop through numbers only if the number is positive
          // pop the end digit by modulo the number by 10
          // reduce the digit down a decimal place by dividing the digit by 10
          // add the pop number from step 1 to palindrome var
      // check if palindrone var === x, if so return true, else false
      
      let reversed_int = 0 // 321-
      // making a copy of the digit
      let y = x // -123
      while(x > 0){ // e.g 1
          let pop = x%10 // 1
          // reducing int - convert to binary, bitwise OR, and get rid of decimal
          x = x/10 | 0 // 0
          // adding int to reversed var
          reversed_int = (reversed_int * 10) + pop
      } 
      // checking if reversed int is a palindrone
      // console.log(reversed_int, y)
      return  reversed_int === y
  };

  // time - O(n) space - 0(n)

  // optimized solution
  var isPalindrome = function(x) {
    // edgecases: negative numbers are not palindromes -> false
    // if just reversing number into a reverse number and checking at the end for palindrome, then could run into an integer overflow problem.
    // avoided if we only reverse half of the number, since the reverse of the last half of the palindrome should be the same as the first half. e.g 1221 -> 12 == [12] palindrome!
    // 12321 -> odd -> 12 (3)ignore [12] palindrome! 3==3
    //     x = 12321
                                //     x = 12
                              // reverse = 123
        // 0 is a palindrome
        if(x === 0) return true
        // digit is negative or evenly divisble by 10
        if(x < 0 || x%10 === 0) return false
        
        let reversedInt = 0 // 123
        while(x > reversedInt){ // going to the middle digit
            let pop = x%10 // 3
            x = x/10 | 0  // 12
            reversedInt = (reversedInt*10) + pop
        }
        // odd number of digits, the middle num doesn't matter
        return x == reversedInt || x == parseInt(reversedInt/10)
    };
    // time - O(log(n) b/c we divide digit by 10 at each iteration 
    // space - 0(1) since we're not fully reversing our Int and running intpo an overflow problem`