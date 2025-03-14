





#Time complexity - O(n2)
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [70, 20, 50, 60, 35, 47]
result = bubblesort(arr)
print(f"After sorting {result}")