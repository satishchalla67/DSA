








def countNegative(nums):
    l, r = 0, len(nums)-1
    while(l<=r):
        mid = l + (r-l)//2
        if nums[mid]<0:
            l = mid + 1
        else:
            r = mid - 1
    return r+1

nums = [-101, 99, 54, 21, 3, 6, 12, 19, 20, 74, 92]
res = countNegative(nums)
print(res)