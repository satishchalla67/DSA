
def sortArr(arr):
    n=len(arr)
    p1=0
    p2=n-1
    for i in range(n):
        if arr[i]==0 and p1<i:
            arr[p1],arr[i]=arr[i],arr[p1]
            p1+=1
        elif arr[i]==2 and p2>i:
            arr[p2],arr[i]=arr[i],arr[p2]
            p2-=1
    return arr    


arr=[2,0,2,1,1,0,1,0,1,2,2,1,0]
res=sortArr(arr)
print(arr)