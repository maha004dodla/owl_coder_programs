def factors(n):
    l=[]
    i=2
    while(i<=n):
        if(n%i==0):
            l.append(i)
            n=n//i
        else:
            i+=1
    return l
def dig(a):
    s=0
    b=str(a)
    for i in b:
        s+=int(i)
    return s
def dsum(l):
    ans=0
    for i in l:
        ans+=dig(i)
    return ans
n = int(input())
l=factors(n)
if(dsum(l)==dig(n)):
    print(1)
else:
    print(0)
