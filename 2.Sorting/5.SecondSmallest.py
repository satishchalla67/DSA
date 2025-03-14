




def selectionsort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        if i==2:
            return arr[1]
    return -1





arr = [70, 20, 50, 60, 35, 47]
result = selectionsort(arr)
print(f"After sorting {result}")