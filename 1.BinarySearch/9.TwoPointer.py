



#Two Sum


def twoSum(nums, target):
    left, right = 0, len(nums)-1
    while(left<right):
        if nums[left]+nums[right]==target:
            return nums[left], nums[right]
        elif nums[left]+nums[right]>target:
            right-=1
        else:
            left+=1
    return -1, -1


nums = [20,40,60,80,90,105,240]
target = 210
num1, num2 = twoSum(nums, target)
print(num1, num2)