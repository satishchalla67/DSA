



def findBadVersion(nums):
    l, r = 0, len(nums)-1
    while(l<=r):
        mid = l + (r-l)//2
        if nums[mid]==1:
            r = mid - 1
        else:
            l = mid + 1
    return l


#Find the bad version/ first occurance of 1
#TC = O(logn)

versions = [0,0,0,0,1,1,1,1,1]
badVersion = findBadVersion(versions)
print(badVersion)