def large(n,k):
    s=list(map(int,str(n)))
    l=[]
    for i in s:
        while(k>0 and l and l[-1]<i):
            l.pop()
            k-=1
        l.append(i)
    while(k>0):
        l.pop()
        k-=1
    return l
n,k=map(int,input().split())
res=large(n,k)
ans=""
for i in res:
    ans+=str(i)
print(ans)
