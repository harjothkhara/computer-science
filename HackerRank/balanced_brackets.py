# write a function that takes a string as input. 
# the string can contain 4 types of brackets: "[]", "()", "{}", and "||"
# function should return a boolean indicating whether the string is balance
# a string is considered balances if it has as many opening brackets of a given type as it has closing
# "[(])" should return false
# "foo(bar)baz" should return true
# "{{||[]||}}" should return true

# classic stack problem
# all we care about is the most recently left open bracket
# stack - LIFO
# push open brackets to the stack and pop closing brackets from the stack
# Pipes "|" "|" brackets use the same character to indicate both opening and closing

# Complete the isBalanced function below.
def balancedBrackets(s):
    # storing opening parenthesis
    open_paren = ["{","(","["]
    # storing closing parenthesis
    close_paren = ["}",")","]"]
    # storing open/close pipes "|" here since both have same open/close
    pipe = []
    # data structure that uses LIFO to keep track of opening brackets (before we can close a bracket a recent opening one must exist for a balance pair to exist)
    stack = []
    for i in s:
        if i in open_paren:
            stack.append(i)
        elif i in close_paren:
            # position of closed parantheis that we will use to check matching open parenthesis index for matching location on stack
            pos = close_paren.index(i)
            # last open paren on stack
            last = len(stack)-1
            # if our stack is not empty and our current close parenthesis matches up with the last open parenthesis on the stack
            if len(stack)>0 and open_paren[pos] == stack[last]:
                # then, pop that open paren off the stack (we found a matched pair!)
                stack.pop()
            else: # balanced pair not found, return False
                return False
        elif i == "|":
            pipe.append(i)
    # if all matching parenthesis pair are popped from stack and we have no pipes to work with, then return true, we have matching pair of brackets that are balanced!        
    if len(stack) == 0 and len(pipe) == 0: 
        return True
    # if all matching parenthesis pair are popped from stack and we have an even number of pipes (balanced!), then return true, we have matching pair of brackets that are balanced! 
    elif len(stack) == 0 and len(pipe) % 2 == 0:
        return True
    # we still have open parens on the stack (unbalanced pair exists, return False)
    else:
        return False
        
# string = "{[]{()}}" # True
string = "{{||[]||}}" # True
# string = "[(])" # False
# string = "foo(bar)baz" # True
# string = "I am happy to take your donation; any amount will be greatly appreciated" # True
# string = "I (wa)n{t to buy a on}esie[...]b(u{[t]kno}w it) won't suit me." # True
# string = "This is t(he la[st random sentence I will be writing |and| I am going to stop mid-sent]" # False
print(string,"-", balancedBrackets(string))

# resources: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/?ref=rp

# python tutor - http://pythontutor.com/live.html#code=open_paren%20%3D%20%5B%22%7B%22,%22%28%22,%22%5B%22%5D%0Aclose_paren%20%3D%20%5B%22%7D%22,%22%29%22,%22%5D%22%5D%0A%23%20Complete%20the%20isBalanced%20function%20below.%0Adef%20balancedBrackets%28s%29%3A%0A%20%20%20%20pipe%20%3D%20%5B%5D%0A%20%20%20%20stack%20%3D%20%5B%5D%0A%20%20%20%20for%20i%20in%20s%3A%0A%20%20%20%20%20%20%20%20if%20i%20in%20open_paren%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20stack.append%28i%29%0A%20%20%20%20%20%20%20%20elif%20i%20in%20close_paren%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20position%20of%20closed%20parantheis%20that%20we%20will%20use%20to%20check%20matching%20open%20parenthesis%20index%20for%20matching%20location%20on%20stack%0A%20%20%20%20%20%20%20%20%20%20%20%20pos%20%3D%20close_paren.index%28i%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20last%20open%20paren%20on%20stack%0A%20%20%20%20%20%20%20%20%20%20%20%20last%20%3D%20len%28stack%29-1%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20our%20stack%20is%20not%20empty%20and%20our%20current%20close%20parenthesis%20matches%20up%20with%20the%20last%20open%20parenthesis%20on%20the%20stack%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20len%28stack%29%3E0%20and%20open_paren%5Bpos%5D%20%3D%3D%20stack%5Blast%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20then,%20pop%20that%20open%20paren%20off%20the%20stack%20%28we%20found%20a%20matched%20pair!%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20stack.pop%28%29%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%20%23%20balanced%20pair%20not%20found,%20return%20False%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20elif%20i%20%3D%3D%20%22%7C%22%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20pipe.append%28i%29%0A%20%20%20%20%23%20if%20all%20matching%20parenthesis%20pair%20are%20popped%20from%20stack%20and%20we%20have%20no%20pipes%20to%20work%20with,%20then%20return%20true,%20we%20have%20matching%20pair%20of%20brackets%20that%20are%20balanced!%20%20%20%20%20%20%20%20%0A%20%20%20%20if%20len%28stack%29%20%3D%3D%200%20and%20len%28pipe%29%20%3D%3D%200%3A%20%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%23%20if%20all%20matching%20parenthesis%20pair%20are%20popped%20from%20stack%20and%20we%20have%20an%20even%20number%20of%20pipes,%20then%20return%20true,%20we%20have%20matching%20pair%20of%20brackets%20that%20are%20balanced!%20%0A%20%20%20%20elif%20len%28stack%29%20%3D%3D%200%20and%20len%28pipe%29%20%25%202%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%23%20we%20still%20have%20open%20parens%20on%20the%20stack%20%28unbalanced%20pair%20exists,%20return%20False%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20False%0A%20%20%20%20%20%20%20%20%0A%23%20string%20%3D%20%22%7B%5B%5D%7B%28%29%7D%7D%22%20%23%20True%0A%23%20string%20%3D%20%22%7B%7B%7C%7C%5B%5D%7C%7C%7D%7D%22%20%23%20True%0Astring%20%3D%20%22%5B%28%5D%29%22%20%23%20False%0A%23%20string%20%3D%20%22foo%28bar%29baz%22%20%23%20True%0A%23%20string%20%3D%20%22I%20am%20happy%20to%20take%20your%20donation%3B%20any%20amount%20will%20be%20greatly%20appreciated%22%20%23%20True%0A%23%20string%20%3D%20%22I%20%28wa%29n%7Bt%20to%20buy%20a%20on%7Desie%5B...%5Db%28u%7B%5Bt%5Dkno%7Dw%20it%29%20won't%20suit%20me.%22%20%23%20True%0A%23%20string%20%3D%20%22This%20is%20t%28he%20la%5Bst%20random%20sentence%20I%20will%20be%20writing%20%7Cand%7C%20I%20am%20going%20to%20stop%20mid-sent%5D%22%20%23%20False%0Aprint%28string,%22-%22,%20balancedBrackets%28string%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false