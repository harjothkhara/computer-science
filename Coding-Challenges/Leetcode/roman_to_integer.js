// given a roman numeral, convert it to an integer
// https://leetcode.com/problems/roman-to-integer/

var romanToInt = function(s){
        // s = 'IIIV'
        // keep track of roman->integer count
        let count = 0
        // use a switch statement to match each numeral to the appropriate case
        // loop backwards starting from end first
       for(let i= s.length-1; i >= 0 ; i--){
           // for each symbol starting from left to right check the appropriate cases
           let num= s[i]
           switch(num){
               case 'I':
                   count+=1 * (count >=5 ? -1 : 1) 
                   break
                case 'V': 
                  count+=5 
                  break
                case 'X': 
                  count+=10 * (count >= 50 ? -1 : 1)
                  break
                case 'L': 
                    count+=50 
                    break
                case 'C': 
                    count+=100 * (count >=500 ? -1 : 1) 
                    break
                case 'D': 
                  count+=500 
                  break
                case 'M': 
                  count+=1000 
                  break
           }
       }
    
       return count
}

//     I = 1
//     V = 5
//     X = 10
//     L = 50
//     C = 100
//     D = 500
//     M = 1000
    
//     // RIGHT TO LEFT (subtraction used)
//     1.IV = 1 5 = 5-1 = 4
//     2.IX = 1 10 = 10-1 = 9
//     3.XL = 10 50 = 50-10 = 40
//     4.XC = 10 100 = 100-10 = 90
//     5.CD = 100 500 = 500-100 = 400
//     6.CM = 100 1000 = 1000-100 = 900
//     // LEFT TO RIGHT
//     III = 1 1 1 = 1+1+1 = 3
//     LVIII = 50 5 3 = 50+5+3 = 58  
//     M CM XC IV = 1000 100 1000  10 100   1 5 = 1000+900+90+4 = 1994
//                       |   |      |  |    | |
//                        900        90      4