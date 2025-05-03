



def partition(arr,p,q):
    pivot=arr[p]
    i=p
    for j in range(i+1, q+1):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j], arr[i]
    arr[p],arr[i]=arr[i],arr[p]
    return i

def quickSelect(arr,p,q,k):
    if p<q:
        mid=partition(arr,p,q)
        if mid==k:
            return arr[mid]
        elif mid>k:
            return quickSelect(arr,p,mid-1,k)
        else:
            return quickSelect(arr,mid+1,q,k)
    return -1

arr = [50,70,65,13,80,62,98,27]
k=2
res=quickSelect(arr,0,len(arr)-1,k-1)
print(res)