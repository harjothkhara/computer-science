// reverseInParentheses - write a function that reverses characters in (possibly nested) parentheses in the input string.
// CodeSignal problem
// Input strings will always be well-formed with matching ()

function reverseInParentheses(str){
  let openP = null
  let closeP = null
  let stringP = null
  let newStr = null
  let combinedStr = null
  for (let i=0; i<str.length; i++ ){
    // grabing the first occurence of parenthesis
    if (str.includes('(')){
      openP = str.indexOf('(')
      closeP = str.indexOf(')')
   // getting the parenthesis string
      stringP = str.slice(openP,closeP+1)
   // putting parenthesis string into array and
   // removing first and last index (parenthesis)
   // reversing the letters inside the array 
      newStr = stringP.split('').slice(1,-1).reverse().join('')
   // combining reversed in parentheseses string with the rest 
      combinedStr = str.slice(0,openP) + newStr + str.slice(closeP+1)
   // setting str to combinedStr so that we can continue looking for
   // more parentheses at the top of loop
      str = combinedStr
     }
   }
   return str
 }
 
 reverseInParentheses('foo(bar)baz(blim)') // foorabbazmilb
 // reverseInParentheses('foo(bar)baz') // foorabbaz
 // reverseInParentheses('(bar)') // rab
 
 // (bar) -> rab
 // foo(bar)baz -> foorabbaz
 // foo(bar)baz(blim) -> foorabbazmilb