def count(n):
    mod = 1e9 + 7
    a=1
    b=2
    for i in range(3, n + 1):
        c = (a+b) % mod
        a=b
        b=c
    return c
N = int(input())
result = count(N)
print(int(result))
