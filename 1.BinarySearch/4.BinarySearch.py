

#Find the first occurance of target
#Binary search with inclusive upper limit
#Go left to explore more possibilities

def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    
    while(left<=right):
        mid = left+(right-left)//2
        if(nums[mid]>=target):
            right = mid - 1
        else:
            left = mid + 1
    return left
    
    
    
    
    

nums = [10, 10, 20, 20, 20, 30, 40]
target = 20

res = binarySearch(nums, target)
print(res)