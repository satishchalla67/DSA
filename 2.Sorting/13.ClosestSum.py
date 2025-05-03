
def closestSum(arr, target):
    i = 0
    j = i+2
    n=len(arr)
    res = -1
    min_dist = float('inf')
    while j < n:
        windowSum = sum(arr[i:j+1])
        print(arr[i], arr[i+1], arr[j])
        dist = abs(windowSum-target)
        if dist<min_dist:
            min_dist = dist
            res = windowSum
        i+=1
        j+=1
    return res

arr= [-1,2,1,-4,-1,0,2]
target = 1
#find three integers such that sum closest to the target
#output = 2, -1+2+1=2 wil be the closest to the target
output = closestSum(arr, target)
print(output)