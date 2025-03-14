





def perfectSquare(num):
    l, r = 1, num
    while(l<=r):
        mid = l + (r-l)//2
        if mid*mid == num:
            return True
        elif mid*mid > num:
            r = mid - 1
        else:
            l = mid + 1
    return False

#Retun True if the num is perfect square else false
num = [4, 9, 16, 25, 36, 40]
res = [perfectSquare(n) for n in num]
print(res)