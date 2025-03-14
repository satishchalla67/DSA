


def linearSearch(arr, a):
    for i in range(len(arr)):
        if a==arr[i]:
            return i
    return -1




arr = [3,4,6,7,2,1,6,7,9,1]
a = 20
res = linearSearch(arr, a)
print(res)