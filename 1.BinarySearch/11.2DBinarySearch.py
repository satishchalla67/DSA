

def binarySearch(arr, target):
    l = 0
    r = len(arr) * len(arr[0])-1
    n = len(arr[0])
    while (l<=r):
        mid = l+(r-l)//2
        if(arr[mid//n][mid%n]==target):
            return mid//n, mid%n
        elif(arr[mid//n][mid%n]>target):
            r = mid-1
        else:
            l = mid+1
    return -1, -1


arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 34
row, col = binarySearch(arr, target)
print(row, col)
#Time complexity = log(m*n)