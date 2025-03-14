






#Time complexity - O(n2)
def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


arr = [70, 20, 50, 60, 35, 47]
result = selectionsort(arr)
print(f"After sorting {result}")