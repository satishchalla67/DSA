
#Brute Force
def binarySearch(arr, target):
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == target:
                return i, j
    return -1, -1



arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 60
row, col = binarySearch(arr, target)
print(row, col)
#TC = O(m*n)