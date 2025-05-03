






def mergeProcedure(arr,p,mid,q):
    m = mid-p+1
    n = q-mid
    leftarray = [0]*m
    rightarray = [0]*n
    for i in range(m):
        leftarray[i] = arr[p+i]
    for j in range(n):
        rightarray[j] = arr[mid+1+j]
    i=0
    j=0
    k=p
    while i<m and j<n:
        if leftarray[i]<rightarray[j]:
            arr[k]=leftarray[i]
            i+=1
        else:
            arr[k]=rightarray[j]
            j+=1
        k+=1
    while i<m:
        arr[k]=leftarray[i]
        i+=1
        k+=1
    while j<n:
        arr[k]=rightarray[j]
        j+=1
        k+=1

def mergeSort(arr,i,j):
    if i<j:
        mid = i + (j-i)//2
        mergeSort(arr, i, mid)
        mergeSort(arr, mid+1, j)
        mergeProcedure(arr,i,mid,j)
    return arr

arr = [50,70,65,13,80,62,98,27]
n = len(arr)
sortedArr = mergeSort(arr,0,n-1)
print(sortedArr)