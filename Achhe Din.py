t=int(input())
for  _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        p=a.count(a[i])
        if(a.count(a[i])==1):
           print(a[i])
           #print(p)
