def count_bin(n):
    mod = 1e9 + 7
    a=1
    b=2
    for i in range(2, n + 1):
        c = (a+b) % mod
        a=b
        b=c
    return c
N = int(input())
result = count_bin(N)
print(int(result))
