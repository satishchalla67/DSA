



#Binary Search using Recursion




def binarySearch(nums, target, l, r):
    mid = l+(r-l)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binarySearch(nums, target, l, mid-1)
    else:
        return binarySearch(nums, target, mid+1, r)
    



nums = [10,20,30,40,50,60,70,80,90]
target = 90
res = binarySearch(nums, target, 0, len(nums)-1)
print(res)