# naive approach - 3 nested for loops O(n**3)
def find3Numbers(A,sum):
    A.sort()
    arr = []
    # Fix the first element as A[i] 
    for i in range( 0, len(A)-2): 
        # Fix the second element as A[j] 
        for j in range(i + 1, len(A)-1):  
            # Now look for the third number 
            for k in range(j + 1, len(A)): 
                if A[i] + A[j] + A[k] == sum: 
                    print("Triplet is", A[i], 
                          ", ", A[j], ", ", A[k]) 
                    # append to triplet arr
                    arr.append([A[i],A[j],A[k]])
    return arr
      

A = [12,3,1,2,-6,5,-8,6]
sum = 0
find3Numbers(A, sum)

# [[-8,2,6],[-8,3,5],[-6,1,5]]

# optimized using sorting (two-pointer technique) O(n**2)
def find3Numbers(A,sum): ## A = arr, sum = target
    # sort the array in ascending order
    A.sort()
    arr = [] # triplet
    # Fix the first element of possible triplet at A[i]
    for i in range( 0, len(A)-2): 
       # fix first pointer from left side of array
       left = i + 1
       # fix second pointer from right side of array(end)
       right = len(A)-1
       while (left<right):
            if A[i] + A[left] + A[right] == sum: 
                print("Triplet is", A[i], 
                      ", ", A[left], ", ", A[right]) 
                # append to triplet arr
                arr.append([A[i],A[left],A[right]])
                left+=1
                right-=1
             # if the sum is smaller increment left pointer to increase the sum of our sorted array 
            elif A[i] + A[left] + A[right] < sum:
              left+=1
             # else, if the sum is bigger, decrement the end, or right pointer to reduce the sum
            else: #A[i] + A[l] + A[r] > sum:
              right-=1
    # return our triplets array              
    return arr
      

A = [12,3,1,2,-6,5,-8,6]
sum = 0
find3Numbers(A, sum)

# resources: https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
# python tutor: http://pythontutor.com/live.html#code=def%20find3Numbers%28A,sum%29%3A%0A%20%20%20%20%23%20sort%20the%20array%20in%20ascending%20order%0A%20%20%20%20A.sort%28%29%0A%20%20%20%20arr%20%3D%20%5B%5D%0A%20%20%20%20%23%20Fix%20the%20first%20element%20of%20possible%20triplet%20at%20A%5Bi%5D%0A%20%20%20%20for%20i%20in%20range%28%200,%20len%28A%29-2%29%3A%20%0A%20%20%20%20%20%20%20%23%20fix%20first%20pointer%20from%20left%20side%20of%20array%0A%20%20%20%20%20%20%20left%20%3D%20i%20%2B%201%0A%20%20%20%20%20%20%20%23%20fix%20second%20pointer%20from%20right%20side%20of%20array%28end%29%0A%20%20%20%20%20%20%20right%20%3D%20len%28A%29-1%0A%20%20%20%20%20%20%20while%20%28left%3Cright%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20A%5Bi%5D%20%2B%20A%5Bleft%5D%20%2B%20A%5Bright%5D%20%3D%3D%20sum%3A%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20print%28%22Triplet%20is%22,%20A%5Bi%5D,%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22,%20%22,%20A%5Bleft%5D,%20%22,%20%22,%20A%5Bright%5D%29%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20append%20to%20triplet%20arr%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20arr.append%28%5BA%5Bi%5D,A%5Bleft%5D,A%5Bright%5D%5D%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20left%2B%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20right-%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20if%20the%20sum%20is%20smaller%20increment%20left%20pointer%20to%20increase%20the%20sum%20of%20our%20sorted%20array%20%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20A%5Bi%5D%20%2B%20A%5Bleft%5D%20%2B%20A%5Bright%5D%20%3C%20sum%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20left%2B%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20else,%20if%20the%20sum%20is%20bigger,%20decrement%20the%20end,%20or%20right%20pointer%20to%20reduce%20the%20sum%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%20%23A%5Bi%5D%20%2B%20A%5Bl%5D%20%2B%20A%5Br%5D%20%3E%20sum%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20right-%3D1%0A%20%20%20%20%23%20return%20our%20triplets%20array%20%20%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20arr%0A%20%20%20%20%20%20%0A%0AA%20%3D%20%5B12,3,1,2,-6,5,-8,6%5D%0A%23%20A%20%3D%20%5B1,2,3,4,5,6,7,8,9,15%5D%0Asum%20%3D%200%0A%23%20sum%20%3D%2030%0Afind3Numbers%28A,%20sum%29%0A&cumulative=false&curInstr=117&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false