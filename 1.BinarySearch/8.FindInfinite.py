
def findInf(nums):
    left, right = 0, len(nums)-1
    while(left<=right):
        mid = left + (right-left)
        if (nums[mid] == float('inf')):
            right = mid - 1
        else:
            left = mid + 1
    return left



#Find the first occurance of infinity
nums = [-23, 40, 51, 1, 2, 27, -89, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
res = findInf(nums)
print(res)