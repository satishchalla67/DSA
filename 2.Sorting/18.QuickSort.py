
def partition(arr,p,q):
    pivot=arr[p]
    i=p
    j=i+1
    while j<=q:
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    arr[i], arr[p] = arr[p], arr[i]
    return i

def quickSort(arr,p,q):
    if p<q:
        mid=partition(arr,p,q)
        quickSort(arr,p,mid-1)
        quickSort(arr,mid+1,q)
    return arr
arr = [50,70,65,13,80,62,98,27]
n = len(arr)
sortedArr = quickSort(arr,0,n-1)
print(sortedArr)