








def peakElement(arr):
    for i in range(1, len(arr)-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            return i
    return -1

arr=[1,2,2,1,2,0]
res=peakElement(arr)
print(res)