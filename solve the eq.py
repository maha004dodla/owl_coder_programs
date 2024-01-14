def solve(n):
    i=3
    while(1):
        if(((i*i)+i+1)==n):
            return i
        i+=1
t=int(input())
for i in range(t):
    n=int(input())
    print(solve(n))
