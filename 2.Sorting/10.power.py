
def power(a, n):
    #small problem
    if n==0:
        return 1
    if n==1:
        return a
    else:
        b = power(a, n//2)
    if n%2==0:
        return b*b
    return b*b*a


a = 2
n = 10
res = power(a, n)
print(res)
print(a**n)