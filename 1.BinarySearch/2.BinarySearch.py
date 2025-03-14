


#Regular binary search
#Time complexity - O(logn)

def binarySearch(arr, a):
    l=0
    r=len(arr)-1
    
    while(l<=r):
        mid = l+(r-l)//2
        if arr[mid] == a:
            return mid
        elif arr[mid]>a:
            r = mid -1
        else:
            l = mid +1


arr = [23,25,33,34,40,44,56,67,71,89,90]
a = 71
resIndex = binarySearch(arr, a)
print(resIndex)