

import math

#Logic: Find the largest integer whose square root is <= n

#Thought: Whenever we are finding the largest number or last occurance in a sorted array return right most element which satisfies the condition. 

def squareRoot(n):
    l, r = 1, n
    while (l<=r):
        mid = l + (r-l)//2
        if mid*mid <= n:
            l = mid + 1
        else:
            r = mid - 1
    return r
            

#Find the integer square root
#Time complexity = O(logn)
n = 100
res = squareRoot(n)
print(f"Square root of {n} is {math.sqrt(n)}")
print(f"Square root of {n} is {res}")
