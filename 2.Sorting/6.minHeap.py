

#tc = O(nlogn)
def buildHeap(arr):
    n = len(arr)
    startIndex = (n//2)-1
    for i in range(startIndex, -1, -1):
        minHeapify(arr,n,i)
def minHeapify(arr,n,i):
    smallest = i
    l = 2*i+1
    r = 2*i+2
    if(l<n and arr[l]<arr[smallest]):
        smallest = l
    if(r<n and arr[r]<arr[smallest]):
        smallest = r
    if smallest!=i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        minHeapify(arr, n, smallest)
        
# def heapSort(arr):
#     buildHeap(arr)
#     n = len(arr)
    
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         minHeapify(arr, i, 0)   


arr = [75,25,35,45,90,80,60,20,30]
buildHeap(arr)
print(arr)