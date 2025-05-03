def findmaxmin(arr, i, j):
    max_val = 0
    min_val = 0
    if (i==j):
        max_val = arr[i]
        min_val = arr[j]
    elif (i==j-1):
        if arr[i]>arr[j]:
            max_val = arr[i]
            min_val = arr[j]
        else:
            max_val = arr[j]
            min_val = arr[i]
    else:
        mid = i + (j-i)//2 #Divide
        max_1, min_1 = findmaxmin(arr, i, mid) #conquer
        max_2, min_2 = findmaxmin(arr, mid+1, j)
        
        if max_1>max_2: #combine
            max_val = max_1
        else:
            max_val = max_2
        if min_1>min_2:
            min_val = min_2
        else:
            min_val = min_1
    return max_val, min_val    

#tc = O(n)
arr = [75,45,95,50,60,67,29,32]
n = len(arr)
max, min = findmaxmin(arr, 0, n-1)
print(f"max: {max}, min: {min}")