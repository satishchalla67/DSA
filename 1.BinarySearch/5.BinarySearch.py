





#Find the last occurance of target
#Binary search with inclusive upper limit
#Go right to explore more possibilities

def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while(left<=right):
        mid = left + (right-left)//2
        if(nums[mid]<=target):
            left = mid + 1
        else:
            right = mid - 1
    return right
    
    
    

nums = [10, 10, 20, 20, 20, 20, 40]
target = 20

res = binarySearch(nums, target)
print(res)