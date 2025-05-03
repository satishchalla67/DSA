#tc = O(nlogn)
def buildHeap(arr): 
    n = len(arr)
    startIndex = (n//2)-1
    for i in range(startIndex, -1, -1):
        maxHeapify(arr, n, i)
        
def maxHeapify(arr, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if (l<n and arr[l]>arr[largest]):
        largest = l
    if (r<n and arr[r]>arr[largest]):
        largest = r
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        maxHeapify(arr, n, largest)

def heapSort(arr):
    buildHeap(arr)
    
    n = len(arr)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, i, 0)


arr = [75,25,35,45,90,80,60,20,30]
heapSort(arr)
print(arr)