
def ternarySearch(arr, target):
    l, r = 0, len(arr)-1
    while (l<=r):
        mid1 = l + (r-l)//3
        mid2 = l + (r-l)//3
        if arr[mid1] == target:
            return mid1
        elif arr[mid2] == target:
            return mid2
        elif arr[mid1]>target:
            r = mid1 - 1
        elif arr[mid2]<target:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1



arr = [20,25,47,56,59,63,65,79,82]
target = 65
res = ternarySearch(arr, target)
print(res)