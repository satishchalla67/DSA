
def majorityElement(nums):
    curr=nums[0]
    j=1
    for i in range(1, len(nums)):
        if curr==nums[i]:
            j+=1
        else:
            j-=1
        if j==0:
            curr = nums[i]
            j=1
    if nums.count(curr)>len(nums)//2:
        return curr
    else:
        return -1

nums = [1,2,3,2,2,1,2,4,2]
res=majorityElement(nums)
print(res)