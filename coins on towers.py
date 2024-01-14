n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if((a+b)%3):
        print("NO")
    else:
        if(abs(a-b)>min(a,b)):
            print("NO")
        else:
            print("YES")
