



def buildHeap(arr):
    n=len(arr)
    startIndex=(n//2)-1
    for i in range(startIndex, -1, -1):
        heapify(arr,i,n)
        
def heapify(arr,i,n):
    smallest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[smallest]:
        smallest=left
    if right<n and arr[right]>arr[smallest]:
        smallest=right
    if smallest!=i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr,smallest,n)
        
def ksmallest(arr,k):
    buildHeap(arr)
    n=len(arr)-1
    curr=0
    for i in range(k):
        curr=arr[0]
        arr[0], arr[n-i] = arr[n-i], arr[0]
        heapify(arr,0, n-i)
    return curr



arr=[40,25,68,79,52,66,89,97]
k=1
res=ksmallest(arr,k)
print(res)