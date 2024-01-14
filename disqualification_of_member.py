def fun(n):
    if n==1:
        return 1
    return 2*((n//2)+1 - fun(n//2));
n = int(input())
print(fun(n))
