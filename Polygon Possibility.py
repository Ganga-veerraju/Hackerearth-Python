t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k=max(a)
    s=sum(a)
    d=s-k
    if (k<d):
             print("Yes")
    else:
            print("No")
